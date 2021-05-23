import firebase_admin
from firebase_admin import db

from utils.peopletracker import PeopleTracker
from utils.trackablepeople import TrackableObject
from utils import config
import numpy as np
import argparse, imutils
import time, dlib, cv2

t0 = time.time()

""" Connect to Firebase Realtime """
creds = firebase_admin.credentials.Certificate('creds/countly-19.json')
firebase_admin.initialize_app(creds, {
    'databaseURL': "https://countly-19-default-rtdb.europe-west1.firebasedatabase.app"
})


def load_model():
    """ Load detection model """
    return cv2.dnn.readNetFromCaffe('models/MobileNetSSD_deploy.prototxt',
                                    'models/MobileNetSSD_deploy.caffemodel')


def draw_prediction_line(frame, width, height, i):
    """ Draw a prediction line """
    cv2.line(frame, (0, height // 2), (width, height // 2), color=(0, 0, 0), thickness=2)
    cv2.putText(frame, "-Prediction line-", (10, height - ((i * 20) + 200)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color=(0, 0, 0), thickness=1)


def draw_object_id(frame, object_id, centroid):
    """ Draw object ID """
    cv2.putText(frame, f"ID: {object_id}", (centroid[0] - 10, centroid[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.circle(frame, (centroid[0], centroid[1]), 4, (255, 255, 255), -1)


def draw_tracking_information(frame, height, cnt_in, cnt_out, sum_people):
    """ Plot tracking information """
    cv2.putText(frame, f"Enter: {cnt_in}", (10, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.putText(frame, f"Exit: {cnt_out}", (10, height - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.putText(frame, f"Total people inside: {sum_people}", (265, height - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)


def send_to_firebase(current_time, count):
    """ Send data to Firebase Realtime """
    ref = db.reference("/stores")
    store_id = ref.child('HuTUAOOYnaJMNBxTsf70')
    store_id.update({current_time: count})


def parse_arguments():
    # construct the argument parse and parse the arguments
    args = argparse.ArgumentParser()
    args.add_argument("-i", "--input", type=str,
                      help="path to optional input video file")
    return vars(args.parse_args())


def run():

    ###############################
    ###     INITIALIZATION      ###
    ###############################

    args = parse_arguments()

    # load model
    net = load_model()

    # initialize width and height of the frame
    width, height = None, None

    # initialize tracker
    ct = PeopleTracker(maxDisappeared=30, maxDistance=30)
    trackers = []
    tracked_people = {}

    total_frames = 0
    cnt_in = 0
    cnt_out = 0
    total = []

    print("[INFO] Starting the video..")
    vs = cv2.VideoCapture(args["input"])

    ###############################
    ###  END OF INITIALIZATION  ###
    ###############################

    while True:
        frame = vs.read()
        frame = frame[1]

        # if frame is None, the video reach end
        if frame is None:
            break

        # resize the video to 500 pixels and convert to RGB
        frame = imutils.resize(frame, width=500)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # set the width and the height of the frame
        if width is None or height is None:
            (height, width) = frame.shape[:2]

        entrance = height / 2

        bboxes = []

        run_detection = total_frames % config.skip_frames == 0
        if run_detection:
            print("[INFO] Start with detecting")
            trackers = []

            # convert the frame to a blob and start with the detection
            blob = cv2.dnn.blobFromImage(frame, 0.007843, (width, height), 127.5)
            net.setInput(blob)

            detections = net.forward()
            for i in np.arange(0, detections.shape[2]):
                # get the confidence
                confidence = detections[0, 0, i, 2]
                if confidence > config.confidence:
                    idx = int(detections[0, 0, i, 1])

                    # if the class label is not a person, ignore it
                    if config.model_classes[idx] != "person":
                        continue

                    # get position (x, y) of the bounding box of the detected person
                    box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
                    (x_start, y_start, x_end, y_end) = box.astype("int")

                    # get bounding box of and start tracking the person
                    tracker = dlib.correlation_tracker()
                    rect = dlib.rectangle(x_start, y_start, x_end, y_end)
                    tracker.start_track(rgb, rect)

                    # add the tracker to the current list of trackers
                    trackers.append(tracker)
        else:
            for tracker in trackers:
                print("[INFO] Start with tracking")

                # update the tracker and us ecurrent position
                tracker.update(rgb)
                position = tracker.get_position()

                # unpack the position object
                x_start, y_start, x_end, y_end = int(position.left()), \
                                                 int(position.top()), \
                                                 int(position.right()), \
                                                 int(position.bottom())

                # add the bounding box coordinates to the rectangles list
                bboxes.append((x_start, y_start, x_end, y_end))

        if config.draw:
            # draw a prediction line, determine whether person going up (out of the "store") or down (in the "store")
            draw_prediction_line(frame, width, height, i)

        # get current people on the video
        visible_people = ct.update(bboxes)
        for (people_id, position) in visible_people.items():
            # get current tarcked object
            tracked_person = tracked_people.get(people_id, None)

            # if there is no existing trackable object, create one
            if tracked_person is None:
                tracked_person = TrackableObject(people_id, position)
            else:
                # get the moving direction of the tracked person id and determine if the person is moving out or in
                current_position_y = [pos[1] for pos in tracked_person.position]
                direction = position[1] - np.mean(current_position_y)
                tracked_person.position.append(position)

                # check to see if the object has been counted or not
                if not tracked_person.is_counted:
                    # if direction negative and position is below the limit then person goes out of the store
                    if direction < 0 and position[1] < entrance:
                        cnt_out += 1
                        tracked_person.is_counted = True
                        send_to_firebase(int(time.time() * 1000), -1)

                    # if direction positive and position is above the limit then person goes in the store
                    elif direction > 0 and position[1] > entrance:
                        cnt_in += 1
                        tracked_person.is_counted = True
                        send_to_firebase(int(time.time() * 1000), 1)

                    total = cnt_in - cnt_out

            # store the trackable object in our dictionary
            tracked_people[people_id] = tracked_person

            if config.draw:
                draw_object_id(frame, people_id, position)

        if config.draw:
            draw_tracking_information(frame, height, cnt_in, cnt_out, total)

        # show the output frame
        cv2.imshow("Real-Time monitoring", frame)
        cv2.waitKey(1)

        total_frames += 1

    # close any open windows
    cv2.destroyAllWindows()


run()
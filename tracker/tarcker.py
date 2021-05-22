import datetime as datetime

from utils.centroidtracker import CentroidTracker
from utils.trackableobejct import TrackableObject
from imutils.video import VideoStream
from imutils.video import FPS
from utils import config
import time, schedule, csv
import numpy as np
import argparse, imutils
import time, dlib, cv2
import datetime
from itertools import zip_longest

t0 = time.time()


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


def draw_tracking_information(frame, height, cnt_in, cnt_out, status, sum_people):
    """ Plot tracking information """
    cv2.putText(frame, f"Enter: {cnt_in}", (10, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.putText(frame, f"Exit: {cnt_out}", (10, height - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.putText(frame, f"Status: {status}", (10, height - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.putText(frame, f"Total people inside: {sum_people}", (265, height - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)


def check_people_limit(frame, sum_people):
    """ Check if the limit is exceeded """
    if sum_people >= config.max_limit:
        cv2.putText(frame, "-ALERT: People limit exceeded-", (10, frame.shape[0] - 80),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)
        print("WARNING: There are too many people inside the store.")


def save_data(cnt_in, cnt_out, sum_people):
    datetime = [datetime.datetime.now()]
    d = [datetime, cnt_in, cnt_out, sum_people]
    export_data = zip_longest(*d, fillvalue = '')

    with open('Log.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(("End Time", "In", "Out", "Total Inside"))
        wr.writerows(export_data)


def parse_arguments():
    # construct the argument parse and parse the arguments
    args = argparse.ArgumentParser()
    args.add_argument("-p", "--prototxt", required=False,
                      help="path to Caffe 'deploy' prototxt file")
    args.add_argument("-m", "--model", required=True,
                      help="path to Caffe pre-trained model")
    args.add_argument("-i", "--input", type=str,
                      help="path to optional input video file")
    args.add_argument("-c", "--confidence", type=float, default=0.4,
                      help="minimum probability to filter weak detections")
    args.add_argument("-s", "--skip-frames", type=int, default=30,
                      help="# of skip frames between detections")
    return vars(args.parse_args())


def run():

    ###############################
    ###     INITIALIZATION      ###
    ###############################

    args = parse_arguments()

    # define mobileNet classes to detect
    CLASSES = config.model_classes

    # load model
    net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

    # initialize width and height of the frame
    width, height = None, None

    # initialize tracker
    ct = CentroidTracker(maxDisappeared=40, maxDistance=50)
    trackers = []
    tracked_people = {}

    total_frames = 0
    cnt_in = 0
    cnt_out = 0
    total = []

    # start the frames per second throughput estimator
    fps = FPS().start()

    # if a video path was not supplied, grab a reference to the ip camera
    if not args.get("input", False):
        print("[INFO] Starting the live stream..")
        vs = VideoStream(config.url).start()
        time.sleep(2.0)

    # otherwise, grab a reference to the video file
    else:
        print("[INFO] Starting the video..")
        vs = cv2.VideoCapture(args["input"])

    ###############################
    ###  END OF INITIALIZATION  ###
    ###############################

    while True:
        frame = vs.read()
        frame = frame[1] if args.get("input", False) else frame

        # if we are viewing a video and we did not grab a frame then we
        # have reached the end of the video
        if args["input"] is not None and frame is None:
            break

        # resize the video to 500 pixels and convert to RGB
        frame = imutils.resize(frame, width=500)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # set the width and the height of the frame
        if width is None or height is None:
            (height, width) = frame.shape[:2]

        # initialite current status and list of bounding boxes
        status = "Waiting"
        bboxes = []

        run_detection = total_frames % args["skip_frames"] == 0
        if run_detection:
            status = "Detecting"
            trackers = []

            # convert the frame to a blob and start with the detction
            blob = cv2.dnn.blobFromImage(frame, 0.007843, (width, height), 127.5)
            net.setInput(blob)
            detections = net.forward()

            # loop over the detections
            for i in np.arange(0, detections.shape[2]):
                # get the confidence
                confidence = detections[0, 0, i, 2]

                if confidence > args["confidence"]:
                    # get the index
                    idx = int(detections[0, 0, i, 1])

                    # if the class label is not a person, ignore it
                    if CLASSES[idx] != "person":
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
                status = "Tracking"

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
                    # if direction negative and centroid is above the center line, count out
                    if direction < 0 and position[1] < height // 2:
                        cnt_out += 1
                        tracked_person.is_counted = True

                    # if direction positive and centroid is below the center line, count in
                    elif direction > 0 and position[1] > height // 2:
                        cnt_in += 1
                        tracked_person.is_counted = True

                        # check if there is too many people inside
                        check_people_limit(frame, total)

                    total = cnt_in - cnt_out
            print(f"Count in: {cnt_in}, count out: {cnt_out}, total: {total}, time: {datetime.datetime.now()}")

            # store the trackable object in our dictionary
            tracked_people[people_id] = tracked_person

            draw_object_id(frame, people_id, position)

        draw_tracking_information(frame, height, cnt_in, cnt_out, status, total)

        # Initiate a simple log to save data at end of the day
        if config.save_data:
            save_data(cnt_in, cnt_out, total)

        # show the output frame
        cv2.imshow("Real-Time Monitoring/Analysis Window", frame)
        key = cv2.waitKey(1)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

        total_frames += 1
        fps.update()

    # stop the timer and display FPS information
    fps.stop()
    print(f"[INFO] elapsed time: {fps.elapsed()}")
    print(f"[INFO] approx. FPS: {fps.fps()}")

    # close any open windows
    cv2.destroyAllWindows()


run()
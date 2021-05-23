from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np


class PeopleTracker:
    def __init__(self, maxDisappeared=50, maxDistance=50):
        self.next_person_id = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()
        self.maxDisappeared = maxDisappeared
        self.maxDistance = maxDistance

    def register(self, centroid):
        """ Register tracker """
        self.objects[self.next_person_id] = centroid
        self.disappeared[self.next_person_id] = 0
        self.next_person_id += 1

    def deregister(self, person_id):
        """ De-register the tracker """
        del self.objects[person_id]
        del self.disappeared[person_id]

    def update(self, rects):
        """ Update tracker """
        if len(rects) == 0:
            for person_id in list(self.disappeared.keys()):
                self.disappeared[person_id] += 1

                # deregister tracker if we reach maximum number of frames
                if self.disappeared[person_id] > self.maxDisappeared:
                    self.deregister(person_id)

            return self.objects

        # initialize current positions of persons on current frame
        input_positions = np.zeros((len(rects), 2), dtype="int")

        for (i, (startX, startY, endX, endY)) in enumerate(rects):
            cX = int((startX + endX) / 2.0)
            cY = int((startY + endY) / 2.0)
            input_positions[i] = (cX, cY)

        # if we do not track any objects, register input person positions
        if len(self.objects) == 0:
            for i in range(0, len(input_positions)):
                self.register(input_positions[i])

        else:
            # grab the set of object IDs and corresponding centroids
            person_ids = list(self.objects.keys())
            objectCentroids = list(self.objects.values())

            D = dist.cdist(np.array(objectCentroids), input_positions)

            rows = D.min(axis=1).argsort()
            cols = D.argmin(axis=1)[rows]

            usedRows = set()
            usedCols = set()

            for (row, col) in zip(rows, cols):
                if row in usedRows or col in usedCols:
                    continue

                if D[row, col] > self.maxDistance:
                    continue

                objectID = person_ids[row]
                self.objects[objectID] = input_positions[col]
                self.disappeared[objectID] = 0

                usedRows.add(row)
                usedCols.add(col)

            unusedRows = set(range(0, D.shape[0])).difference(usedRows)
            unusedCols = set(range(0, D.shape[1])).difference(usedCols)

            # check if some points dissapeared
            if D.shape[0] >= D.shape[1]:
                for row in unusedRows:
                    objectID = person_ids[row]
                    self.disappeared[objectID] += 1

                    if self.disappeared[objectID] > self.maxDisappeared:
                        self.deregister(objectID)

            # register new trackable object
            else:
                for col in unusedCols:
                    self.register(input_positions[col])

        # return the set of trackable objects
        return self.objects
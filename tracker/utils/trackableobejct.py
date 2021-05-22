class TrackableObject:
    def __init__(self, people_id, position):
        self.people_id = people_id
        self.position = [position]
        self.is_counted = False
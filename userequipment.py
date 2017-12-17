class UserEquipment:
    def __init__(self, multipoint_array, valid_capacity):
        self.multipoint_array = multipoint_array
        self.valid_capacity = valid_capacity
        self.access_point_id = None

    @property
    def get_point(self):
        return self.point

    def assign_access_point(self, access_point_id):
        self.access_point_id = access_point_id

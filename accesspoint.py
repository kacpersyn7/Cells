class AccessPoint:

    def __init__(self, point, max_power, max_users, max_range, users, id):
        self.point = point
        self.area = self.point.buffer(max_range, resolution=16)  # make a circle
        self.max_power = max_power
        self.max_users = max_users
        self.max_range = max_range
        self.users = users
        self.id = id
        return self

    def get_power(self, ue):
        distance = self.point.distance(ue)
        if distance < self.max_range:
            return self.max_power / (distance * distance)
        else:
            return 0

    def add_user(self):
        if (self.users <= self.max_users):
            self.users = self.users + 1

    # sorted matrix first by x_coord, second for y_coord
    def search_for_ues(self, ues, ue_dict):
        # left_x = bisect.bisect_left(sorted_users_list, self.point.bounds[0])
        # right_x = bisect.bisect_right(sorted_users_list, self.point.bounds[2])
        # list_by_x = sorted_users_list[left_x:right_x]
        # for point in list_by_x:
        potential_ues = ues.intersection(self.area)
        for point in potential_ues:
            ue_dict[point].assign_access_point(self.id)

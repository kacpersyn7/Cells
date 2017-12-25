class AccessPoint:

    def __init__(self, x, y, max_power=10, max_range=10, max_users=0, users=0, id=0):
        self.x = x
        self.y = y
        # self.area = self.point.buffer(max_range, resolution=16)  # make a circle
        self.max_power = max_power
        self.max_users = max_users
        self.max_range = max_range
        self.users = users
        self.id = id

    def get_power(self, ue_x, ue_y):
        distance = ue_x * ue_x + ue_y * ue_y
        return self.max_power / (distance)

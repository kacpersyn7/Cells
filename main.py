import numpy as np

COLS = 20
ROWS = 20


def generate_area(x, y, resolution):
    area = np.zeros((x, y))
    return area


def get_power(ap_x, ap_y, ue_x, ue_y, max_power):
    distance = ((ue_x - ap_x) ** 2 + (ue_y - ap_y) ** 2).astype(float)
    distance[np.where(distance == 0)[0]] = 0.5
    print(distance)
    return (1. / (distance)) * max_power


def update_result_area(accesspoint_bitmap, result_area, cols=COLS, rows=ROWS, max_power=400,
                       activation_area=lambda x, y: x * x + y * y <= 16):
    accesspoint_ones = np.where(accesspoint_bitmap == 0)
    new_result_area = np.copy(result_area)
    for x, y in zip(accesspoint_ones[0], accesspoint_ones[1]):
        temp_y, temp_x = np.ogrid[-x:cols - x, -y:rows - y]
        mask_indexes = np.where(activation_area(temp_x, temp_y))
        print(mask_indexes)
        new_result_area[mask_indexes] = get_power(x, y, mask_indexes[0], mask_indexes[1], max_power)
        diff = np.where((new_result_area - result_area) < 0)
        new_result_area[diff] = result_area[diff]
        result_area = np.copy(new_result_area)
    return new_result_area


def generate_individuals(n=10, cols=COLS, rows=ROWS):
    individuals = np.zeros((n, cols, rows))
    for i in range(n):
        individuals[i] = (np.random.randint(0, 10, size=(cols, rows)))
    return individuals


def generate_users(max_request, cols=COLS, rows=ROWS):
    return np.random.randint(0, max_request, size=(cols, rows))


def second_target_function(power_area, accesspoint_area, users_area, cost_of_accesspoint):
    cost_function = np.sum(accesspoint_area == 0) * cost_of_accesspoint
    print(np.sum(accesspoint_area == 0))
    quality_function = np.sum(users_area * (power_area - users_area))
    return quality_function - cost_function


users = generate_users(250)
aps = generate_individuals()
power_a = np.zeros((COLS, ROWS))

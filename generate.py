import numpy as np
from shapely.geometry import asMultiPoint

ues_points_list = asMultiPoint(np.array([[1, 2], [0, 1], [5, 6]]))
accesspoints_points_list = asMultiPoint(np.array([[0, 0], [9, 9]]))

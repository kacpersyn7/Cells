COLS = 20
ROWS = 20

access_points_types = [{'cost': 100, 'max_power': 10, 'access_area_fun': lambda x,
                                                                                y: x * x + y * y <= 9,
                        'dist_fun': lambda diff_x, diff_y: (diff_x * diff_x + diff_y * diff_y).astype(float)},

                       {'cost': 213, 'max_power': 20, 'access_area_fun': lambda x,
                                                                                y: x * x + y * y <= 16,
                        'dist_fun': lambda diff_x, diff_y: (diff_x * diff_x + diff_y * diff_y).astype(float)}
                       ]

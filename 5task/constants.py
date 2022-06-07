import numpy as np

CP = {
    'back': (189, 172, 161),
    0: (204, 192, 179),
    1: (238, 228, 219),
    2: (240, 226, 202),
    3: (242, 177, 121),
    4: (236, 141, 85),
    5: (250, 123, 92),
    6: (234, 90, 56),
    7: (237, 207, 114),
    8: (242, 208, 75),
    9: (237, 200, 80),
    10: (227, 186, 19),
    11: (236, 196, 2),
    12: (96, 217, 146)
}

TEST_GRID = np.array([[2, 4, 8, 16],
                      [32, 64, 128, 256],
                      [512, 1024, 2048, 4096],
                      [0, 0, 0, 0]])

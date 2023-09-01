# corner cutting algorithm

import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Qt5Agg')

points_dict = {

}


def corner_cutting(points, num_iter):
    """
    Applies corner cutting algorithm to the given points
    :param points: list of points
    :param num_iter: number of iterations
    :return: list of points
    """
    if num_iter == 0:
        return points
    else:
        new_points = []
        for i in range(len(points) - 1):
            pi_minus_1 = points[i-1]
            pi_0 = points[i]
            pi_plus_1 = points[i+1]
            pi_plus_2 = points[(i+2)%len(points)]

            q1 = pi_0
            q2 = (1/16)*(-pi_minus_1 + 9*pi_0 + 9*pi_plus_1 - pi_plus_2)
            new_points.append(q1)
            new_points.append(q2)
        new_points.append(new_points[0])
        
        points_dict[num_iter] = np.array(new_points)
        return corner_cutting(np.array(new_points), num_iter - 1)


def main():
    points = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], dtype=np.float64)
    points_dict[0] = points
    points = np.array(corner_cutting(points, 5))
    # print(points_dict)
    # plt.plot(points[:, 0], points[:, 1])
    for key in points_dict:
        plt.plot(points_dict[key][:, 0], points_dict[key][:, 1])
    plt.show()


if __name__ == '__main__':
    main()



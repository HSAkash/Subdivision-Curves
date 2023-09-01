# chaikin's scheme for curve smoothing

import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Qt5Agg')

points_dict = {

}


def chaikin_scheme(points, num_iter):
    """
    Applies chaikin's scheme to the given points
    :param points: list of points
    :param num_iter: number of iterations
    :return: list of points
    """
    if num_iter == 0:
        return points
    else:
        new_points = []
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            q1 = 3 / 4 * p1 + 1 / 4 * p2
            q2 = 1 / 4 * p1 + 3 / 4 * p2
            new_points.append(q1)
            new_points.append(q2)
        new_points.append(new_points[0])
        
        points_dict[num_iter] = np.array(new_points)
        return chaikin_scheme(new_points, num_iter - 1)


def main():
    points = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], dtype=np.float64)
    points_dict[0] = points
    points = np.array(chaikin_scheme(points, 10))
    # print(points_dict)
    # plt.plot(points[:, 0], points[:, 1])
    for key in points_dict:
        plt.plot(points_dict[key][:, 0], points_dict[key][:, 1])
    plt.show()


if __name__ == '__main__':
    main()
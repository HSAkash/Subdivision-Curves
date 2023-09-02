# Four point algorithm

import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Qt5Agg')

points_dict = {}

def getFigureSize(points, param = 8):
    """
    Calculates the size of the figure
    :param points: numpy array of points & shape (n, 2)
    :return: size of the figure
    """
    x_min = np.min(points[:, 0])
    x_max = np.max(points[:, 0])
    y_min = np.min(points[:, 1])
    y_max = np.max(points[:, 1])
    ratio = (x_max - x_min) / (y_max - y_min)
    if ratio > 2:
        ratio = 2
    elif ratio < 0.5:
        ratio = 0.5
    fig_x = param if ratio >= 1 else param*ratio
    fig_y = param/ratio if ratio >= 1 else param
    return (fig_x, fig_y)
    

def isConnected(points):
    """
    Checks if the points are connected
    :param points: numpy array of points & shape (n, 2)
    :return: True if connected, False otherwise
    """
    return np.array_equal(points[0], points[-1])


def four_point(points, num_iter, is_connect=False):
    """
    Applies four point algorithm to the given points
    :param points: numpy array of points & shape (n, 2)
    :param num_iter: number of iterations
    :param is_connect: boolean
    :return: list of points dtype(numpy array)
    """
    if num_iter == 0:
        return points
    

    new_points = []
    # if points are not connected, add the first point to the new points
    if not is_connect:
        new_points.append(points[0])

    for i in range(len(points) - 1):
        pi_minus_1 = points[i-1]
        pi_0 = points[i]
        pi_plus_1 = points[i+1]
        pi_plus_2 = points[(i+2)%len(points)]

        q1 = pi_0
        q2 = (1/16)*(-pi_minus_1 + 9*pi_0 + 9*pi_plus_1 - pi_plus_2)
        new_points.append(q1)
        new_points.append(q2)

    # if points are connected, add the first point to the new points
    if is_connect:
        new_points.append(new_points[0])
    # if points are not connected, add the last point to the new points
    else:
        new_points.append(points[-1])
    
    # list to numpy array
    new_points = np.array(new_points)
    # every iteration, add the new points to the dictionary
    points_dict[num_iter] =new_points
    # return the new points and call the function recursively

    return four_point(new_points, num_iter - 1, is_connect)


def main():
    # initialize the points
    # points = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], dtype=np.float64)
    points = np.array([[0, 0], [0, 1], [1, 1], [1, 0], [2, 0], [2, 1], [3, 1], [3, 0], [4, 0],[4,1], [5, 1]], dtype=np.float64)
    # add the points to the dictionary 
    points_dict[0] = points
    # call the function 
    points = four_point(points, 10, isConnected(points))
    # plot the points
    figsize = getFigureSize(points)
    plt.figure(figsize=figsize)
    for key in points_dict:
        plt.plot(points_dict[key][:, 0], points_dict[key][:, 1])
    plt.show()


if __name__ == '__main__':
    main()



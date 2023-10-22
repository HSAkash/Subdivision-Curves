# Quadratic Bspline Curve Subdivision

import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Qt5Agg')


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


def draw(points_dict,num_iter, points, multi_line_thikness, single_line_thikness, single_line_color, axis_off):
    """
    Draws the points
    :param points_dict: dictionary of points
    :return: None
    """
    # plot the points
    figsize = getFigureSize(points)
    plt.figure(figsize=figsize)
    plt.rcParams['lines.linewidth'] = multi_line_thikness
    for key in points_dict:
        plt.plot(points_dict[key][:, 0], points_dict[key][:, 1])
    if axis_off:
        plt.axis('off')
    plt.show()


    plt.figure(figsize=figsize)
    plt.plot(
        points_dict[num_iter][:, 0],
        points_dict[num_iter][:, 1],
        linewidth=single_line_thikness,
        color=single_line_color
    )
    
    if axis_off:
        plt.axis('off')
    plt.show()




def isConnected(points):
    """
    Checks if the points are connected
    :param points: numpy array of points & shape (n, 2)
    :return: True if connected, False otherwise
    """
    return np.array_equal(points[0], points[-1])


def quadraticBsplineCurve(points, is_connect=False):
    """
    Applies four point algorithm to the given points
    :param points: numpy array of points & shape (n, 2)
    :param w: omega
    :param is_connect: boolean
    :return: list of points dtype(numpy array)
    """


    new_points = []
    # if points are not connected, add the first point to the new points
    if not is_connect:
        new_points.append(points[0])


    for i in range(len(points)):
        pi_minus_1 = points[i-1]
        pi_0 = points[i]
        pi_plus_1 = points[(i+1)%len(points)]

        q1 = (1/2)*pi_minus_1 + (1/2)*pi_0 
        q2 = (1/8)*pi_minus_1 + (6/8)*pi_0 + (1/8)*pi_plus_1

        new_points.append(q1)
        new_points.append(q2)


    # if points are connected, add the first point to the new points
    if is_connect:
        new_points.append(new_points[0])
    # if points are not connected, add the last point to the new points
    else:
        new_points.append(points[-1])

    return new_points





def main():
    """Input the number of iterations and the points"""
    # iteration input
    num_iter = int(input("Enter the number of iterations: "))
    # multiple points draw line thikness
    multi_line_thikness = int(input("Enter the line thikness (all): "))
    # single point draw line thikness
    single_line_thikness = int(input("Enter the line thikness (single): "))
    # single point draw line color
    single_line_color = input("Enter the line color (single): ")
    # axis off
    axis_off = input("Enter 'y' if you want to turn off the axis: ")
    axis_off = True if axis_off == 'y' else False

    # num_iter = 15
    # multi_line_thikness = 1
    # single_line_thikness = 1
    # single_line_color = 'red'
    # axis_off = True
    # is_connect = True
    # # initialize the points
    # main_points = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0,0]], dtype=np.float64)


    # initialize the points
    main_points = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0,0]], dtype=np.float64)

    is_connect = isConnected(main_points)

    # add the points to the dictionary 
    points = np.copy(main_points[:-1])

    points_dict = {}
    points_dict[0]=np.copy(main_points)

    # is_connect = isConnected(points)
    for i in range(1, num_iter+1):
        points = quadraticBsplineCurve(points, is_connect)
        points_dict[i]=np.copy(points)
        points = points[:-1] 
    # draw the points
    draw(points_dict, num_iter, main_points, multi_line_thikness, single_line_thikness, single_line_color, axis_off)


if __name__ == '__main__':
    main()



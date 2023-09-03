# corner cutting algorithm

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


def corner_cutting(points, num_iter, a, b, is_connect=False):
    """
    Applies corner cutting algorithm to the given points
    :param points: numpy array of points & shape (n, 2)
    :param num_iter: number of iterations
    :param a: floating point number
    :param b: floating point number
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
        p1 = points[i]
        p2 = points[i + 1]
        q1 = (1-a) * p1 + a * p2
        q2 = (1-b) * p1 + b * p2
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
    return corner_cutting(new_points, num_iter - 1, a, b, is_connect)


def draw(points_dict, points, multi_line_thikness, single_line_thikness, single_line_color, axis_off):
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
        points_dict[1][:, 0],
        points_dict[1][:, 1],
        linewidth=single_line_thikness,
        color=single_line_color
    )
    
    if axis_off:
        plt.axis('off')
    plt.show()



def main():
    """Input the number of iterations and the points"""
    # a input
    a = float(input("Enter a value usually 0.1 :"))
    # b input
    b = float(input("Enter a value usually 0.6 :"))
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



    # initialize the points
    # points = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], dtype=np.float64)
    points = np.array([[0, 0], [0, 1], [1, 1], [1, 0], [2, 0], [2, 1], [3, 1], [3, 0]], dtype=np.float64)
    # a and b are the parameters
    a = 0.1
    b = 0.6
    # add the points to the dictionary 
    points_dict[0] = points
    # call the function 
    points = corner_cutting(points, num_iter, a, b, isConnected(points))
    


    # draw the points
    draw(points_dict, points, multi_line_thikness, single_line_thikness, single_line_color, axis_off)


if __name__ == '__main__':
    main()



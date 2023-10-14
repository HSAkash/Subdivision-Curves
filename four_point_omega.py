# Four point algorithm

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

import matplotlib
matplotlib.use('Qt5Agg')


def draw(points_dict, points, multi_line_thikness, single_line_thikness, axis_off):
    """
    Draws the points
    :param points_dict: dictionary of points
    :return: None
    """
    # plot the points
    figsize = getFigureSize(points)
    plt.figure(figsize=figsize)
    plt.rcParams['lines.linewidth'] = multi_line_thikness
    for w in points_dict:
        for i, key in enumerate(points_dict[w]):
            if i == 0:
                continue
            plt.plot(key[:, 0], key[:, 1],
                    label=f"it = {i: 2d} w = {w}")
    if axis_off:
        plt.axis('off')
    
    # legend top left
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    # Adjust the layout to avoid cutting off labels
    plt.tight_layout()
    plt.show()


    plt.figure(figsize=figsize)
    for w in points_dict:
        plt.plot(
            points_dict[w][-1][:, 0],
            points_dict[w][-1][:, 1],
            linewidth=single_line_thikness,
            # color=single_line_color,
            label=f"it = {len(points_dict[w]) - 1: 2d} w = {w}"
        )
    
    if axis_off:
        plt.axis('off')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    # Adjust the layout to avoid cutting off labels
    plt.tight_layout()
    plt.show()



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
    return (fig_x+1, fig_y)
    

def isConnected(points):
    """
    Checks if the points are connected
    :param points: numpy array of points & shape (n, 2)
    :return: True if connected, False otherwise
    """
    return np.array_equal(points[0], points[-1])


def four_point_omega(points, w, is_connect=False):
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

    for i in range(len(points) - 1):
        pi_minus_1 = points[i-1]
        pi_0 = points[i]
        pi_plus_1 = points[i+1]
        pi_plus_2 = points[(i+2)%len(points)]

        q1 = pi_0
        # q2 = (1/16)*(-pi_minus_1 + 9*pi_0 + 9*pi_plus_1 - pi_plus_2)
        q2 = -w*pi_minus_1 + (.5+w)*pi_0 + (.5+w)*pi_plus_1 - w*pi_plus_2
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
    # omega input
    omega = list(map(float, input("Enter the omega: ").split()))
    # iteration input
    num_iter = int(input("Enter the number of iterations: "))
    # multiple points draw line thikness
    multi_line_thikness = int(input("Enter the line thikness (all): "))
    # single point draw line thikness
    single_line_thikness = int(input("Enter the line thikness (single): "))
    # axis off
    axis_off = input("Enter 'y' if you want to turn off the axis: ")
    axis_off = True if axis_off == 'y' else False



    # initialize the points
    # points = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], dtype=np.float64)
    main_points = np.array([[0, 0], [0, 1], [1, 1], [1, 0], [2, 0], [2, 1], [3, 1], [3, 0], [4, 0],[4,1], [5, 1]], dtype=np.float64)
    # add the points to the dictionary 
    points_dict = defaultdict(list)
    for w in omega:
        points_dict[w].append(np.copy(main_points))
    # call the function 
    for i in range(1, num_iter+1):
        for w in omega:
            points = points_dict[w][i-1]
            w_i_points = four_point_omega(points, w, isConnected(points))
            points_dict[w].append(np.copy(w_i_points))    

    # draw the points
    draw(points_dict, main_points, multi_line_thikness, single_line_thikness, axis_off)


if __name__ == '__main__':
    main()



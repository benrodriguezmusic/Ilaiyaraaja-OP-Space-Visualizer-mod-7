import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pointy as pointy

cube_points = pointy.the_point_of_it_all(pointy.non_repeating_forms)
the_cube_plot = plt.axes(projection='3d')
the_cube_plot.set_title("BIG OPTIC")
the_cube_plot.set_xlabel('X values')
the_cube_plot.set_ylabel('Y values')
the_cube_plot.set_zlabel('Z values')


def plot_it(form_list):
    for points in form_list:
        X, Y, Z = zip(*points)
        the_cube_plot.scatter(X, Y, Z, s=10)


def plot_transparent(form_list):
    for points in form_list:
        X, Y, Z = zip(*points)
        the_cube_plot.scatter(X, Y, Z, s=10, alpha=.4)


# plot_it(cube_points)

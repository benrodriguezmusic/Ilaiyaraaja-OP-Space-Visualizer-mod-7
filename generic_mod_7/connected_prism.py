import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import the_cube as cube
import pointy as pointy
import extended_cube as xtcube
import the_basic_prism as prism
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# prism_figure = plt.axes(projection='3d')
# prism_figure.set_xlim(1, 9)
# prism_figure.set_ylim(-1, 7)
# prism_figure.set_zlim(3, 11)

free_points = prism.prism_filter(xtcube.extend_cube(pointy.the_point_of_it_all(pointy.all_opt_forms)))
connect_points = prism.prism_filter(xtcube.extend_cube(pointy.the_point_of_it_all(pointy.non_repeating_forms)))
only_rojavai = prism.prism_filter(xtcube.extend_cube(pointy.the_point_of_it_all(pointy.rojavai_forms)))


def plot_neighbors(form_list):
    connect_pool = []

    for form in form_list:
        for point in form:
            connect_pool.append(point)

    for point in connect_pool:
        # transpose by one step in a direction
        # if in transposed point in connect_pool, make a pair with point
        for transposer in [1, -1]:
            for i in range(0, 3):
                candidate_neighbor = point.copy()
                candidate_neighbor[i] = point[i] + transposer
                if candidate_neighbor in connect_pool:
                    neighbor_pair = [point, candidate_neighbor]
                    X, Y, Z = zip(*neighbor_pair)
                    cube.the_cube_plot.plot(X, Y, Z, color='black', linewidth = .5)


def plot_prism_walls():
    # bottom triangle, sum class 12 (5 mod-7)
    A = (4, 4, 4)
    B = (19/3, -2/3, 19/3)
    C = (5/3, 5/3, 26/3)
    # top triangle
    D = (4, 4, 11)
    E = (19/3, 19/3, 19/3)
    F = (26/3, 5/3, 26/3)
    faces = [[A, B, C], [D, E, F], [A, B, F, E], [C, A, E, D]]
    walls = Poly3DCollection(faces, edgecolors='black', linewidths=.2, alpha=.2)
    cube.the_cube_plot.add_collection3d(walls)


plot_prism_walls()
cube.the_cube_plot.set_axis_off()
cube.the_cube_plot.set_xlim(1, 9)
cube.the_cube_plot.set_ylim(-1, 7)
cube.the_cube_plot.set_zlim(3, 11)

plot_neighbors(only_rojavai)
cube.plot_it(only_rojavai)
cube.plot_transparent(free_points)
plt.show()
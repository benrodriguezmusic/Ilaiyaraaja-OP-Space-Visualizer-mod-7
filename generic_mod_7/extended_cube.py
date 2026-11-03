import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import the_cube as cube
import pointy as pointy

old_cube_points = pointy.the_point_of_it_all(pointy.non_repeating_forms)


def extend_cube(old_cube):
    new_cube = []
    for form_list in old_cube:
        new_form_list = []
        for point in form_list:
            for h in range(0, 2):
                new_x = (point[0] + (h * 7))
                for i in range(0, 2):
                    new_y = (point[1] + (i * 7))
                    for j in range(0, 2):
                        new_z = (point[2] + (j * 7))
                        new_point = [new_x, new_y, new_z]
                        new_form_list.append(new_point)
        new_cube.append(new_form_list)
    new_refined_cube = []
    for form_list in new_cube:
        new_refined_form_list = []
        for point in form_list:
            if point not in new_refined_cube:
                new_refined_form_list.append(point)
        new_refined_cube.append(new_refined_form_list)
    return new_refined_cube


# print(extend_cube(old_cube_points))
# cube.plot_it(extend_cube(old_cube_points))

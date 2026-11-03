import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import the_cube as cube
import pointy as pointy
import extended_cube as xtcube


extended_forms_list = xtcube.extend_cube(pointy.the_point_of_it_all(pointy.all_opt_forms))


def prism_filter(form_list):
    filtered = []
    for point_list in form_list:
        trimmed_prism = []
        prism_untrimmed = []
        for point in point_list:
            # if #x>z, x>y, y+7>z
            if (point[0] >= point[1]) and (point[1] >= point[2] - 7) and (point[2] >= point[0]):
                prism_untrimmed.append(point)
        for point in prism_untrimmed:
            if point[0] + point[1] + point[2] >= 12 and (point[0] + point[1] + point[2] <= 19):
                trimmed_prism.append(point)
        if trimmed_prism:
            filtered.append(trimmed_prism)
    return filtered


# cube.the_cube_plot.set_xlim(1, 9)
# cube.the_cube_plot.set_ylim(-1, 7)
# cube.the_cube_plot.set_zlim(3, 11)
# cube.plot_it(prism_filter(extended_forms_list))

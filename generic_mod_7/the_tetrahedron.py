import the_cube as cube
import pointy as pointy
import matplotlib as plt


# the_tetrahedron = plt.axes(projection='3d')
old_cube = pointy.the_point_of_it_all(pointy.all_opt_forms)


# taking a list of lists. inner lists contain all the points for a given form
def tetra_filter(form_list):
    filtered_forms = []
    for point_list in form_list:
        filtered_points = []
        for point in point_list:
            # if #x>y, y>z, y<z
            if (point[0] > point[1]) and (point[1] > point[2]) and (point[2] < point[0]):
                filtered_points.append(point)
        if filtered_points:
            filtered_forms.append(filtered_points)
    return filtered_forms


# cube.plot_it(tetra_filter(old_cube))

# print(tetra_filter(old_cube_points))

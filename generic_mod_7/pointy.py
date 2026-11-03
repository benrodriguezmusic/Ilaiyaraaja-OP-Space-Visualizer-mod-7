mod_space = 7
opt_000 = [0, 0, 0]
opt_001 = [0, 0, 1]
opt_002 = [0, 0, 2]
opt_003 = [0, 0, 3]
opt_011 = [0, 1, 1]
opt_012 = [0, 1, 2]
opt_013 = [0, 1, 3]
opt_014 = [0, 1, 4]
opt_022 = [0, 2, 2]
opt_023 = [0, 2, 3]
opt_024 = [0, 2, 4]
opt_033 = [0, 3, 3]

repeating_forms = [opt_000, opt_001, opt_002, opt_003, opt_011, opt_022, opt_033]
all_opt_forms = [opt_000, opt_001, opt_002, opt_003, opt_011, opt_012, opt_013, opt_014, opt_022, opt_023, opt_024, opt_033]
non_repeating_forms = [opt_012, opt_013, opt_014, opt_023, opt_024]
rojavai_forms = [opt_024, opt_014]
victors_forms =  [opt_014, opt_023, opt_013]


def permute(opt_form):
    all = []

    for i in range(0, 3):
        x, y, z = opt_form[i], opt_form[(i + 1) % 3], opt_form[(i + 2) % 3]
        all.append([x, y, z])
    for i in range(0, 3):
        x, y, z = opt_form[i], opt_form[(i - 1) % 3], opt_form[(i - 2) % 3]
        all.append([x, y, z])
    return all


def transpose(permuted_list):
    transposed = []

    for point in permuted_list:
        for i in range(0, 7):
            new_triad = []
            for pitch in point:
                new_pitch = (pitch + i) % mod_space
                new_triad.append(new_pitch)
            transposed.append(new_triad)
    #print(f'transposed: {transposed}')
    return transposed


def the_point_of_it_all(raw_form_list):
    all_the_points = []

    for norm_form in raw_form_list:
        current_list = transpose(permute(norm_form))
        all_the_points.append(current_list)
    return all_the_points



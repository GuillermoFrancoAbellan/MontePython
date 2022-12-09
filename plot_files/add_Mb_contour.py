# add 68% and 95% contours corresponding to
# a gaussian H0 prior/likelihood
# Values from 1903.07603

if (name == r'$M_B$') or (second_name == r'$M_B$'):

    center=19.24
    sigma=0.0374 
    contour_color = info.MP_color['DOrange']
    contour_alpha = 0.5

    # add vertical contours when M is on the x axis
    if second_name == r'$M_B$':
        x68 = [-center-sigma,-center+sigma]
        x95 = [-center-2.*sigma,-center+2.*sigma]
        y1 = info.extent[2]
        y2 = info.extent[3]
        ax2dsub.fill_between(x95,
                             y1,
                             y2,
                             facecolor=contour_color[0],
                             edgecolor=contour_color[1],
                             linewidth=1,
                             alpha=contour_alpha)
        ax2dsub.fill_between(x68,
                             y1,
                             y2,
                             color=contour_color[1],
                             alpha=contour_alpha)

    # add horizontal contours when M is on the y axis
    if name == r'$M_B$':
        y68_1 = -center-sigma
        y68_2 = -center+sigma
        y95_1 = -center-2.*sigma
        y95_2 = -center+2.*sigma
        xx = [info.extent[0],info.extent[1]]
        ax2dsub.fill_between(xx,
                             y95_1,
                             y95_2,
                             facecolor=contour_color[0],
                             edgecolor=contour_color[1],
                             linewidth=1,
                             alpha=contour_alpha)
        ax2dsub.fill_between(xx,
                             y68_1,
                             y68_2,
                             color=contour_color[1],
                             alpha=contour_alpha)

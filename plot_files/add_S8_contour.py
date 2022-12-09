# add 68% and 95% contours corresponding to
# a gaussian S8 prior/likelihood

#if (name == 'S8') or (second_name == 'S8') or (name == r'$S_8$') or (second_name == r'$S_8$'):
if (name == r'$S_8$') or (second_name == r'$S_8$'):

    # Corresponds to 2007.15633
#    centers=[0.759]
#    sigma_pls=[0.024]
#    sigma_mns=[0.021]

    centers=[0.766]
    sigma_pls=[0.020]
    sigma_mns=[0.014]
    contour_colors = [info.MP_color['Purple']]
    contour_alphas = [0.5]

    for i in range(len(centers)):
      center = centers[i]
      sigma_pl = sigma_pls[i]
      sigma_mn = sigma_mns[i]
      contour_color = contour_colors[i]
      contour_alpha = contour_alphas[i]
      # add vertical contours when S8 is on the x axis
      if second_name == 'S8' or second_name == r'$S_8$':
          x68 = [center-sigma_mn,center+sigma_pl]
          x95 = [center-2.*sigma_mn,center+2.*sigma_pl]
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

      # add horizontal contours when S8 is on the y axis
      if name == 'S8' or name == r'$S_8$':
          y68_1 = center-sigma_mn
          y68_2 = center+sigma_pl
          y95_1 = center-2.*sigma_mn
          y95_2 = center+2.*sigma_pl
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

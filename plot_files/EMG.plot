import matplotlib.pyplot as plt
import numpy as np

info.redefine={'sigma8':'sigma8*(Omega_m/0.3)**0.5'}
info.to_change={'Omega_m':r'$\Omega_m$','parameters_smg__2':r'$\xi\sigma_i^2$', 'sigma8':r'$S_8$','H0':r'$H_0$','indexg_V':r'$V_0$','thetai_scf':r'$\sigma_i$'}

info.plot_legend_1d = True
info.plot_legend_2d = True
#info.legendnames = [r'$\rm{PlTT650TEEE}+\rm{SPT3G}+\rm{Pantheon}+\rm{BAO}$', r'$+\rm{ACTDR4}$']
info.legendnames = [r'$\rm{PlTT650}+\rm{SPT3G}+\rm{PanPlus}+\rm{BAO}$',r'$+\rm{TEEE}$', r'$+\rm{ACTDR4}$',r'$+\rm{high}\ell\rm{TT}$']

info.legendsize=24
info.ticknumber = 3
info.ticksize = 12
info.decimal=3
info.fontsize = 20
info.line_width = 2

info.to_plot = [r'$\Omega_m$',r'$\xi\sigma_i^2$', r'$S_8$',r'$H_0$',r'$V_0$',r'$\sigma_i$']
info.bins=20

info.force_limits = {r'$S_8$':[0.72,0.88], r'$H_0$':[65,77]}
info.force_limits = {r'$H_0$':[65,77]}

info.custom2d = ['add_S8_contour.py','add_h_contour.py']

info.MP_color = {'Red':['#E69679','#CC071E'],'Green':['#B8D698', '#57AB27'],'Blue':['#8EBAE5','#00549F'],'Orange':['#FDD48F','#F6A800'], 'Purple':['#BCB5D7','#7A6FAC'],'LRed':['#f79286','#f04430'],'LBlue':['#bcf1f7','#8be5f0'],'DGreen':['#4fb54a','#147d0f'],'DOrange':['#f5aa64','#f58822'],'Grey':['#bdbbbb','#878787'],'Black':['#595959','#141414'],'Pink':['#ff94c4','#f571ac'],'Magenta':['#eda1c3','#d6699a']}
info.MP_color_cycle = [info.MP_color['Red'], info.MP_color['Green'],info.MP_color['Blue'], info.MP_color['Orange'],  info.MP_color['Purple'], info.MP_color['LRed'], info.MP_color['LBlue'], info.MP_color['Pink'], info.MP_color['Grey'],info.MP_color['DGreen'], info.MP_color['DOrange'], info.MP_color['Black']]
info.alphas = [1.0, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85]



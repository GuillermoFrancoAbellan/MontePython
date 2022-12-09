#import matplotlib.pyplot as plt
#import numpy as np
#import math

# --  Put here your re-definitions of the derived quantities, for example to get S8.
info.redefine = {'sigma8':'sigma8*np.sqrt(Omega_m/0.3)'}

# -- Put here your re-namings of the quantities for nicer display
# -- The second line is important to more beautifully display even the default parameters.
info.to_change = {'sigma8':r'$S_8$','H0':r'$H_0$','age':r'${\rm Age [Gyr]}$','log10_z_c':r'${\rm log}_{10}(z_c)$','f_axion_ac':r'$f_{\rm EDE}(z_c)$','scf_parameters__1':r'$\theta_i$'}

# -- Put here the quantities you want to plot, using the full (and beautified) names.
# -- See the examples above for how to make your names appear nice and in LaTeX font
# -- First plot :: Planck variations (up to +BAO)
info.to_plot = [r'$H_0$',r'$f_{\rm EDE}(z_c)$',r'${\rm log}_{10}(z_c)$',r'$\theta_i$', r'$S_8$',r'${\rm Age [Gyr]}$']
#info.legendnames = [r'$\textrm{SPT+}\tau$',r'$\textrm{SPT+ACT+}\tau$',r'$\textrm{SPT+ACT+Planck TT+}\tau$']

#info.custom2d = ['add_h_contour.py','add_Mb_contour.py','add_S8_contour.py']

# -- Options:
# -- Adjust colors to consistent (and nice) color scheme
#info.MP_color = {'Red':['#E69679','#CC071E'],'Blue':['#8EBAE5','#00549F'],'Green':['#B8D698', '#57AB27'],'Orange':['#FDD48F','#F6A800'], 'Purple':['#BCB5D7','#7A6FAC'], 'LRed':['#f79286','#f04430'],'LBlue':['#bcf1f7','#8be5f0'],'DGreen':['#4fb54a','#147d0f'], 'DOrange':['#f5aa64','#f58822'],'Grey':['#bdbbbb','#878787'],'Black':['#595959','#141414'],'Pink':['#ff94c4','#f571ac'],'Magenta':['#eda1c3','#d6699a']}
#info.MP_color_cycle = [info.MP_color['Red'], info.MP_color['Blue'], info.MP_color['Green'], info.MP_color['Orange'],  info.MP_color['Purple'], info.MP_color['LRed'], info.MP_color['LBlue'], info.MP_color['Pink'], info.MP_color['Grey'],info.MP_color['DGreen'],info.MP_color['DOrange'],info.MP_color['Black']]
# -- (Up to a maximum of 9 contours are possible)
#info.alphas = [1.0, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85]

# -- Important: We might want to force these limits to get more consistent and comparable plots.
# -- Important: This should not be done by just setting [low,high] as the parameter bounds
# -- This is because montepython does some extension of the ranges
# -- The formula to calculate the required limits for no rounding is 'parameter' : [ (0.9*low-0.1*high)/0.8 , (0.9*high-0.1*low)/0.8 ]
# -- Proposed limits: Omega_m - (0.25 to 0.35)
#                     H0      - (65 to 75)
#                     S8      - (0.7 to 0.85)
#                     Mb      - (-19.5 to -19.2)
#info.force_limits = {'Omega_m':[0.2375,0.3625], r'$H_0$':[65.75,85.25],r'$M_B$':[-19.5375,-19.1625],r'$\theta_i$':[0.1,3],r'${\rm Log}_{10}a_c$':[-4.4,-3],r'$f_{\rm NEDE}$':[0.01,0.3],r'$3w_{\rm NEDE}$':[1,3],r'${\rm Log}_{10}(m_{\rm NEDE})$':[1.3, 3.3],r'$\theta_i$':[0.1,3],r'${\rm Log}_{10}a_c$':[-4.4,-3],r'$f_{\rm EDE}(z_c)$':[0.01,0.4],r'${\rm log}_{10}(z_c)$':[3,4]}

# -- Tick sizes
info.ticknumber = 3
info.ticksize = 18
info.fontsize = 18
info.decimal = 3
info.legendsize=13

# -- The bins aren't fixed on purpose. One can still use "--bins Nbins" as a command line option
info.bins=13


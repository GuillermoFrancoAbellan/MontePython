# --  Put here your re-definitions of the derived quantities, for example to get S8.
info.redefine = {'sigma8':'sigma8*np.sqrt(Omega_m/0.3)'}

# -- Put here your re-namings of the quantities for nicer display
# -- The second line is important to more beautifully display even the default parameters.
#info.to_change = {'YHe': 'Omega_m','sigma8':r'$S_8$',
# 'M':r'$M_B$','H0':r'$H_0$','b_clump':r'$b$','b_clump':r'$b$' }

info.to_change = {'Omega_m': r'$\Omega_m$','sigma8':r'$S_8$','M':r'$M_B$',
                  'H0':r'$H_0$','parameters_smg__2':r'$\xi$','indexg_V':r'$V_0$', 'thetai_scf':r'$\sigma_i$'}

# -- Put here the quantities you want to plot, using the full (and beautified) names.
# -- See the examples above for how to make your names appear nice and in LaTeX font
# -- First plot :: Planck variations (up to +BAO)
info.to_plot = [r'$H_0$',r'$M_B$',r'$\Omega_m$',r'$S_8$',r'$\xi$', r'$V_0$',r'$\sigma_i$']
info.legendnames = [r'P18+BAO+Pantheon',r'+RSD+CC',r'+RSD+CC+Ly$\alpha$',r'+RSD+CC+Ly$\alpha$+$M_B$']
info.custom2d = ['add_h_contour.py','add_S8_contour.py','add_Mb_contour.py']

# -- Second plot :: SN + Mb
#info.to_plot = [r'$H_0$','Omega_m',r'$M_B$', <model-specific-parameters>]
#info.legendnames = [r'$\text{Planck TTTEEE+Lens+BAO+Pantheon}$',r'$\text{Planck TTTEEE+Lens+BAO+$H_0$}$',r'$\text{Planck TTTEEE+Lens+BAO+Pantheon+$M_B$}$']
#info.custom2d = ['add_h_contour.py','add_Mb_contour.py','add_S8_contour.py']

# -- Options:
# -- Adjust colors to consistent (and nice) color scheme
info.MP_color = {'Red':['#E69679','#CC071E'],'Blue':['#8EBAE5','#00549F'],'Green':['#B8D698', '#57AB27'],'Orange':['#FDD48F','#F6A800'], 'Purple':['#BCB5D7','#7A6FAC'],'LRed':['#f79286','#f04430'],'LBlue':['#bcf1f7','#8be5f0'],'DGreen':['#4fb54a','#147d0f'],'DOrange':['#f5aa64','#f58822'],'Grey':['#bdbbbb','#878787'],'Black':['#595959','#141414'],'Pink':['#ff94c4','#f571ac'],'Magenta':['#eda1c3','#d6699a']}
info.MP_color_cycle = [info.MP_color['Red'], info.MP_color['Blue'], info.MP_color['Green'], info.MP_color['Orange'],  info.MP_color['Purple'], info.MP_color['LRed'], info.MP_color['LBlue'], info.MP_color['Pink'], info.MP_color['Grey'],info.MP_color['DGreen'], info.MP_color['DOrange'], info.MP_color['Black']]
# -- (Up to a maximum of 9 contours are possible)
info.alphas = [1.0, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85]

# -- Important: We might want to force these limits to get more consistent and comparable plots.
# -- Important: This should not be done by just setting [low,high] as the parameter bounds
# -- This is because montepython does some extension of the ranges
# -- The formula to calculate the required limits for no rounding is 'parameter' : [ (0.9*low-0.1*high)/0.8 , (0.9*high-0.1*low)/0.8 ]
# -- Proposed limits: Omega_m - (0.25 to 0.35)
#                     H0      - (65 to 75)
#                     S8      - (0.7 to 0.85)
#                     Mb      - (-19.5 to -19.2)
#info.force_limits = {'Omega_m':[0.2375,0.3625], r'$H_0$':[63.75,76.25],r'$S_8$':[0.68125,0.86875],r'$M_B$':[-19.5375,-19.1625]}
info.force_limits = {r'$H_0$':[63.75,76.25],r'$S_8$':[0.68125,0.86875],r'$\xi$':[0.00375,0.66625],r'$V_0$':[0.9375,3.5625],r'$\sigma_i$':[0.0125,0.8875] }


# -- Tick sizes
info.ticknumber = 3
info.ticksize = 20
info.fontsize = 24
info.decimal = 3
info.legendsize = 20

# -- The bins aren't fixed on purpose. One can still use "--bins Nbins" as a command line option
#info.bins=20

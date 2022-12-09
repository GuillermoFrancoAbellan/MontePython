# --  Put here your re-definitions of the derived quantities, for example to get S8.
info.redefine = {'YHe': '1.-Omega_Lambda','sigma8':'sigma8*np.sqrt(Omega_m/0.3)'}

# -- Put here your re-namings of the quantities for nicer display
# -- The second line is important to more beautifully display even the default parameters.
info.to_change = {'YHe': 'Omega_m','sigma8':r'$S_8$',
 'M':r'$M_B$','H0':r'$H_0$','N_ur':r'$N_\mathrm{ur}$','Neff':r'$N_\mathrm{eff}$', '100*theta_s':r'$100~\theta_s$'}

# -- Put here the quantities you want to plot, using the full (and beautified) names.
# -- See the examples above for how to make your names appear nice and in LaTeX font
# -- First plot :: Planck variations (up to +BAO)
info.to_plot = [r'$H_0$','Omega_m',r'$S_8$', <model-specific-parameters>]
info.legendnames = [r'$\text{Planck TT}$',r'$\text{Planck TTTEEE}$',r'$\text{Planck TTTEEE+Lens}$',r'$\text{Planck TTTEEE+Lens+BAO}$']
info.custom2d = ['add_h_contour.py','add_S8_contour.py']

# -- Second plot :: SN + Mb
#info.to_plot = [r'$H_0$','Omega_m',r'$M_B$', <model-specific-parameters>]
#info.legendnames = [r'$\text{Planck TTTEEE+Lens+BAO+Pantheon}$',r'$\text{Planck TTTEEE+Lens+BAO+$H_0$}$',r'$\text{Planck TTTEEE+Lens+BAO+Pantheon+$M_B$}$']
#info.custom2d = ['add_h_contour.py','add_Mb_contour.py','add_S8_contour.py']

# -- Options:
# -- Adjust colors to consistent (and nice) color scheme
info.MP_color = {'Red':['#E69679','#CC071E'],'Blue':['#8EBAE5','#00549F'],'Green':['#B8D698', '#57AB27'],'Orange':['#FDD48F','#F6A800'], 'Purple':['#BCB5D7','#7A6FAC'], 'LGreen':['#33FF77','#2EE66B'],'DOrange':['#FF8333','#CC6A29'],'Cyan':['#33FFA5','#29CC85'], 'LBlue':['#33E6FF','#29B9CC']}
info.MP_color_cycle = [info.MP_color['Red'], info.MP_color['Blue'], info.MP_color['Green'], info.MP_color['Orange'],  info.MP_color['Purple'], info.MP_color['LGreen'], info.MP_color['DOrange'], info.MP_color['Cyan'], info.MP_color['LBlue']]
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

# -- Tick sizes
info.ticknumber = 3
info.ticksize = 14
info.fontsize = 17
info.decimal = 3
info.legendsize=20

# -- The bins aren't fixed on purpose. One can still use "--bins Nbins" as a command line option
#info.bins=20

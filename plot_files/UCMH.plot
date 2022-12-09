import matplotlib.pyplot as plt
import numpy as np

#info.redefine={'sigma8':'sigma8*(Omega_m/0.3)**0.5'}
info.to_change={'Log10_A_spike':r'${\rm Log}_{10}(A_0)$','Log10_k_spike':r'${\rm Log}_{10}(k_s/{\rm Mpc}^{-1})$'}
info.plot_legend_1d = True
info.plot_legend_2d = True
#info.legendnames = ['Planck18+Lens+BAO+SNIa: Delos']
#info.legendnames = ['w cut-off','wo cut-off']
info.legendnames = ['GG','Delos']


info.legendsize=18
info.ticknumber = 3
info.ticksize = 12
info.decimal= 3
info.fontsize = 16
info.line_width = 2

info.to_plot = [r'${\rm Log}_{10}(A_0)$',r'${\rm Log}_{10}(k_s/{\rm Mpc}^{-1})$']
info.bins=20

# -- Important: We might want to force these limits to get more consistent and comparable plots.
# -- Important: This should not be done by just setting [low,high] as the parameter bounds
# -- This is because montepython does some extension of the ranges
# -- The formula to calculate the required limits for no rounding is 'parameter' : [ (0.9*low-0.1*high)/0.8 , (0.9*high-0.1*low)/0.8 ]
info.force_limits = {r'${\rm Log}_{10}(A_0)$':[-7.75,-5.25], r'${\rm Log}_{10}(k_s/{\rm Mpc}^{-1})$':[0.375,6.625]}

#info.custom1d = []
#info.custom2d = ['add_S8_contour.py']



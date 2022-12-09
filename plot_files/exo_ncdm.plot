
import matplotlib.pyplot as plt
import numpy as np

#info.redefine={'sigma8':'sigma8*(Omega_m/0.3)**0.5'}
#info.to_change={'sigma8':r'$\sigma_8$', 'm_ncdm':r'$M_{\chi}/\rm{keV}$', 'omega_ncdm':r'$\omega_{\rm{cdm}}$'}
info.plot_legend_1d = True
info.plot_legend_2d = True
#info.legendnames = [r'$\rm{Planck}+\rm{Ly}-\alpha$']

info.legendsize=25
info.ticknumber = 3
info.ticksize = 12
info.decimal=3
info.fontsize = 20
info.line_width = 2

#info.to_plot = [r'$\sigma_8$',r'$M_{\chi}/\rm{keV}$',r'$\omega_{\rm{cdm}}$']
info.to_plot = ['sigma8','m_ncdm','omega_ncdm']

info.bins=20

#info.force_limits = {r'$S_8$':[0.69,0.85]}

#info.custom1d = []
#info.custom2d = ['add_S8_contour.py']



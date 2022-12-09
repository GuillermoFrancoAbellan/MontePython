
import matplotlib.pyplot as plt
import numpy as np

#info.redefine={'sigma8':'sigma8*(Omega_m/0.3)**0.5'}
info.redefine={'m_ncdm':'3.0*m_ncdm'}
info.to_change={'A_glob':r'$10^9 A_{\rm glob}$','alpha_iso':r'$10^3 \alpha_{\rm iso}$','n_s':r'$n_s$','n_cdi':r'$n_{\rm iso}$', 'beta_iso_low':r'$\beta_{\rm low}$','beta_iso_mid':r'$\beta_{\rm mid}$','m_ncdm':r'$M_{\rm tot}$'}
info.plot_legend_1d = True
info.plot_legend_2d = True
info.legendnames = [r'$\rm{Planck}-\rm{only}+\rm{M}_{\nu}$']

info.legendsize=25
info.ticknumber = 3
info.ticksize = 12
info.decimal=3
info.fontsize = 20
info.line_width = 2

info.to_plot = [r'$10^9 A_{\rm glob}$',r'$10^3 \alpha_{\rm iso}$',r'$n_s$',r'$n_{\rm iso}$',r'$\beta_{\rm low}$',r'$\beta_{\rm mid}$',r'$M_{\rm tot}$']
info.bins=20

#info.force_limits = {r'$S_8$':[0.7,0.85]}

#info.custom1d = []
#info.custom2d = ['add_S8_contour.py']



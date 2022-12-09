
import matplotlib.pyplot as plt
import numpy as np

#info.redefine={'sigma8':'sigma8*(Omega_m/0.3)**0.5'}
info.redefine={'m_ncdm':'3.0*m_ncdm'}
info.to_change={'P_{RR}^1':r'$10^9P_{\rm{RR}}^1$','P_{RR}^2':r'$10^9P_{\rm{RR}}^2$','alpha_k1':r'$\alpha_{k1}$','alpha_k2':r'$\alpha_{k2}$', 'beta_iso_low':r'$\beta_{\rm low}$','beta_iso_mid':r'$\beta_{\rm mid}$', 'm_ncdm':r'$M_{\rm tot}$'}

info.plot_legend_1d = True
info.plot_legend_2d = True
#info.legendnames = [r'$\rm{Planck}-\rm{only}+\rm{M}_{\nu}$']

info.legendsize=25
info.ticknumber = 3
info.ticksize = 12
info.decimal=3
info.fontsize = 20
info.line_width = 2

info.to_plot = [r'$10^9P_{\rm{RR}}^1$',r'$10^9P_{\rm{RR}}^2$',r'$\alpha_{k1}$',r'$\alpha_{k2}$',r'$\beta_{\rm low}$',r'$\beta_{\rm mid}$',r'$M_{\rm tot}$']
info.bins=20

#info.force_limits = {r'$S_8$':[0.7,0.85]}

info.custom1d = []
#info.custom2d = ['add_S8_contour.py']



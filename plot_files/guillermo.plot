import matplotlib.pyplot as plt
import numpy as np

info.redefine={'sigma8':'sigma8*(Omega_m/0.3)**0.5'}
#info.redefine={'Log10_Gamma_dcdm':'2.991-Log10_Gamma_dcdm'}
info.to_change={'Omega_m':r'$\Omega_{\rm m}$','sigma8':r'$S_8$','H0':r'$H_0$','log10_epsilon_dcdm':r'${\rm Log}_{10}(\varepsilon)$','Log10_Gamma_dcdm':r'${\rm Log}_{10}(\Gamma / {\rm km} {\rm s}^{-1} {\rm Mpc}^{-1} )$'}
info.plot_legend_1d = True
info.plot_legend_2d = True
#info.legendnames = [r'$\rm{Planck}+\rm{BAO}/f\sigma_8+\rm{SNIa}+S_8\rm{KiDS-1000}$',r'$\rm{Planck}+\rm{BAO}/f\sigma_8+\rm{SNIa}+S_8\rm{KiDS-BOSS-2dFLens}$']
info.legendnames = [r'$\rm{Planck}+\rm{BAO}/f\sigma_8+\rm{SNIa}+S_8\rm{KiDS-1000}$']
#info.legendnames = ['BAO+Pantheon+SH0ES']

info.legendsize=25
info.ticknumber = 3
info.ticksize = 12
info.decimal=3
info.fontsize = 20
info.line_width = 2

info.to_plot = [r'$S_8$',r'$\Omega_{\rm m}$',r'$H_0$',r'${\rm Log}_{10}(\varepsilon)$',r'${\rm Log}_{10}(\Gamma / {\rm km} {\rm s}^{-1} {\rm Mpc}^{-1} )$']
#info.to_plot = [r'$H_0$', r'$\Omega^{\rm ini}_{\rm dcdm}$',r'$\varepsilon$',r'$\tau$',r'$r_s(z_{\rm rec})$']
info.bins=15

#info.force_limits = {r'$\Omega^{\rm ini}_{\rm dcdm}$':[0.15,0.43],r'$\Omega_{\rm cdm}$':[0.15,0.43],r'$H_0$':[66,81],r'$r_s(z_{\rm rec})$':[120,152]}
info.force_limits = {r'$S_8$':[0.69,0.85], r'$\Omega_{\rm m}$':[0.24,0.35]}

#info.custom1d = []
info.custom2d = ['add_S8_contour.py']



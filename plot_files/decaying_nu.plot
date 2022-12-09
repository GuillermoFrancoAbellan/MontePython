import matplotlib.pyplot as plt
import numpy as np

info.redefine={'m_ncdm':'3.0*m_ncdm'}
info.to_change={'m_ncdm':r'$\sum m_{\nu}/ {\rm eV}$','Log10_Gamma_neutrinos':r'${\rm Log}_{10}(\Gamma_{\nu} / {\rm km} {\rm s}^{-1} {\rm Mpc}^{-1} )$'}
info.plot_legend_1d = True
info.plot_legend_2d = True
info.legendnames = [r'$\rm{BAO}+\rm{Pantheon}+\rm{Planck18}$']

info.legendsize=12
info.ticknumber = 3
info.ticksize = 12
info.decimal=3
info.fontsize = 15
info.line_width = 2

info.to_plot = [r'$\sum m_{\nu}/ {\rm eV}$',r'${\rm Log}_{10}(\Gamma_{\nu} / {\rm km} {\rm s}^{-1} {\rm Mpc}^{-1} )$']
info.bins=20

#info.force_limits = {r'${\rm Log}_{10}(\Gamma_{\nu} / {\rm km} {\rm s}^{-1} {\rm Mpc}^{-1} )$':[0.05,5.55]}




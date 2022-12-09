import matplotlib.pyplot as plt
import numpy as np

info.redefine={'sigma8':'sigma8*(Omega_m/0.3)**0.5'}
info.redefine={'log10_epsilon_dcdm':'10**(Log10_Gamma_dcdm)*1.02*10**(-3)*np.sqrt(1.0-2.0*10**(log10_epsilon_dcdm))'}
#info.redefine={'m_dcdm':'0.5*(1.0-m_dcdm*m_dcdm)'}
#info.redefine={'Log10_Gamma_dcdm':'2.991-Log10_Gamma_dcdm'}
#info.redefine={'Log10_Gamma_dcdm':'3.0-Log10_Gamma_dcdm'}
info.to_change={'sigma8':r'$S_8$','H0':r'$H_0$','log10_epsilon_dcdm':r'$(\Gamma / {\rm Gyrs}^{-1})\sqrt(1-2\varepsilon)$'}
#info.redefine={'Gamma_dcdm2':'980.3921/Gamma_dcdm2'}
#info.to_change={'Gamma_dcdm2':r'$\tau$','H0':r'$H_0$','rs_rec': r'$r_s(z_{\rm rec})$','Omega_ini_dcdm2':r'$\Omega^{\rm ini}_{\rm dcdm}$','varepsilon':r'$\varepsilon$'}
info.plot_legend_1d = True
info.plot_legend_2d = True
#info.legendnames = [r'$\rm{BAO}+SNIa$',r'$+\rm{Planck}$',r'$+H_0$']
info.legendnames = [r'$\rm{BAOLy}\alpha+\rm{Pantheon}+\rm{Planck}$']
#info.legendnames = ['BAO+Pantheon+SH0ES']
#info.legendnames = ['without Planck prior','with Planck prior']
#info.legendnames = ['class DCDM2','class MAJORON']

info.legendsize=25
info.ticknumber = 3
info.ticksize = 12
info.decimal=3
info.fontsize = 20
info.line_width = 2

info.to_plot = [r'$S_8$',r'$H_0$',r'$(\Gamma / {\rm Gyrs}^{-1})\sqrt(1-2\varepsilon)$']
#info.to_plot = [r'$H_0$', r'$\Omega^{\rm ini}_{\rm dcdm}$',r'$\varepsilon$',r'$\tau$',r'$r_s(z_{\rm rec})$']
info.bins=20

#info.force_limits = {r'$\Omega^{\rm ini}_{\rm dcdm}$':[0.15,0.43],r'$\Omega_{\rm cdm}$':[0.15,0.43],r'$H_0$':[66,81],r'$r_s(z_{\rm rec})$':[120,152]}
info.force_limits= {r'$(\Gamma / {\rm Gyrs}^{-1})\sqrt(1-2\varepsilon)$':[0.0001, 0.3]}
#info.custom1d = []
info.custom2d = ['add_S8_contour.py']


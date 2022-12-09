import matplotlib.pyplot as plt
import numpy as np

info.redefine={'sigma8':'sigma8*(Omega_m/0.3)**0.5'}
info.redefine={'f_idm_wzdr':'100*f_idm_wzdr'}
#info.redefine={'Omega_Lambda':'(1.-Omega_Lambda)'}
#info.to_change={'Omega_m':r'$\Omega_m$', 'sigma8':r'$S_8$','H0':r'$H_0$','Gamma_0_wzdr':r'$\Gamma_0 ({\rm Mpc}^{-1})$','N_wzdr':r'$\Delta N_{\rm eff,IR}$','log10_zt_wzdr':r'${\rm log}_{10}(z_t)$'}
#info.to_change={'Omega_m':r'$\Omega_m$', 'sigma8':r'$S_8$','H0':r'$H_0$','N_wzdr':r'$\Delta N_{\rm eff,IR}$','log10_zt_wzdr':r'${\rm log}_{10}(z_t)$'}
info.to_change={'sigma8':r'$S_8$','Omega_m':r'$\Omega_m$','H0':r'$H_0$','N_wzdr':r'$\Delta N_{\rm eff,IR}$','log10_zt_wzdr':r'${\rm log}_{10}(z_t)$','f_idm_wzdr':r'$f_{\rm idm} [\%]$'}
#info.to_change={'sigma8':r'$S_8$','Omega_Lambda':r'$\Omega_m$','H0':r'$H_0$','n_s':r'$n_s$','rs_d':r'$r_s(z_{\rm drag})$', 'N_wzdr':r'$\Delta N_{\rm eff,IR}$','log10_zt_wzdr':r'${\rm log}_{10}(z_t)$'}


info.plot_legend_1d = True
info.plot_legend_2d = True
#info.legendnames = [r'$\rm{BAO}+\rm{Pantheon}+\rm{Planck18}: \rm{WZDR}$',r'$\rm{BAO}+\rm{Pantheon}+\rm{Planck18}: \rm{WZDR+IDM(n=0)}$']
#info.legendnames = [r'$\rm{BAO}+\rm{Pantheon}+\rm{Planck18}$',r'$\rm{BAO}+\rm{Pantheon}+\rm{Planck18}+S_8$',r'$\rm{BAO}+\rm{Pantheon}+\rm{Planck18}+H_0+S_8$']
info.legendnames = [r'$\rm{Planck18}+\rm{BAO}+\rm{Pantheon}+S_8+M_b$']
#info.legendnames = [r'SPT-3G + SPTLens + ACT-DR4 + Planck18 [lowTT+lowEE+high$\ell$TTTEEE($\ell<1050$)+high$\ell$EE]']
#info.legendnames = [r'WZDR: SPT-3G + SPTLens + Pl18[lowTT+lowEE+high$\ell$TT($\ell<1050$)]',r'WZDR: SPT-3G + SPTLens + Pl18[lowTT+lowEE+high$\ell$TTTEEE($\ell<1050$)]',r'WZDR: SPT-3G + SPTLens + ACT-DR4 + Pl18[lowTT+lowEE+high$\ell$TTTEEE($\ell<1050$)+high$\ell$EE]']

info.legendsize=22
info.ticknumber = 3
info.ticksize = 12
info.decimal=3
info.fontsize = 20
info.line_width = 2

info.to_plot = [r'$\Omega_m$', r'$S_8$',r'$H_0$',r'$\Delta N_{\rm eff,IR}$',r'${\rm log}_{10}(z_t)$',r'$f_{\rm idm} [\%]$']
#info.to_plot = [r'$S_8$',r'$\Omega_m$',r'$H_0$',r'$n_s$',r'$r_s(z_{\rm drag})$',r'$\Delta N_{\rm eff,IR}$',r'${\rm log}_{10}(z_t)$']
info.bins=20

info.force_limits = {r'$S_8$':[0.72,0.88], r'$H_0$':[65,77]}

info.custom2d = ['add_S8_contour.py','add_h_contour.py']
#info.custom2d = ['add_h_contour.py']




from __future__ import print_function
import sys, os
sys.path.insert(0,os.path.realpath(os.path.join(os.getcwd(),'..')))
from getdist import plots, mcsamples,chains
import pylab as plt
plt.rcParams['text.usetex']=True
import glob 
from getdist import loadMCSamples
from getdist import MCSamples

settings = {'ignore_rows' : 0.3}

print("~~~~~~~~~~~~importing chains ~~~~~~~~~~~~~")

s_pl18_old  = loadMCSamples('/home/fabellan/montepython_public/chains/decay_nu_full_Pl18_bao_sn_CUT_HIGH_newDR/2021-06-02_1000000_', settings = settings)
s_pl18_new  = loadMCSamples('/home/fabellan/montepython_public/chains/decay_nu_full_Pl18_bao_sn_CUT_HIGH_newDR_l3/2021-07-20_1000000_', settings = settings)

print("~~~~~~~~~~~~importing paramnames~~~~~~~~~~~~~")
##useful sometimes; the paramnames is a file that contains all the parameter names and latex labels. (see inside the folder)
#s_pl18_w_shearDR.setParamNames('/home/fabellan/montepython_public/chains/decay_nu_full_Pl18_bao_sn_CUT_HIGH_newDR/2021-06-02_1000000_.paramnames') 
#s_pl18_wo_shearDR.setParamNames('/home/fabellan/montepython_public/chains/decay_nu_fluid_Pl18_bao_sn_CUT_HIGH/2021-05-18_1000000_.paramnames') 


##add derived parameters
s_pl18_old.addDerived(s_pl18_old.getParams().Log10_Gamma_neutrinos,'Log10_Gamma',label=r'${\rm Log}_{10}(\Gamma_{\nu} / {\rm km} {\rm s}^{-1} {\rm Mpc}^{-1} )$')
s_pl18_new.addDerived(s_pl18_new.getParams().Log10_Gamma_neutrinos,'Log10_Gamma',label=r'${\rm Log}_{10}(\Gamma_{\nu} / {\rm km} {\rm s}^{-1} {\rm Mpc}^{-1} )$')

s_pl18_old.addDerived(s_pl18_old.getParams().m_ncdm*3.0,'M_nu',label=r'$\sum m_{\nu}/ {\rm eV}$')
s_pl18_new.addDerived(s_pl18_new.getParams().m_ncdm*3.0,'M_nu',label=r'$\sum m_{\nu}/ {\rm eV}$')

print("~~~set Ranges~~~~~~~~~~~~~")

s_pl18_old.setRanges({'Log10_Gamma':(3,5.5)})
s_pl18_new.setRanges({'Log10_Gamma':(3,5.5)})
s_pl18_old.setRanges({'M_nu':(0.06,1.2)})
s_pl18_new.setRanges({'M_nu':(0.06,1.2)})

###create figure
rec = plots.getSubplotPlotter() # set this to an instance of the subplotter 
g = plots.get_single_plotter(width_inch=4, ratio=1)

rec.settings.subplot_size_inch = 2
rec.settings.axes_fontsize = 15
rec.settings.lab_fontsize = 13
rec.settings.legend_fontsize = 16
rec.settings.figure_legend_frame = False 

print("~~~~~~~~~~~~setting params to output~~~~~~~~~~~~~")
params_to_plot = ['M_nu','Log10_Gamma']

print(' --------------------------------- Making triangle plot. --------------------------------- ')
rec.triangle_plot([s_pl18_old,s_pl18_new],params_to_plot,filled=[True,True],legend_labels = ['Pl18+BAO+SN, OLD','Pl18+BAO+SN, NEW'],contour_colors = ['green','blue'])


mNu     = [0.06,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7]
log_gam = [4.04, 4.38, 4.83, 5.09, 5.28, 5.42, 5.53, 5.64]

ax=rec.subplots[1,0]
ax.plot(mNu, log_gam, color = 'red')

rec.export('decaying_nu_old_vs_new.pdf')


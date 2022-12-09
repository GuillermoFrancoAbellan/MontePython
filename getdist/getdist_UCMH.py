from __future__ import print_function
import sys, os
sys.path.insert(0,os.path.realpath(os.path.join(os.getcwd(),'..')))
from getdist import plots, mcsamples,chains
import pylab as plt
plt.rcParams['text.usetex']=True
import glob 
from getdist import loadMCSamples
from getdist import MCSamples

settings_1 = {'ignore_rows' : 0.05}
settings = {'ignore_rows' : 0.3}

print("~~~~~~~~~~~~importing chains ~~~~~~~~~~~~~")

s_pl18  = loadMCSamples('/home/fabellan/montepython_public/chains/UCMH_m1Tev_bb_pl18_bao_sn_DELOS/2022-10-22_1000000_',settings = settings_1)
#s_pl18  = loadMCSamples('/home/fabellan/montepython_public/chains/UCMH_m1Tev_bb_pl18_bao_sn_GG_wkfs/2022-11-23_1000000_',settings = settings)
s_pl18_2  = loadMCSamples('/home/fabellan/montepython_public/chains/UCMH_m1Tev_bb_pl18_bao_sn_GG/2022-10-24_1000000_', settings = settings)

print("~~~~~~~~~~~~importing paramnames~~~~~~~~~~~~~")
##useful sometimes; the paramnames is a file that contains all the parameter names and latex labels. (see inside the folder)

##add derived parameters
s_pl18.addDerived(s_pl18.getParams().Log10_k_spike,'Log10_k',label=r'${\rm Log}_{10}(k_s/{\rm Mpc}^{-1})$')
s_pl18.addDerived(s_pl18.getParams().Log10_A_spike,'Log10_A',label=r'${\rm Log}_{10}(A_0)$')

s_pl18_2.addDerived(s_pl18_2.getParams().Log10_k_spike,'Log10_k',label=r'${\rm Log}_{10}(k_s/{\rm Mpc}^{-1})$')
s_pl18_2.addDerived(s_pl18_2.getParams().Log10_A_spike,'Log10_A',label=r'${\rm Log}_{10}(A_0)$')

print("~~~set Ranges~~~~~~~~~~~~~")

s_pl18.setRanges({'Log10_k':(0,7)})
s_pl18.setRanges({'Log10_A':(-8,-5)})

s_pl18_2.setRanges({'Log10_k':(0,7)})
s_pl18_2.setRanges({'Log10_A':(-8,-5)})

###create figure
rec = plots.getSubplotPlotter() # set this to an instance of the subplotter 
g = plots.get_single_plotter(width_inch=4, ratio=1)

rec.settings.subplot_size_inch = 2
rec.settings.axes_fontsize = 15
rec.settings.lab_fontsize = 13
rec.settings.legend_fontsize = 16
rec.settings.figure_legend_frame = False 

print("~~~~~~~~~~~~setting params to output~~~~~~~~~~~~~")
params_to_plot = ['Log10_k','Log10_A']

print(' --------------------------------- Making triangle plot. --------------------------------- ')
#rec.triangle_plot([s_pl18,s_pl18_2],params_to_plot,filled=[True,True],legend_labels = ['w cut-off','wo cut-off'],contour_colors = ['red','blue'])
rec.triangle_plot([s_pl18_2,s_pl18],params_to_plot,filled=[True,True],legend_labels = ['GG','Delos'],contour_colors = ['red','blue'])

rec.export('UCMH_constraints_Delos_vs_GG.pdf')
#rec.export('UCMH_constraints_w_vs_wo_kfs.pdf')


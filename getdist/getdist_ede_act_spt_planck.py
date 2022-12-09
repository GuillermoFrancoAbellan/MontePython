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

s_cmb             = loadMCSamples('/home/fabellan/montepython_public/chains/3param_SPT_ACT_PlanckTT650_TEEE_220105/2022-01-05_1000000_', settings = settings)
s_cmb_baosn       = loadMCSamples('/home/fabellan/montepython_public/chains/3param_SPT_ACT_PlanckTT650_TEEE_Ext_220106/2022-01-07_1000000_', settings = settings)
s_cmb_baosn_lens  = loadMCSamples('/home/fabellan/montepython_public/chains/3pEDE_SPT_ACT_PlTT650_TEEE_BAO_Pan_lens/2022-01-11_1000000_', settings = settings)

print("~~~~~~~~~~~~importing paramnames~~~~~~~~~~~~~")
##useful sometimes; the paramnames is a file that contains all the parameter names and latex labels. (see inside the folder)
s_cmb.setParamNames('/home/fabellan/montepython_public/chains/3param_SPT_ACT_PlanckTT650_TEEE_220105/2022-01-05_1000000_.paramnames') 
s_cmb_baosn.setParamNames('/home/fabellan/montepython_public/chains/3param_SPT_ACT_PlanckTT650_TEEE_Ext_220106/2022-01-07_1000000_.paramnames') 
s_cmb_baosn_lens.setParamNames('/home/fabellan/montepython_public/chains/3pEDE_SPT_ACT_PlTT650_TEEE_BAO_Pan_lens/2022-01-11_1000000_.paramnames') 


##add derived parameters
s_cmb.addDerived(s_cmb.getParams().f_axion_ac,'f_EDE',label=r'$f_{\rm EDE}(z_c)$')
s_cmb_baosn.addDerived(s_cmb_baosn.getParams().f_axion_ac,'f_EDE',label=r'$f_{\rm EDE}(z_c)$')
s_cmb_baosn_lens.addDerived(s_cmb_baosn_lens.getParams().f_axion_ac,'f_EDE',label=r'$f_{\rm EDE}(z_c)$')

#s_cmb.addDerived(s_cmb.getParams().H0,'H0',label=r'$H_0$')
#s_cmb_baosn.addDerived(s_cmb_baosn.getParams().H0,'H0',label=r'$H_0$')
#s_cmb_baosn_lens.addDerived(s_cmb_baosn_lens.getParams().H0,'H0',label=r'$H_0$')

print("~~~set Ranges~~~~~~~~~~~~~")

s_cmb.setRanges({'f_EDE':(0.0001,0.35)})
s_cmb_baosn.setRanges({'f_EDE':(0.0001,0.35)})
s_cmb_baosn_lens.setRanges({'f_EDE':(0.0001,0.35)})

###create figure
rec = plots.getSubplotPlotter() # set this to an instance of the subplotter 
g = plots.get_single_plotter(width_inch=4, ratio=1)

rec.settings.subplot_size_inch = 2
rec.settings.axes_fontsize = 15
rec.settings.lab_fontsize = 13
rec.settings.legend_fontsize = 10
rec.settings.figure_legend_frame = False 

print("~~~~~~~~~~~~setting params to output~~~~~~~~~~~~~")
params_to_plot = ['f_EDE','H0']

print(' --------------------------------- Making triangle plot. --------------------------------- ')
rec.triangle_plot([s_cmb,s_cmb_baosn,s_cmb_baosn_lens],params_to_plot,filled=[True,True,True],legend_labels = ['Planck TT650TEEE+ACT-DR4+SPT-3G','+BAOfs8+Pantheon', '+Planck lensing'],contour_colors = ['red','blue', 'green'])


plot_H0 = True
if plot_H0 == True:
        for i in range(len(params_to_plot)):
                index = params_to_plot.index('H0')
                if i < index:
                        rec.add_y_bands(73.04, 1.04, color='gray', ax=rec.subplots[index,i], alpha1=0.30, alpha2=0.2)
                if i > index:
                        rec.add_x_bands(73.04, 1.04, color='gray', ax=rec.subplots[i,index], alpha1=0.30, alpha2=0.2)

rec.export('ede_act_spt_plack.pdf')


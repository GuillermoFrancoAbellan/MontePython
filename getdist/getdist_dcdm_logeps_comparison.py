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

print("~~~~~~~~~~~~importing chains   ~~~~~~~~~~~~~")

s_low_logeps   =loadMCSamples('/home/fabellan/montepython_public/chains/dcdm_ALL_S8_lowlogeps/2021-11-26_1000000_', settings = settings)
s_high_logeps  =loadMCSamples('/home/fabellan/montepython_public/chains/chains_for_guillermo/wdm_SN_BAOLya_Planck_S8_log_eps_2010/2020-10-20_5000000_', settings = settings)

print("~~~~~~~~~~~~importing paramnames~~~~~~~~~~~~~")
##useful sometimes; the paramnames is a file that contains all the parameter names and latex labels. (see inside the folder).
s_low_logeps.setParamNames('/home/fabellan/montepython_public/chains/dcdm_ALL_S8_lowlogeps/2021-11-26_1000000_.paramnames') 
s_high_logeps.setParamNames('/home/fabellan/montepython_public/chains/chains_for_guillermo/wdm_SN_BAOLya_Planck_S8_log_eps_2010/2020-10-20_5000000_.paramnames') 

##add derived parameters
s_low_logeps.addDerived(s_low_logeps.getParams().sigma8*((s_low_logeps.getParams().Omega_m)/0.3)**(0.5),'S_8',label=r'$S_8$')
s_high_logeps.addDerived(s_high_logeps.getParams().sigma8*((s_high_logeps.getParams().Omega_m)/0.3)**(0.5),'S_8',label=r'$S_8$')

s_low_logeps.addDerived(s_low_logeps.getParams().Log10_Gamma_dcdm-2.991,'Log10_Gamma_gyrs',label=r'${\rm Log}_{10}(\Gamma / {\rm Gyrs}^{-1})$')
s_high_logeps.addDerived(s_high_logeps.getParams().Log10_Gamma_dcdm-2.991,'Log10_Gamma_gyrs',label=r'${\rm Log}_{10}(\Gamma / {\rm Gyrs}^{-1})$')

s_low_logeps.addDerived(s_low_logeps.getParams().log10_epsilon_dcdm,'log10_epsilon',label=r'${\rm Log}_{10}(\varepsilon)$')
s_high_logeps.addDerived(s_high_logeps.getParams().log10_epsilon_dcdm,'log10_epsilon',label=r'${\rm Log}_{10}(\varepsilon)$')

print("~~~set Ranges~~~~~~~~~~~~~")

s_low_logeps.setRanges({'Omega_m':(0.28,0.34)})
s_high_logeps.setRanges({'Omega_m':(0.28,0.34)})

s_low_logeps.setRanges({'S_8':(0.71,0.89)})
s_high_logeps.setRanges({'S_8':(0.71,0.89)})

s_low_logeps.setRanges({'Log10_Gamma_gyrs':(-4,1)})
s_high_logeps.setRanges({'Log10_Gamma_gyrs':(-4,1)})

s_low_logeps.setRanges({'log10_epsilon':(-6,-0.3011)})
s_high_logeps.setRanges({'log10_epsilon':(-4,-0.3011)})

###create figure
rec = plots.getSubplotPlotter() # set this to an instance of the subplotter 
g = plots.get_single_plotter(width_inch=4, ratio=1)

rec.settings.subplot_size_inch = 2
rec.settings.axes_fontsize = 15

rec.settings.lab_fontsize = 13
rec.settings.legend_fontsize = 15
rec.settings.figure_legend_frame = False # remove legend frame 

# tri.settings.legend_frac_subplot_margin = 0.02 # another way to move legend around 
#rec.settings.figure_legend_loc = (0.33,0.85) # set legend location 
# tri.settings.tight_layout = True

print("~~~~~~~~~~~~setting params to output~~~~~~~~~~~~~")
params_to_plot = ['Log10_Gamma_gyrs','log10_epsilon','S_8','Omega_m']


print(' --------------------------------- Making triangle plot. --------------------------------- ')

rec.triangle_plot([s_low_logeps,s_high_logeps],params_to_plot,filled=[True,True],legend_labels = [r'Planck+BAO+SN+$S_8$: ${\rm Log}_{10}(\varepsilon_{\rm min})=-6$',r'Planck+BAO+SN+$S_8$: ${\rm Log}_{10}(\varepsilon_{\rm min})=-4$'],contour_colors = ['red','blue'])


plot_S_8 = True
if plot_S_8 == True:
        for i in range(len(params_to_plot)):
                index = params_to_plot.index('S_8')
                if i < index:
                        print('here' + str(index))
                        rec.add_y_bands(0.766, 0.014, color='green', ax=rec.subplots[index,i], alpha1=0.30, alpha2=0.2)
                if i > index:
                        rec.add_x_bands(0.766, 0.014, color='green', ax=rec.subplots[i,index], alpha1=0.30, alpha2=0.2)

rec.export('dcdm_low_vs_high_logeps.pdf')


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

s_low_lineps   =loadMCSamples('/home/fabellan/montepython_public/chains/dcdm_ALL_S8_lowlineps/2021-12-02_1000000_', settings = settings)
s_high_lineps  =loadMCSamples('/home/fabellan/montepython_public/chains/final_DCDM_SN+BAOLya+Planck+S8_lin_priors_cut/2021-06-17_1000000_', settings = settings)


print("~~~~~~~~~~~~importing paramnames~~~~~~~~~~~~~")
##useful sometimes; the paramnames is a file that contains all the parameter names and latex labels. (see inside the folder).
s_low_lineps.setParamNames('/home/fabellan/montepython_public/chains/dcdm_ALL_S8_lowlineps/2021-12-02_1000000_.paramnames') 
s_high_lineps.setParamNames('/home/fabellan/montepython_public/chains/final_DCDM_SN+BAOLya+Planck+S8_lin_priors_cut/2021-06-17_1000000_.paramnames') 

##add derived parameters
s_low_lineps.addDerived(s_low_lineps.getParams().sigma8*((s_low_lineps.getParams().Omega_m)/0.3)**(0.5),'S_8',label=r'$S_8$')
s_high_lineps.addDerived(s_high_lineps.getParams().sigma8*((s_high_lineps.getParams().Omega_m)/0.3)**(0.5),'S_8',label=r'$S_8$')

s_low_lineps.addDerived(s_low_lineps.getParams().Gamma_dcdm*(1.02e-3)  ,'Gamma_gyrs',label=r'$\Gamma / {\rm Gyrs}^{-1}$')
s_high_lineps.addDerived(s_high_lineps.getParams().Gamma_dcdm*(1.02e-3),'Gamma_gyrs',label=r'$\Gamma / {\rm Gyrs}^{-1}$')

s_low_lineps.addDerived(s_low_lineps.getParams().epsilon_dcdm          ,'epsilon',label=r'$\varepsilon$')
s_high_lineps.addDerived(s_high_lineps.getParams().epsilon_dcdm/10000.0,'epsilon',label=r'$\varepsilon$')

print("~~~set Ranges~~~~~~~~~~~~~")

s_low_lineps.setRanges({'Omega_m':(0.28,0.34)})
s_high_lineps.setRanges({'Omega_m':(0.28,0.34)})

s_low_lineps.setRanges({'S_8':(0.71,0.89)})
s_high_lineps.setRanges({'S_8':(0.71,0.89)})

s_low_lineps.setRanges({'Gamma_gyrs':(1.02e-4,0.051)})
s_high_lineps.setRanges({'Gamma_gyrs':(1.02e-4,0.051)})

s_low_lineps.setRanges({'epsilon':(0.000001,0.015)})
s_high_lineps.setRanges({'epsilon':(0.0001,0.015)})

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
params_to_plot = ['Gamma_gyrs','epsilon','S_8','Omega_m']


print(' --------------------------------- Making triangle plot. --------------------------------- ')

rec.triangle_plot([s_low_lineps,s_high_lineps],params_to_plot,filled=[True,True],legend_labels = [r'Planck+BAO+SN+$S_8$: $\varepsilon_{\rm min}=10^{-6}$',r'Planck+BAO+SN+$S_8$: $\varepsilon_{\rm min}=10^{-4}$'],contour_colors = ['red','blue'])


plot_S_8 = True
if plot_S_8 == True:
        for i in range(len(params_to_plot)):
                index = params_to_plot.index('S_8')
                if i < index:
                        print('here' + str(index))
                        rec.add_y_bands(0.766, 0.014, color='green', ax=rec.subplots[index,i], alpha1=0.30, alpha2=0.2)
                if i > index:
                        rec.add_x_bands(0.766, 0.014, color='green', ax=rec.subplots[i,index], alpha1=0.30, alpha2=0.2)

rec.export('dcdm_low_vs_high_lineps.pdf')


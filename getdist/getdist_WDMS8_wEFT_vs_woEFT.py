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

#s_woEFT = loadMCSamples('/home/fabellan/montepython_public/Theos_runs/WDM/woEFT_wS8/2020-10-20_5000000_', settings = settings)
s_woEFT = loadMCSamples('/home/fabellan/montepython_public/chains/WDM_pl18_pan_baofs8_S8KIDS-1000/2022-02-25_1000000_', settings = settings)
s_wEFT  = loadMCSamples('/home/fabellan/montepython_public/Theos_runs/WDM/wEFT_wS8/2022-01-05_1000000_', settings = settings)


print("~~~~~~~~~~~~importing paramnames~~~~~~~~~~~~~")
##useful sometimes; the paramnames is a file that contains all the parameter names and latex labels. (see inside the folder).
#s_woEFT.setParamNames('/home/fabellan/montepython_public/Theos_runs/WDM/woEFT_wS8/2020-10-20_5000000_.paramnames') 
s_woEFT.setParamNames('/home/fabellan/montepython_public/chains/WDM_pl18_pan_baofs8_S8KIDS-1000/2022-02-25_1000000_.paramnames') 
s_wEFT.setParamNames('/home/fabellan/montepython_public/Theos_runs/WDM/wEFT_wS8/2022-01-05_1000000_.paramnames') 

##add derived parameters
s_woEFT.addDerived(s_woEFT.getParams().sigma8*((s_woEFT.getParams().Omega_m)/0.3)**(0.5),'S_8',label=r'$S_8$')
s_wEFT.addDerived(s_wEFT.getParams().sigma8*((s_wEFT.getParams().Omega_m)/0.3)**(0.5),'S_8',label=r'$S_8$')

s_woEFT.addDerived(s_woEFT.getParams().Log10_Gamma_dcdm-2.991,'log_Gamma_Gyr',label=r'$\rm{log}_{10}(\Gamma/\rm{Gyr}^{-1})$')
s_wEFT.addDerived(s_wEFT.getParams().Log10_Gamma_dcdm-2.991,'log_Gamma_Gyr',label=r'$\rm{log}_{10}(\Gamma/\rm{Gyr}^{-1})$')

print("~~~set Ranges~~~~~~~~~~~~~")

s_woEFT.setRanges({'Omega_m':(0.28,0.34)})
s_wEFT.setRanges({'Omega_m':(0.28,0.34)})

s_woEFT.setRanges({'S_8':(0.71,0.89)})
s_wEFT.setRanges({'S_8':(0.71,0.89)})

s_woEFT.setRanges({'H0':(64,73)})
s_wEFT.setRanges({'H0':(64,73)})

s_woEFT.setRanges({'log10_epsilon_dcdm':(-4.0,-0.3011)})
s_wEFT.setRanges({'log10_epsilon_dcdm':(-4.0,-0.3011)})

s_woEFT.setRanges({'log_Gamma_Gyr':(-4.0,1.0)})
s_wEFT.setRanges({'log_Gamma_Gyr':(-4.0,1.0)})

###create figure
rec = plots.getSubplotPlotter() # set this to an instance of the subplotter 
g = plots.get_single_plotter(width_inch=4, ratio=1)

rec.settings.subplot_size_inch = 2
rec.settings.axes_fontsize = 15

rec.settings.lab_fontsize = 18
rec.settings.legend_fontsize = 22
rec.settings.figure_legend_frame = False # remove legend frame 

# tri.settings.legend_frac_subplot_margin = 0.02 # another way to move legend around 
rec.settings.figure_legend_loc = (0.30,0.9) # set legend location 
# tri.settings.tight_layout = True

print("~~~~~~~~~~~~setting params to output~~~~~~~~~~~~~")
params_to_plot = ['log_Gamma_Gyr','log10_epsilon_dcdm','H0','S_8','Omega_m']


print(' --------------------------------- Making triangle plot. --------------------------------- ')

rec.triangle_plot([s_woEFT,s_wEFT],params_to_plot,filled=[True,True],legend_labels = [r'Planck + Pantheon + BOSS BAO/f$\sigma_8$ + Ext-BAO + $S_8$',r'Planck + Pantheon + EFTofBOSS + Ext-BAO + $S_8$' ],contour_colors = ['red','blue'])


plot_S_8 = True
if plot_S_8 == True:
        for i in range(len(params_to_plot)):
                index = params_to_plot.index('S_8')
                if i < index:
                        print('here' + str(index))
                        rec.add_y_bands(0.766, 0.02, color='gray', ax=rec.subplots[index,i], alpha1=0.30, alpha2=0.2)
                if i > index:
                        rec.add_x_bands(0.766, 0.02, color='gray', ax=rec.subplots[i,index], alpha1=0.30, alpha2=0.2)

rec.export('WDMS8_wEFT_vs_woEFT.pdf')



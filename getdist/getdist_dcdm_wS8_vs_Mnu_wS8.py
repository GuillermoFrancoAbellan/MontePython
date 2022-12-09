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

samp_DCDM_wS8 =loadMCSamples('/home/fabellan/montepython_public/chains/SN+BAOLya+Planck+S8_log_eps_gamma/2021-03-01_1000000_', settings = settings)
samp_NU_wS8 =loadMCSamples('/home/fabellan/montepython_public/chains/chains_for_guillermo/LCDM_MCMC_Mnu_S8KIDS1000_3107/2020-07-31_500000_', settings = settings)


print("~~~~~~~~~~~~importing paramnames~~~~~~~~~~~~~")
##useful sometimes; the paramnames is a file that contains all the parameter names and latex labels. (see inside the folder).
samp_DCDM_wS8.setParamNames('/home/fabellan/montepython_public/chains/SN+BAOLya+Planck+S8_log_eps_gamma/2021-03-01_1000000_.paramnames') 
samp_NU_wS8.setParamNames('/home/fabellan/montepython_public/chains/chains_for_guillermo/LCDM_MCMC_Mnu_S8KIDS1000_3107/2020-08-09_500000_.paramnames') 

##add derived parameters
samp_DCDM_wS8.addDerived(samp_DCDM_wS8.getParams().sigma8*((samp_DCDM_wS8.getParams().Omega_m)/0.3)**(0.5),'S_8',label=r'$S_8$')
samp_NU_wS8.addDerived(samp_NU_wS8.getParams().sigma8*((samp_NU_wS8.getParams().Omega_m)/0.3)**(0.5),'S_8',label=r'$S_8$')

#samp_DCDM_wS8.addDerived(samp_DCDM_wS8.getParams().Log10_Gamma_dcdm-2.991,'Log10_Gamma_gyrs',label=r'${\rm Log}_{10}(\Gamma / {\rm Gyrs}^{-1} )$')
samp_DCDM_wS8.addDerived(samp_DCDM_wS8.getParams().Log10_Gamma_epsilon_dcdm,'Log10_eps_Gamma_gyrs',label=r'${\rm Log}_{10}(\varepsilon \Gamma / {\rm Gyrs}^{-1} )$')

print("~~~set Ranges~~~~~~~~~~~~~")

samp_DCDM_wS8.setRanges({'Omega_m':(0.28,0.34)})
samp_NU_wS8.setRanges({'Omega_m':(0.28,0.34)})

samp_DCDM_wS8.setRanges({'S_8':(0.71,0.89)})
samp_NU_wS8.setRanges({'S_8':(0.71,0.89)})

samp_DCDM_wS8.setRanges({'log10_epsilon_dcdm':(-4,-0.301)})
#samp_DCDM_wS8.setRanges({'Log10_Gamma_gyrs':(-4,1)})
samp_DCDM_wS8.setRanges({'Log10_eps_Gamma_gyrs':(-7,-1)})

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
#params_to_plot = ['Log10_Gamma_gyrs','log10_epsilon_dcdm','S_8','Omega_m']
params_to_plot = ['Log10_eps_Gamma_gyrs','log10_epsilon_dcdm','S_8','Omega_m']


print(' --------------------------------- Making triangle plot. --------------------------------- ')

rec.triangle_plot([samp_DCDM_wS8,samp_NU_wS8],params_to_plot,filled=[True,True],legend_labels = [r'$\Lambda$DDM',r'$\nu\Lambda$CDM'],contour_colors = ['red','blue'])

#,markers={'f_axion_ac':8.481209e-02,'log10_zc':3.569486e+00,'scf_parameters__1':2.756,'H0':70.5})

plot_S_8 = True
if plot_S_8 == True:
        for i in range(len(params_to_plot)):
                index = params_to_plot.index('S_8')
                if i < index:
                        print('here' + str(index))
                        rec.add_y_bands(0.766, 0.014, color='green', ax=rec.subplots[index,i], alpha1=0.30, alpha2=0.2)
                if i > index:
                        rec.add_x_bands(0.766, 0.014, color='green', ax=rec.subplots[i,index], alpha1=0.30, alpha2=0.2)

rec.export('dcdm2_wS8_vs_Mnu_wS8.pdf')


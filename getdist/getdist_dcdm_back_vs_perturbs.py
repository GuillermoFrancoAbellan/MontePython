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

print("~~~~~~~~~~~~importing chain DCDM (no SH0ES)~~~~~~~~~~~~~")

samp_DCDM_back =loadMCSamples('/home/fabellan/montepython_public/dcdm_SN_BAOLya_log_eps_2/2020-07-19_1000000_', settings = settings)
samp_DCDM_perts =loadMCSamples('/home/fabellan/montepython_public/SN+BAOLya+Planck_log_eps/2020-07-17_2000000_', settings = settings)

print("~~~~~~~~~~~~importing chain DCDM (SHOES) ~~~~~~~~~~~~~")

samp_DCDM_pertsH0= loadMCSamples('/home/fabellan/montepython_public/SN+BAO+H0+Planck_log_eps/2020-07-14_2000000_', settings = settings)

print("~~~~~~~~~~~~importing paramnames~~~~~~~~~~~~~")
##useful sometimes; the paramnames is a file that contains all the parameter names and latex labels. (see inside the folder).
#samp_LCDM_Planck.setParamNames('/datadec/users/users/vpoulin/chains_montepython/AxiCLASS_2018/AxiCLASS_n3_mpi_KV_0306/2020-06-03_500000_.paramnames') 
samp_DCDM_back.setParamNames('/home/fabellan/montepython_public/dcdm_SN_BAOLya_log_eps_2/2020-07-19_1000000_.paramnames') 
samp_DCDM_perts.setParamNames('/home/fabellan/montepython_public/SN+BAOLya+Planck_log_eps/2020-07-17_2000000_.paramnames') 
samp_DCDM_pertsH0.setParamNames('/home/fabellan/montepython_public/SN+BAO+H0+Planck_log_eps/2020-07-14_2000000_.paramnames') 

##add derived parameters
samp_DCDM_perts.addDerived(samp_DCDM_perts.getParams().sigma8*((samp_DCDM_perts.getParams().Omega_m)/0.3)**(0.5),'S_8',label=r'$S_8$')
samp_DCDM_pertsH0.addDerived(samp_DCDM_pertsH0.getParams().sigma8*((samp_DCDM_pertsH0.getParams().Omega_m)/0.3)**(0.5),'S_8',label=r'$S_8$')
samp_DCDM_perts.addDerived(samp_DCDM_perts.getParams().Log10_Gamma_dcdm-2.991,'Log10_Gamma_gyrs',label=r'${\rm Log}_{10}(\Gamma / {\rm Gyrs}^{-1} )$')
samp_DCDM_pertsH0.addDerived(samp_DCDM_pertsH0.getParams().Log10_Gamma_dcdm-2.991,'Log10_Gamma_gyrs',label=r'${\rm Log}_{10}(\Gamma / {\rm Gyrs}^{-1} )$')
samp_DCDM_back.addDerived(samp_DCDM_back.getParams().Log10_Gamma_dcdm-2.991,'Log10_Gamma_gyrs',label=r'${\rm Log}_{10}(\Gamma / {\rm Gyrs}^{-1} )$')

print("~~~set Ranges~~~~~~~~~~~~~")
samp_DCDM_perts.setRanges({'H0':(64,73)})
samp_DCDM_pertsH0.setRanges({'H0':(64,73)})
samp_DCDM_back.setRanges({'H0':(64,73)})

samp_DCDM_perts.setRanges({'Omega_m':(0.24,0.35)})
samp_DCDM_pertsH0.setRanges({'Omega_m':(0.24,0.35)})
samp_DCDM_back.setRanges({'Omega_m':(0.24,0.35)})

samp_DCDM_perts.setRanges({'S_8':(0.7,0.87)})
samp_DCDM_pertsH0.setRanges({'S_8':(0.7,0.87)})

samp_DCDM_perts.setRanges({'log10_epsilon_dcdm':(-4,-0.301)})
samp_DCDM_pertsH0.setRanges({'log10_epsilon_dcdm':(-4,-0.301)})
samp_DCDM_back.setRanges({'log10_epsilon_dcdm':(-4,-0.301)})

samp_DCDM_perts.setRanges({'Log10_Gamma_gyrs':(-4,1)})
samp_DCDM_pertsH0.setRanges({'Log10_Gamma_gyrs':(-4,1)})
samp_DCDM_back.setRanges({'Log10_Gamma_gyrs':(-4,1)})
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
#params_to_plot = ['Log10_Gamma_dcdm','log10_epsilon_dcdm','H0','S_8','Omega_m']
params_to_plot = ['Log10_Gamma_gyrs','log10_epsilon_dcdm','H0','S_8','Omega_m']

print(' --------------------------------- Making triangle plot. --------------------------------- ')

rec.triangle_plot([samp_DCDM_perts,samp_DCDM_back],params_to_plot,filled=[True,False],legend_labels = ['BAO+SNIa+Planck','BAO+SNIa'],contour_colors = ['dodgerblue','darkorchid'])

#,markers={'f_axion_ac':8.481209e-02,'log10_zc':3.569486e+00,'scf_parameters__1':2.756,'H0':70.5})
plot_H0 = True
if plot_H0 == True:
	for i in range(len(params_to_plot)):
		index = params_to_plot.index('H0')
		if i < index:	
			print('here' + str(index))
			rec.add_y_bands(74.03, 1.42, color='grey', ax=rec.subplots[index,i], alpha1=0.30, alpha2=0.2, label = r'SH0ES')
		if i > index:
			rec.add_x_bands(74.03, 1.42, color='grey', ax=rec.subplots[i,index], alpha1=0.30, alpha2=0.2, label = r'SH0ES')

plot_S_8 = True
if plot_S_8 == True:
        for i in range(len(params_to_plot)):
                index = params_to_plot.index('S_8')
                if i < index:
                        print('here' + str(index))
                        rec.add_y_bands(0.755, 0.019, color='green', ax=rec.subplots[index,i], alpha1=0.30, alpha2=0.2, label = r'COSEBIs')
                if i > index:
                        rec.add_x_bands(0.755, 0.019, color='green', ax=rec.subplots[i,index], alpha1=0.30, alpha2=0.2, label = r'COSEBIs')

rec.export('dcdm_back_vs_perts.pdf')

###we produce a second plot 
#params_to_plot = ['Log10_Gamma_dcdm','log10_epsilon_dcdm','H0','S_8','Omega_m']
params_to_plot = ['Log10_Gamma_gyrs','log10_epsilon_dcdm','H0','S_8','Omega_m']

rec.triangle_plot(samp_DCDM_pertsH0,params_to_plot,filled=[True,True],legend_labels =['BAO+SNIA+Planck+SH0ES'],contour_colors = ['crimson'])


plot_H0 = True
if plot_H0 == True:
        for i in range(len(params_to_plot)):
                index = params_to_plot.index('H0')
                if i < index:
                        print('here' + str(index))
                        rec.add_y_bands(74.03, 1.42, color='grey', ax=rec.subplots[index,i], alpha1=0.30, alpha2=0.2, label = r'SH0ES')
                if i > index:
                        rec.add_x_bands(74.03, 1.42, color='grey', ax=rec.subplots[i,index], alpha1=0.30, alpha2=0.2, label = r'SH0ES')

plot_S_8 = True
if plot_S_8 == True:
        for i in range(len(params_to_plot)):
                index = params_to_plot.index('S_8')
                if i < index:
                        print('here' + str(index))
                        rec.add_y_bands(0.755, 0.019, color='green', ax=rec.subplots[index,i], alpha1=0.30, alpha2=0.2, label = r'COSEBIs')
                if i > index:
                        rec.add_x_bands(0.755, 0.019, color='green', ax=rec.subplots[i,index], alpha1=0.30, alpha2=0.2, label = r'COSEBIs')

rec.export('dcdm_perts_H0.pdf')

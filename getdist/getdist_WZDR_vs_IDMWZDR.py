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

s_WZDR = loadMCSamples('/home/fabellan/montepython_public/chains/WZDR_pl18_lens_bao_sn_2/2022-02-16_1000000_', settings = settings)
s_IDM  = loadMCSamples('/home/fabellan/montepython_public/chains/IDM_WZDR_pl18_lens_bao_sn_2/2022-02-16_1000000_', settings = settings)


print("~~~~~~~~~~~~importing paramnames~~~~~~~~~~~~~")
##useful sometimes; the paramnames is a file that contains all the parameter names and latex labels. (see inside the folder).
s_WZDR.setParamNames('/home/fabellan/montepython_public/chains/WZDR_pl18_lens_bao_sn_2/2022-02-16_1000000_.paramnames') 
s_IDM.setParamNames('/home/fabellan/montepython_public/chains/IDM_WZDR_pl18_lens_bao_sn_2/2022-02-16_1000000_.paramnames') 

##add derived parameters
s_WZDR.addDerived(s_WZDR.getParams().sigma8*((s_WZDR.getParams().Omega_m)/0.3)**(0.5),'S_8',label=r'$S_8$')
s_IDM.addDerived(s_IDM.getParams().sigma8*((s_IDM.getParams().Omega_m)/0.3)**(0.5),'S_8',label=r'$S_8$')

s_WZDR.addDerived(s_WZDR.getParams().H0/100,'h',label=r'$h$')
s_IDM.addDerived(s_IDM.getParams().H0/100,'h',label=r'$h$')

s_IDM.addDerived(s_IDM.getParams().Gamma_0_wzdr*1e8,'Gamma',label=r'$\Gamma_0 [\rm{Mpc}^{-1}] \times 10^8$')

print("~~~set Ranges~~~~~~~~~~~~~")

s_WZDR.setRanges({'Omega_m':(0.28,0.34)})
s_IDM.setRanges({'Omega_m':(0.28,0.34)})

s_WZDR.setRanges({'S_8':(0.69,0.89)})
s_IDM.setRanges({'S_8':(0.69,0.89)})

s_WZDR.setRanges({'h':(0.64,0.77)})
s_IDM.setRanges({'h':(0.64,0.77)})

s_WZDR.setRanges({'N_wzdr':(0,1)})
s_IDM.setRanges({'N_wzdr':(0,1)})

s_WZDR.setRanges({'log10_zt_wzdr':(4,4.6)})
s_IDM.setRanges({'log10_zt_wzdr':(4,4.6)})

s_IDM.setRanges({'Gamma':(0,10)})

###create figure
rec = plots.getSubplotPlotter() # set this to an instance of the subplotter 
g = plots.get_single_plotter(width_inch=4, ratio=1)

rec.settings.subplot_size_inch = 2
rec.settings.axes_fontsize = 17

rec.settings.lab_fontsize = 20
rec.settings.legend_fontsize = 28
rec.settings.figure_legend_frame = True # remove legend frame 

# tri.settings.legend_frac_subplot_margin = 0.02 # another way to move legend around 
rec.settings.figure_legend_loc = (0.5,0.9) # set legend location 
# tri.settings.tight_layout = True

print("~~~~~~~~~~~~setting params to output~~~~~~~~~~~~~")
params_to_plot = ['N_wzdr','log10_zt_wzdr','Gamma', 'h','S_8','Omega_m']


print(' --------------------------------- Making triangle plot. --------------------------------- ')

rec.triangle_plot([s_IDM,s_WZDR],params_to_plot,filled=[True,True],legend_labels = [r'IDM+WZDR',r'WZDR' ],contour_colors = ['green','red'],label_order=-1)

for ax in rec.fig.axes:
    geo = ax.get_geometry()
    if (geo[2]-1) // geo[0] > (geo[2]-1) % geo[0]:
       for c,z in zip(ax.collections, [19,20,21,17,18,21]):
           c.zorder =z


plot_H0 = True
if plot_H0 == True:
        for i in range(len(params_to_plot)):
                index = params_to_plot.index('h')
                if i < index:
                        print('here' + str(index))
                        rec.add_y_bands(0.7304, 0.0104, color='grey', ax=rec.subplots[index,i], alpha1=0.30, alpha2=0.2, label = r'SH0ES',zorder=-2)
                if i > index:
                        rec.add_x_bands(0.7304, 0.0104, color='grey', ax=rec.subplots[i,index], alpha1=0.30, alpha2=0.2, label = r'SH0ES',zorder=-2)

plot_S_8 = True
if plot_S_8 == True:
        for i in range(len(params_to_plot)):
                index = params_to_plot.index('S_8')
                if i < index:
                        print('here' + str(index))
                        rec.add_y_bands(0.766, 0.02, color='lightsteelblue', ax=rec.subplots[index,i], alpha1=0.40, alpha2=0.3,zorder=-2)
                if i > index:
                        rec.add_x_bands(0.766, 0.02, color='lightsteelblue', ax=rec.subplots[i,index], alpha1=0.40, alpha2=0.3,zorder=-2)



rec.export('WZDR_vs_IDMWZDR.pdf')



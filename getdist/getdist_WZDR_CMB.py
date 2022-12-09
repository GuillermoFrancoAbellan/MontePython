from __future__ import print_function
import sys, os
sys.path.insert(0,os.path.realpath(os.path.join(os.getcwd(),'..')))
from getdist import plots, mcsamples,chains
import pylab as plt
plt.rcParams['text.usetex']=True
import glob 
from getdist import loadMCSamples
from getdist import MCSamples

settings = {'ignore_rows' : 0.3, 'smooth_scale_2D':0.5,'smooth_scale_1D':0.5}
#settings = {'ignore_rows' : 0.3, 'smooth_scale_2D':0.5}

print("~~~~~~~~~~~~importing chains   ~~~~~~~~~~~~~")

s_WZDR1 = loadMCSamples('/home/fabellan/montepython_public/chains/wzdr_pantheon_tight_nobbn_spinstat0_g2eq0_nopantheon/2022-05-23_1000000_', settings = settings)
s_WZDR2 = loadMCSamples('/home/fabellan/montepython_public/chains/WZDR_SPT3G_SPTLens_Plow_Phigh_TTmax1050/2022-04-06_1000000_', settings = settings)
s_WZDR3 = loadMCSamples('/home/fabellan/montepython_public/chains/WZDR_SPT3G_SPTLens_Plow_Phigh_TTTEEEmax1050/2022-03-31_1000000_', settings = settings)
s_WZDR4 = loadMCSamples('/home/fabellan/montepython_public/chains/WZDR_SPT3G_SPTLens_ACTDR4_Plow_Phigh_TTTEmax1050_EE/2022-03-28_1000000_', settings = settings)


print("~~~~~~~~~~~~importing paramnames~~~~~~~~~~~~~")
##useful sometimes; the paramnames is a file that contains all the parameter names and latex labels. (see inside the folder).
s_WZDR1.setParamNames('/home/fabellan/montepython_public/chains/wzdr_pantheon_tight_nobbn_spinstat0_g2eq0_nopantheon/2022-05-20_1000000_.paramnames') 
s_WZDR2.setParamNames('/home/fabellan/montepython_public/chains/WZDR_SPT3G_SPTLens_Plow_Phigh_TTmax1050/2022-04-06_1000000_.paramnames') 
s_WZDR3.setParamNames('/home/fabellan/montepython_public/chains/WZDR_SPT3G_SPTLens_Plow_Phigh_TTTEEEmax1050/2022-03-31_1000000_.paramnames') 
s_WZDR4.setParamNames('/home/fabellan/montepython_public/chains/WZDR_SPT3G_SPTLens_ACTDR4_Plow_Phigh_TTTEmax1050_EE/2022-03-28_1000000_.paramnames') 

##add derived parameters
s_WZDR1.addDerived(s_WZDR1.getParams().sigma8*((1.0-s_WZDR1.getParams().Omega_Lambda)/0.3)**(0.5),'S_8',label=r'$S_8$')
s_WZDR2.addDerived(s_WZDR2.getParams().sigma8*((1.0-s_WZDR2.getParams().Omega_Lambda)/0.3)**(0.5),'S_8',label=r'$S_8$')
s_WZDR3.addDerived(s_WZDR3.getParams().sigma8*((1.0-s_WZDR3.getParams().Omega_Lambda)/0.3)**(0.5),'S_8',label=r'$S_8$')
s_WZDR4.addDerived(s_WZDR4.getParams().sigma8*((1.0-s_WZDR4.getParams().Omega_Lambda)/0.3)**(0.5),'S_8',label=r'$S_8$')

s_WZDR1.addDerived(s_WZDR1.getParams().H0/100,'h',label=r'$h$')
s_WZDR2.addDerived(s_WZDR2.getParams().H0/100,'h',label=r'$h$')
s_WZDR3.addDerived(s_WZDR3.getParams().H0/100,'h',label=r'$h$')
s_WZDR4.addDerived(s_WZDR4.getParams().H0/100,'h',label=r'$h$')

print("~~~set Ranges~~~~~~~~~~~~~")


s_WZDR1.setRanges({'S_8':(0.69,0.89)})
s_WZDR2.setRanges({'S_8':(0.69,0.89)})
s_WZDR3.setRanges({'S_8':(0.69,0.89)})
s_WZDR4.setRanges({'S_8':(0.69,0.89)})

s_WZDR1.setRanges({'h':(0.64,0.77)})
s_WZDR2.setRanges({'h':(0.64,0.77)})
s_WZDR3.setRanges({'h':(0.64,0.77)})
s_WZDR4.setRanges({'h':(0.64,0.77)})

s_WZDR1.setRanges({'N_wzdr':(0,1)})
s_WZDR2.setRanges({'N_wzdr':(0,1)})
s_WZDR2.setRanges({'N_wzdr':(0,1)})
s_WZDR2.setRanges({'N_wzdr':(0,1)})

###create figure
rec = plots.getSubplotPlotter() # set this to an instance of the subplotter 
g = plots.get_single_plotter(width_inch=4, ratio=1)

rec.settings.subplot_size_inch = 2
rec.settings.axes_fontsize = 15
rec.settings.lab_fontsize = 13
rec.settings.legend_fontsize = 13
rec.settings.figure_legend_frame = True 


# tri.settings.legend_frac_subplot_margin = 0.02 # another way to move legend around 
#rec.settings.figure_legend_loc = (0.5,0.9) # set legend location 
# tri.settings.tight_layout = True

print("~~~~~~~~~~~~setting params to output~~~~~~~~~~~~~")
params_to_plot = ['h','S_8','N_wzdr']

print(' --------------------------------- Making triangle plot. --------------------------------- ')

rec.triangle_plot([s_WZDR1,s_WZDR2,s_WZDR3,s_WZDR4],params_to_plot,filled=[True,True,True,True],legend_labels = [r'PlanckTTTEEE+BAO (2111.00014)',r'SPT+PlanckTT[$\ell<1050$]',r'SPT+PlanckTTTEEE[$\ell<1050$]',r'SPT+ACT+PlanckTTTE[$\ell<1050$]EE'],contour_colors = ['blue','red','green','mediumorchid'])

#for ax in rec.fig.axes:
#    geo = ax.get_geometry()
#    if (geo[2]-1) // geo[0] > (geo[2]-1) % geo[0]:
#       for c,z in zip(ax.collections, [19,20,21,17,18,21]):
#           c.zorder =z


plot_H0 = True
if plot_H0 == True:
        for i in range(len(params_to_plot)):
                index = params_to_plot.index('h')
                if i < index:
                        print('here' + str(index))
                        rec.add_y_bands(0.7304, 0.0104, color='grey', ax=rec.subplots[index,i], alpha1=0.30, alpha2=0.2, label = r'SH0ES',zorder = -2)
                if i > index:
                        rec.add_x_bands(0.7304, 0.0104, color='grey', ax=rec.subplots[i,index], alpha1=0.30, alpha2=0.2, label = r'SH0ES',zorder = -2)

plot_S_8 = True
if plot_S_8 == True:
        for i in range(len(params_to_plot)):
                index = params_to_plot.index('S_8')
                if i < index:
                        print('here' + str(index))
                        rec.add_y_bands(0.766, 0.02, color='lightsteelblue', ax=rec.subplots[index,i], alpha1=0.40, alpha2=0.3,zorder = -2)
                if i > index:
                        rec.add_x_bands(0.766, 0.02, color='lightsteelblue', ax=rec.subplots[i,index], alpha1=0.40, alpha2=0.3,zorder = -2)

rec.export('WZDR_CMB.pdf')



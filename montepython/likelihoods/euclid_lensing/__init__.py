########################################################
# Euclid_lensing likelihood
########################################################
# written by Benjamin Audren
# (adapted from J Lesgourgues's old COSMOS likelihood for CosmoMC)
#
# Modified by S. Clesse in March 2016 to add an optional form of n(z)
# motivated by ground based exp. (Van Waerbeke et al., 2013)
# See google doc document prepared by the Euclid IST - Splinter 2
#
# Modified by J. Lesgourgues in March 2016 to vectorise and speed up
#
# Modified by Tim Sprenger in May 2017 to include z-dependent lmax

from montepython.likelihood_class import Likelihood
import io_mp
#import time

import scipy.integrate
from scipy import interpolate as itp
from classy import Class
import os
import numpy as np
import math
import warnings
import matplotlib.pyplot as plt

try:
    xrange
except NameError:
    xrange = range

class euclid_lensing(Likelihood):

    def __init__(self, path, data, command_line):

        Likelihood.__init__(self, path, data, command_line)

        # Force the cosmological module to store Pk for redshifts up to
        # max(self.z) and for k up to k_max
        self.need_cosmo_arguments(data, {'output': 'mPk'})
        self.need_cosmo_arguments(data, {'z_max_pk': self.zmax})
        self.need_cosmo_arguments(data, {'P_k_max_1/Mpc': 0.75*self.k_max_h_by_Mpc})

        # Compute non-linear power spectrum if requested
        if (self.use_halofit):
            self.need_cosmo_arguments(data, {'non linear':'halofit'})

	# Warn if theoretical error and linear cutoff are requested
        if (self.use_lmax_lincut and self.theoretical_error!=0):
    	    warnings.warn("A lmax cutoff infered from kmax and a theoretical error are requested. This combination is not implemented and in most cases not necessary as the theoretical error should induce a cutoff by itself.")

        # Define array of l values, and initialize them
        # It is a logspace
        # find nlmax in order to reach lmax with logarithmic steps dlnl
        self.nlmax = np.int(np.log(self.lmax/self.lmin)/self.dlnl)+1
        # redefine slightly dlnl so that the last point is always exactly lmax
        self.dlnl = np.log(self.lmax/self.lmin)/(self.nlmax-1)
        self.l = self.lmin*np.exp(self.dlnl*np.arange(self.nlmax))

        ########################################################
        # Find distribution of dn_dz (not normalized) in each bin
        ########################################################
        # Assuming each bin contains the same number of galaxies, we find the
        # bin limits in z space
        # Compute the total number of galaxies until zmax (no normalization
        # yet), that is the integral of the galaxy distribution function from 0
        # to self.zmax
        n_tot, error = scipy.integrate.quad(
            self.galaxy_distribution, 0, self.zmax)
        assert error <= 1e-7,  (
            "The integration of the galaxy distribution is not as "
            "precise as expected.")

        # For each bin, compute the limit in z space

        # Create the array that will contain the z boundaries for each bin. The
        # first value is already correctly set to 0.
        self.z_bin_edge = np.zeros(self.nbin+1, 'float64')

        total_count = 0.
        for Bin in xrange(self.nbin-1):
            bin_count = 0.
            z = self.z_bin_edge[Bin]
            while (bin_count <= (n_tot-total_count)/(self.nbin-Bin)):
                gd_1 = self.galaxy_distribution(z)
                gd_2 = self.galaxy_distribution(z+self.dz)
                bin_count += 0.5*(gd_1+gd_2)*self.dz
                z += self.dz
            self.z_bin_edge[Bin+1] = z
            total_count += bin_count
        self.z_bin_edge[self.nbin] = self.zmax

        # Fill array of discrete z values
        self.z = np.linspace(0, self.zmax, num=self.nzmax)

        # Fill distribution for each bin (convolving with photo_z distribution)
        self.eta_z = np.zeros((self.nzmax, self.nbin), 'float64')
        gal = self.galaxy_distribution(self.z, True)
        for Bin in xrange(self.nbin):
            low = self.z_bin_edge[Bin]
            hig = self.z_bin_edge[Bin+1]
            for nz in xrange(self.nzmax):
                z = self.z[nz]
                integrand = gal*self.photo_z_distribution(z, self.z, True)
                integrand = np.array([
                    elem if low <= self.z[index] <= hig else 0
                    for index, elem in enumerate(integrand)])
                self.eta_z[nz, Bin] = scipy.integrate.trapz(
                    integrand,
                    self.z)

        # integrate eta(z) over z (in view of normalizing it to one)
        self.eta_norm = np.zeros(self.nbin, 'float64')
        for Bin in xrange(self.nbin):
            self.eta_norm[Bin] = np.sum(0.5*(
                self.eta_z[1:, Bin]+self.eta_z[:-1, Bin])*(
                self.z[1:]-self.z[:-1]))

        ################
        # Noise spectrum
        ################

        # Number of galaxies per steradian
        self.noise = 3600.*self.gal_per_sqarcmn*(180./math.pi)**2

        # Number of galaxies per steradian per bin
        self.noise = self.noise/self.nbin

        # Noise spectrum (diagonal in bin*bin space, independent of l and Bin)
        self.noise = self.rms_shear**2/self.noise

        ###########
        # Read data
        ###########

        # If the file exists, initialize the fiducial values
        # It has been stored flat, so we use the reshape function to put it in
        # the right shape.
        self.Cl_fid = np.zeros((self.nlmax, self.nbin, self.nbin), 'float64')
        self.fid_values_exist = False
        fid_file_path = os.path.join(self.data_directory, self.fiducial_file)
        if os.path.exists(fid_file_path):
            self.fid_values_exist = True
            flat_Cl = np.loadtxt(fid_file_path)
            self.Cl_fid = flat_Cl.reshape((self.nlmax, self.nbin, self.nbin))

        return

    def galaxy_distribution(self, z, array=False):
        """
        Galaxy distribution returns the function D(z) from the notes

        If the array flag is set to True, z is then interpretated as an array,
        and not as a single value.

        Modified by S. Clesse in March 2016 to add an optional form of n(z) motivated by ground based exp. (Van Waerbeke et al., 2013)
        See google doc document prepared by the Euclid IST - Splinter 2
        """

        zmean = 0.9
        z0 = zmean/1.412

        if not array:
            galaxy_dist = z**2*math.exp(-(z/z0)**(1.5))
        elif self.nofz_method==1:
            return z**2*np.exp(-(z/z0)**(1.5))
        else:
            return self.a1*np.exp(-(z-0.7)**2/self.b1**2.)+self.c1*np.exp(-(z-1.2)**2/self.d1**2.)


        return galaxy_dist

    def photo_z_distribution(self, z, zph, array=True):
        """
        Photo z distribution

        If the array flag is set to True, z is then interpretated as an array,
        and not as a single value.
        """

        # Standard error on dz/(1+z)
        sigma_ph = 0.05

        # Note: you must normalize it yourself to one if you want to get nice
        # plots of the galaxy distribution function in each bin (otherwise, the
        # spectra will remain correct, but each D_i(x) will loot strangely
        # normalized when compared to the original D(z)
        if not array:
            photo_z_dist = math.exp(-0.5*(
                (z-zph)/sigma_ph/(1.+z))**2)/sigma_ph/(1.+z)/math.sqrt(
                2.*math.pi)
        else:
            photo_z_dist = np.exp(-0.5*(
                (z-zph)/sigma_ph/(1.+z))**2)/sigma_ph/(1.+z)/math.sqrt(
                2.*math.pi)

        return photo_z_dist

    def loglkl(self, cosmo, data):

        #start = time.time()

        # One wants to obtain here the relation between z and r, this is done
        # by asking the cosmological module with the function z_of_r
        self.r = np.zeros(self.nzmax, 'float64')
        self.dzdr = np.zeros(self.nzmax, 'float64')

        self.r, self.dzdr = cosmo.z_of_r(self.z)

        # Compute now the selection function eta(r) = eta(z) dz/dr normalized
        # to one. The np.newaxis helps to broadcast the one-dimensional array
        # dzdr to the proper shape. Note that eta_norm is also broadcasted as
        # an array of the same shape as eta_z
        self.eta_r = self.eta_z*(self.dzdr[:, np.newaxis]/self.eta_norm)

        # Compute function g_i(r), that depends on r and the bin
        # g_i(r) = 2r(1+z(r)) int_r^+\infty drs eta_r(rs) (rs-r)/rs
        # The integration starts from r ----> GFA: why?
        g = np.zeros((self.nzmax, self.nbin), 'float64')
        for Bin in xrange(self.nbin):
            for nr in xrange(1, self.nzmax-1):
                fun = self.eta_r[nr:, Bin]*(self.r[nr:]-self.r[nr])/self.r[nr:]
                g[nr, Bin] = np.sum(0.5*(fun[1:]+fun[:-1])*(self.r[nr+1:]-self.r[nr:-1]))
# this commented part is to make the integral start from 0 instead of r
#                fun = self.eta_r[1:, Bin]*(self.r[1:]-self.r[nr])/self.r[1:]
#                g[nr, Bin] = np.sum(0.5*(fun[1:]+fun[:-1])*(self.r[2:]-self.r[1:-1]))
                g[nr, Bin] *= 2.*self.r[nr]*(1.+self.z[nr])

# GFA: Here is where we could read the window functions
#        print("shape of g=",np.shape(g))
#        print("shape of z=",np.shape(self.z))
#        print("shape of r=",np.shape(self.r))
#        print("z=",self.z)
#        print("r=",self.r)

        if self.write_W_of_z:
            W_file_path = os.path.join(
            self.data_directory, self.file_W_of_z)
            with open(W_file_path, 'w') as Wz_file:
                Wz_file.write('# Fiducial parameters')
                for key, value in io_mp.dictitems(data.mcmc_parameters):
                    Wz_file.write(
                        ', %s = %.5g' % (key, value['current']*value['scale']))
                Wz_file.write('\n')
                for nz in range(1,self.nzmax):
                    Wz_file.write("%s\t%s \n" % (self.z[nz],(3.0/4.0)*cosmo.Omega_m()*g[nz,self.bin_to_plot]/self.r[nz]))

        if self.plot_W_of_z:
            nzbins = range(1,self.nzmax)
#            plt.plot(self.z[nzbins],self.r[nzbins])
#            plt.plot(self.z[nzbins],g[nzbins,self.bin_to_plot]/2./self.r[nzbins]/(1.+self.z[nzbins]),label=" %f < z < %f"%(self.z_bin_edge[self.bin_to_plot],self.z_bin_edge[self.bin_to_plot+1]))

#            plt.plot(self.z[nzbins],self.eta_z[nzbins,3]/self.eta_norm[3],'red',label=" %.3f < z < %.3f"%(self.z_bin_edge[3],self.z_bin_edge[4]))
#            plt.plot(self.z[nzbins],self.eta_z[nzbins,6]/self.eta_norm[6],'green',label=" %.3f < z < %.3f"%(self.z_bin_edge[6],self.z_bin_edge[7]))
#            plt.plot(self.z[nzbins],self.eta_z[nzbins,9]/self.eta_norm[9],'blue',label=" %.3f < z < %.3f"%(self.z_bin_edge[9],self.z_bin_edge[10]))

            plt.plot(self.z[nzbins],(3.0/4.0)*cosmo.Omega_m()*g[nzbins,3]/self.r[nzbins],'red',label=" %.3f < z < %.3f"%(self.z_bin_edge[3],self.z_bin_edge[4]))
            plt.plot(self.z[nzbins],(3.0/4.0)*cosmo.Omega_m()*g[nzbins,6]/self.r[nzbins],'green',label=" %.3f < z < %.3f"%(self.z_bin_edge[6],self.z_bin_edge[7]))
            plt.plot(self.z[nzbins],(3.0/4.0)*cosmo.Omega_m()*g[nzbins,9]/self.r[nzbins],'blue',label=" %.3f < z < %.3f"%(self.z_bin_edge[9],self.z_bin_edge[10]))

#            plt.plot(self.z[nzbins],((3.0/4.0)*cosmo.Omega_m()*g[nzbins,9]/self.r[nzbins])*((3.0/4.0)*cosmo.Omega_m()*g[nzbins,9]/self.r[nzbins])/self.dzdr[nzbins],'blue',label="$ij = 99$")
#            plt.plot(self.z[nzbins],((3.0/4.0)*cosmo.Omega_m()*g[nzbins,3]/self.r[nzbins])*((3.0/4.0)*cosmo.Omega_m()*g[nzbins,9]/self.r[nzbins])/self.dzdr[nzbins],'purple', label="$ij = 39$")

#            plt.semilogy()
#            plt.semilogx()
#            plt.grid()
            plt.xlim([0,3.5])
            plt.legend(frameon=False)
            plt.xlabel(r'$ z $', fontsize= 15)
#            plt.ylabel(r'$ r(z) \ \ [\mathrm{Mpc}]$', fontsize=15)
#            plt.ylabel(r'$ n_i(z) $', fontsize=15)
            plt.ylabel(r'$ W_i(z) $', fontsize=15)
#            plt.ylabel(r'$ W_i(z) \  W_j(z) /H(z) \ \mathrm{Mpc} $', fontsize=15)
            plt.show()

	    # compute the maximum l where most contributions are linear
	    # as a function of the lower bin number
        if self.use_lmax_lincut:
            lintegrand_lincut_o = np.zeros((self.nzmax, self.nbin, self.nbin), 'float64')
            lintegrand_lincut_u = np.zeros((self.nzmax, self.nbin, self.nbin), 'float64')
            l_lincut = np.zeros((self.nbin, self.nbin), 'float64')
            l_lincut_mean = np.zeros(self.nbin, 'float64')
            for Bin1 in xrange(self.nbin):
                for Bin2 in xrange(Bin1,self.nbin):
                    lintegrand_lincut_o[1:,Bin1, Bin2] = g[1:, Bin1]*g[1:, Bin2]/(
                        self.r[1:])
            for Bin1 in xrange(self.nbin):
                for Bin2 in xrange(Bin1,self.nbin):
                    lintegrand_lincut_u[1:,Bin1, Bin2] = g[1:, Bin1]*g[1:, Bin2]/(
                        self.r[1:]**2)
            for Bin1 in xrange(self.nbin):
                for Bin2 in xrange(Bin1,self.nbin):
                    l_lincut[Bin1, Bin2] = np.sum(0.5*(
                        lintegrand_lincut_o[1:, Bin1, Bin2] +
                        lintegrand_lincut_o[:-1, Bin1, Bin2])*(
                        self.r[1:]-self.r[:-1]))
                    l_lincut[Bin1, Bin2] /= np.sum(0.5*(
                        lintegrand_lincut_u[1:, Bin1, Bin2] +
                        lintegrand_lincut_u[:-1, Bin1, Bin2])*(
                        self.r[1:]-self.r[:-1]))
            z_peak = np.zeros((self.nbin, self.nbin), 'float64')
            for Bin1 in xrange(self.nbin):
                for Bin2 in xrange(Bin1,self.nbin):
                    z_peak[Bin1, Bin2] = self.zmax
                    for index_z in xrange(self.nzmax):
                        if (self.r[index_z]>l_lincut[Bin1, Bin2]):
                            z_peak[Bin1, Bin2] = self.z[index_z]
                            break
                    if self.use_zscaling:
                        l_lincut[Bin1, Bin2] *= self.kmax_hMpc*cosmo.h()*pow(1.+z_peak[Bin1, Bin2],2./(2.+cosmo.n_s()))
                    else:
                        l_lincut[Bin1, Bin2] *= self.kmax_hMpc*cosmo.h()
                l_lincut_mean[Bin1] = np.sum(l_lincut[Bin1, :])/(self.nbin-Bin1)

	    #for Bin1 in xrange(self.nbin):
	        #for Bin2 in xrange(Bin1,self.nbin):
		    #print("%s\t%s\t%s\t%s" % (Bin1, Bin2, l_lincut[Bin1, Bin2], l_lincut_mean[Bin1]))

	#for nr in xrange(1, self.nzmax-1):
	#	print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (self.z[nr], g[nr, 0], g[nr, 1], g[nr, 2], g[nr, 3], g[nr, 4], g[nr, 5], g[nr, 6], g[nr, 7], g[nr, 8], g[nr, 9]))

        # Get power spectrum P(k=l/r,z(r)) from cosmological module
        kmin_in_inv_Mpc = self.k_min_h_by_Mpc * cosmo.h()
        kmax_in_inv_Mpc = self.k_max_h_by_Mpc * cosmo.h()
        pk = np.zeros((self.nlmax, self.nzmax), 'float64')

        # GFA
        if self.ddm_non_linear:
            LCDM = Class()
            commonsettings={'omega_b':cosmo.omega_b(), 'omega_cdm':cosmo.omega_cdm()+cosmo.omega_ini_dcdm(),'h':cosmo.h(),'tau_reio':cosmo.tau_reio(),'n_s':cosmo.n_s(),'A_s':cosmo.A_s(),'output':'mPk','non linear':'halofit','z_max_pk': self.zmax,'P_k_max_h/Mpc': self.k_max_h_by_Mpc,'N_ur':2.0328,'N_ncdm':1,'m_ncdm':0.06}
            LCDM.set(commonsettings)
            LCDM.compute()
            pk_nl_lcdm = np.zeros((self.nlmax, self.nzmax), 'float64')
            epsilon_lin = np.zeros(self.nzmax, 'float64')
            u = cosmo.omega_b()/0.02216
            v = cosmo.h()/0.6776
            w = (cosmo.omega_cdm()+cosmo.omega_ini_dcdm()+cosmo.omega_b())/0.14116
            alpha = (5.323-1.4644*u-1.391*v)+(-2.055+1.329*u+0.8672*v)*w+(0.2682-0.3509*u)*w*w
            beta  = 0.9260+(0.05735-0.02690*v)*w+(-0.01373+0.006713*v)*w*w
            gamma =  (9.553-0.7860*v)+(0.4884+0.1754*v)*w+(-0.2512+0.07558*v)*w*w
            frac_ddm = cosmo.omega_ini_dcdm()/(cosmo.omega_ini_dcdm()+cosmo.omega_cdm())

        for index_z in xrange(1, self.nzmax):

            if self.ddm_non_linear:
                aa = 0.7208+2.027*(1/cosmo.tau_gyr())+3.031*(1/(1+1.1*self.z[index_z]))-0.18
                bb = 0.0120+2.786*(1/cosmo.tau_gyr())+0.6699*(1/(1+1.1*self.z[index_z]))-0.09
                pp = 1.045+1.225*(1/cosmo.tau_gyr())+0.2207*(1/(1+1.1*self.z[index_z]))-0.099
                qq = 0.9922+1.735*(1/cosmo.tau_gyr())+0.2154*(1/(1+1.1*self.z[index_z]))-0.056
                epsilon_lin[index_z] = alpha*((1.0/cosmo.tau_gyr())**beta)*(1.0/(0.105*self.z[index_z]+1.0))**gamma

            for index_l in xrange(self.nlmax):
        # These lines would return an error when you ask for P(k,z) out of computed range
        #        if (self.l[index_l]/self.r[index_z] > self.k_max):
        #            raise io_mp.LikelihoodError(
        #                "you should increase euclid_lensing.k_max up to at least %g" % (self.l[index_l]/self.r[index_z]))
        #        pk[index_l, index_z] = cosmo.pk(
        #            self.l[index_l]/self.r[index_z], self.z[index_z])

        # These lines set P(k,z) to zero out of [k_min, k_max] range
                k_in_inv_Mpc =  self.l[index_l]/self.r[index_z]
                if (k_in_inv_Mpc < kmin_in_inv_Mpc) or (k_in_inv_Mpc > kmax_in_inv_Mpc):
                    pk[index_l, index_z] = 0.
                else:
                    if self.ddm_non_linear:
                        pk_nl_lcdm[index_l, index_z] = LCDM.pk(self.l[index_l]/self.r[index_z], self.z[index_z])
                        epsilon_nl_over_lin = ((1+aa*(self.l[index_l]/self.r[index_z])**pp)/(1+bb*(self.l[index_l]/self.r[index_z])**qq))*frac_ddm
                        pk[index_l, index_z] =(1-epsilon_nl_over_lin*epsilon_lin[index_z])*pk_nl_lcdm[index_l, index_z]
        #                print("l=%s z=%s pk_res=%e" %(self.l[index_l], self.z[index_z], pk[index_l, index_z]/pk_nl_lcdm[index_l, index_z]))
                    else:
                        pk[index_l, index_z] = cosmo.pk(self.l[index_l]/self.r[index_z], self.z[index_z])



        # Recover the non_linear scale computed by halofit. If no scale was
        # affected, set the scale to one, and make sure that the nuisance
        # parameter epsilon is set to zero
        k_sigma = np.zeros(self.nzmax, 'float64')
        if (cosmo.nonlinear_method == 0):
            k_sigma[:] = 1.e6
        else:
            k_sigma = cosmo.nonlinear_scale(self.z, self.nzmax)

	    # replace unphysical values of k_sigma
        if not (cosmo.nonlinear_method == 0):
    	    k_sigma_problem = False
    	    for index_z in xrange(self.nzmax-1):
    	        if (k_sigma[index_z+1]<k_sigma[index_z]) or (k_sigma[index_z+1]>2.5):
    	            k_sigma[index_z+1] = 2.5
    	            k_sigma_problem = True
    	        #print("%s\t%s" % (k_sigma[index_z], self.z[index_z]))
    	    if k_sigma_problem:
    	        warnings.warn("There were unphysical (decreasing in redshift or exploding) values of k_sigma (=cosmo.nonlinear_scale(...)). To proceed they were set to 2.5, the highest scale that seems to be stable.")

        # Define the alpha function, that will characterize the theoretical
        # uncertainty. Chosen to be 0.001 at low k, raise between 0.1 and 0.2
        # to self.theoretical_error
        alpha = np.zeros((self.nlmax, self.nzmax), 'float64')
        # self.theoretical_error = 0.1
        if self.theoretical_error != 0:
#MArchi     for index_l in range(self.nlmax):
                #k = self.l[index_l]/self.r[1:]
                #alpha[index_l, 1:] = np.log(1.+k[:]/k_sigma[1:])/(
                    #1.+np.log(1.+k[:]/k_sigma[1:]))*self.theoretical_error
            for index_l in xrange(self.nlmax):
             for index_z in xrange(1, self.nzmax):
                k = self.l[index_l]/self.r[index_z]
                alpha[index_l, index_z] = np.log(1.+k/k_sigma[index_z])/(
                    1.+np.log(1.+k/k_sigma[index_z]))*self.theoretical_error

        # recover the e_th_nu part of the error function
        e_th_nu = self.coefficient_f_nu*cosmo.Omega_nu/cosmo.Omega_m()

        # Compute the Error E_th_nu function
        if 'epsilon' in self.use_nuisance:
            E_th_nu = np.zeros((self.nlmax, self.nzmax), 'float64')
            for index_l in range(1, self.nlmax):
                E_th_nu[index_l, :] = np.log(
                    1.+self.l[index_l]/k_sigma[:]*self.r[:]) / (
                    1.+np.log(1.+self.l[index_l]/k_sigma[:]*self.r[:]))*e_th_nu

        # Add the error function, with the nuisance parameter, to P_nl_th, if
        # the nuisance parameter exists
                for index_l in range(self.nlmax):
                    epsilon = data.mcmc_parameters['epsilon']['current']*(
                        data.mcmc_parameters['epsilon']['scale'])
                    pk[index_l, :] *= (1.+epsilon*E_th_nu[index_l, :])

        # Start loop over l for computation of C_l^shear
        Cl_integrand = np.zeros((self.nzmax, self.nbin, self.nbin), 'float64')
        Cl = np.zeros((self.nlmax, self.nbin, self.nbin), 'float64')
        # Start loop over l for computation of E_l
        if self.theoretical_error != 0:
            El_integrand = np.zeros((self.nzmax, self.nbin, self.nbin),
                                    'float64')
            El = np.zeros((self.nlmax, self.nbin, self.nbin), 'float64')

        for nl in xrange(self.nlmax):

            # find Cl_integrand = (g(r) / r)**2 * P(l/r,z(r))
            for Bin1 in xrange(self.nbin):
                for Bin2 in xrange(Bin1,self.nbin):
                    Cl_integrand[1:, Bin1, Bin2] = g[1:, Bin1]*g[1:, Bin2]/(
                        self.r[1:]**2)*pk[nl, 1:]
                    if self.theoretical_error != 0:
                        El_integrand[1:, Bin1, Bin2] = g[1:, Bin1]*(
                            g[1:, Bin2])/(
                            self.r[1:]**2)*pk[nl, 1:]*alpha[nl, 1:]

            # Integrate over r to get C_l^shear_ij = P_ij(l)
            # C_l^shear_ij = 9/16 Omega0_m^2 H_0^4 \sum_0^rmax dr (g_i(r)
            # g_j(r) /r**2) P(k=l/r,z(r))
            # It it then multiplied by 9/16*Omega_m**2 to be in units of Mpc**4
            # and then by (h/2997.9)**4 to be dimensionless
            for Bin1 in xrange(self.nbin):
                for Bin2 in xrange(Bin1,self.nbin):
                    Cl[nl, Bin1, Bin2] = np.sum(0.5*(
                        Cl_integrand[1:, Bin1, Bin2] +
                        Cl_integrand[:-1, Bin1, Bin2])*(
                        self.r[1:]-self.r[:-1]))
                    Cl[nl, Bin1, Bin2] *= 9./16.*(cosmo.Omega_m())**2
                    Cl[nl, Bin1, Bin2] *= (cosmo.h()/2997.9)**4

                    if self.theoretical_error != 0:
                        El[nl, Bin1, Bin2] = np.sum(0.5*(
                            El_integrand[1:, Bin1, Bin2] +
                            El_integrand[:-1, Bin1, Bin2])*(
                            self.r[1:]-self.r[:-1]))
                        El[nl, Bin1, Bin2] *= 9./16.*(cosmo.Omega_m())**2
                        El[nl, Bin1, Bin2] *= (cosmo.h()/2997.9)**4
                    if Bin1 == Bin2:
                        Cl[nl, Bin1, Bin2] += self.noise

        # Write fiducial model spectra if needed (exit in that case)
        if self.fid_values_exist is False:
            # Store the values now, and exit.
            fid_file_path = os.path.join(
                self.data_directory, self.fiducial_file)
            with open(fid_file_path, 'w') as fid_file:
                fid_file.write('# Fiducial parameters')
                for key, value in io_mp.dictitems(data.mcmc_parameters):
                    fid_file.write(
                        ', %s = %.5g' % (key, value['current']*value['scale']))
                fid_file.write('\n')
                for nl in range(self.nlmax):
                    for Bin1 in range(self.nbin):
                        for Bin2 in range(self.nbin):
                            fid_file.write("%.8g\n" % Cl[nl, Bin1, Bin2])
            print('\n')
            warnings.warn(
                "Writing fiducial model in %s, for %s likelihood\n" % (
                    self.data_directory+'/'+self.fiducial_file, self.name))
            return 1j


# START OF MODIFICATIONS BY VP AND GFA
#        print("residuals in % at ij=99 and l=984 w.r.t. LCDM are ",100.0*(Cl[26, self.bin_to_plot, self.bin_to_plot]/(3.525604e-9)-1.0))
#        print("residuals in % at ij=33 and l=984 w.r.t. LCDM are ",100.0*(Cl[26, self.bin_to_plot, self.bin_to_plot]/(2.792159e-09)-1.0))
#        print(self.z)
        if self.write_LCDM:
            self.file_LCDM_exist = False
            # Store the values now, and exit.
            LCDM_file_path = os.path.join(
                self.data_directory, self.file_LCDM)
            print(LCDM_file_path)
            with open(LCDM_file_path, 'w') as LCDM_file:
                LCDM_file.write('# Fiducial parameters')
                for key, value in io_mp.dictitems(data.mcmc_parameters):
                    LCDM_file.write(
                        ', %s = %.5g' % (key, value['current']*value['scale']))
                LCDM_file.write('\n')
                for nl in range(self.nlmax):
                    LCDM_file.write("%.8g\n" % Cl[nl, self.bin_to_plot, self.bin_to_plot])
#            print("C_{l=984}^{ij=99} for LCDM is ",Cl[26, self.bin_to_plot, self.bin_to_plot])
            print("C_{l=984}^{ij=33} for LCDM is ",Cl[26, self.bin_to_plot, self.bin_to_plot])

        if self.read_LCDM:
            self.file_LCDM_exist = False
            LCDM_file_path = os.path.join(self.data_directory, self.file_LCDM)
            if os.path.exists(LCDM_file_path):
                self.file_LCDM_exist = True
                Cl_LCDM = np.loadtxt(LCDM_file_path)
                self.Cl_LCDM = Cl_LCDM.reshape((self.nlmax, 1, 1))

        if self.plot:
            nlbins=range(self.nlmax)
            #print("nlmax=",self.nlmax)
            print(self.l)
            if self.plot_residuals and  self.file_LCDM_exist:
                plt.plot(self.l,Cl[nlbins, self.bin_to_plot, self.bin_to_plot]/Cl_LCDM[nlbins]-1,label="%f < z < %f"%(self.z_bin_edge[self.bin_to_plot],self.z_bin_edge[self.bin_to_plot+1]))
            else:
                if self.file_LCDM_exist:
		                  plt.plot(self.l,Cl_LCDM[nlbins],label="LCDM, %f < z < %f"%(self.z_bin_edge[self.bin_to_plot],self.z_bin_edge[self.bin_to_plot+1]))
                plt.plot(self.l,Cl[nlbins, self.bin_to_plot, self.bin_to_plot],label="DCDM, Gamma(km/s/Mpc)= 760, f_dcdm=0.038")
                plt.semilogy()
            plt.semilogx()
            plt.legend()
            plt.show()
        #GFA
        if self.write_DCDM:
            DCDM_file_path = os.path.join(
            self.data_directory, self.file_DCDM)
            with open(DCDM_file_path, 'w') as DCDM_file:
                DCDM_file.write('# Fiducial parameters')
                for key, value in io_mp.dictitems(data.mcmc_parameters):
                    DCDM_file.write(
                        ', %s = %.5g' % (key, value['current']*value['scale']))
                DCDM_file.write('\n')
                for nl in range(self.nlmax):
                    DCDM_file.write("%.8g\n" % Cl[nl, self.bin_to_plot, self.bin_to_plot])


## END OF MODIFICATIONS BY VP AND GFA

        # Now that the fiducial model is stored, we add the El to both Cl and
        # Cl_fid (we create a new array, otherwise we would modify the
        # self.Cl_fid from one step to the other)

        # Spline Cl[nl,Bin1,Bin2] along l
        spline_Cl = np.empty((self.nbin, self.nbin), dtype=(list, 3))
        for Bin1 in xrange(self.nbin):
            for Bin2 in xrange(Bin1, self.nbin):
                spline_Cl[Bin1, Bin2] = list(itp.splrep(
                    self.l, Cl[:, Bin1, Bin2]))
                if Bin2 > Bin1:
                    spline_Cl[Bin2, Bin1] = spline_Cl[Bin1, Bin2]

        # Spline El[nl,Bin1,Bin2] along l
        if self.theoretical_error != 0:
            spline_El = np.empty((self.nbin, self.nbin), dtype=(list, 3))
            for Bin1 in xrange(self.nbin):
                for Bin2 in xrange(Bin1, self.nbin):
                    spline_El[Bin1, Bin2] = list(itp.splrep(
                        self.l, El[:, Bin1, Bin2]))
                    if Bin2 > Bin1:
                        spline_El[Bin2, Bin1] = spline_El[Bin1, Bin2]

        # Spline Cl_fid[nl,Bin1,Bin2]    along l
        spline_Cl_fid = np.empty((self.nbin, self.nbin), dtype=(list, 3))
        for Bin1 in xrange(self.nbin):
            for Bin2 in xrange(Bin1, self.nbin):
                spline_Cl_fid[Bin1, Bin2] = list(itp.splrep(
                    self.l, self.Cl_fid[:, Bin1, Bin2]))
                if Bin2 > Bin1:
                    spline_Cl_fid[Bin2, Bin1] = spline_Cl_fid[Bin1, Bin2]

        # Compute likelihood

        # Prepare interpolation for every integer value of l, from the array
        # self.l, to finally compute the likelihood (sum over all l's)
        dof = 1./(int(self.l[-1])-int(self.l[0])+1)

        ells = range(int(self.l[0]), int(self.l[-1])+1)

        # Define cov theory, observ and error on the whole integer range of ell
        # values
        Cov_theory = np.zeros((len(ells), self.nbin, self.nbin), 'float64')
        Cov_observ = np.zeros((len(ells), self.nbin, self.nbin), 'float64')
        Cov_error = np.zeros((len(ells), self.nbin, self.nbin), 'float64')

        for Bin1 in xrange(self.nbin):
            for Bin2 in xrange(Bin1, self.nbin):
                Cov_theory[:, Bin1, Bin2] = itp.splev(
                    ells, spline_Cl[Bin1, Bin2])
                Cov_observ[:, Bin1, Bin2] = itp.splev(
                    ells, spline_Cl_fid[Bin1, Bin2])
                if self.theoretical_error > 0:
                    Cov_error[:, Bin1, Bin2] = itp.splev(
                        ells, spline_El[Bin1, Bin2])
                if Bin2 > Bin1:
                    Cov_theory[:, Bin2, Bin1] = Cov_theory[:, Bin1, Bin2]
                    Cov_observ[:, Bin2, Bin1] = Cov_observ[:, Bin1, Bin2]
                    Cov_error[:, Bin2, Bin1] = Cov_error[:, Bin1, Bin2]

        chi2 = 0.

        # TODO parallelize this
        for index, ell in enumerate(ells):

            if self.use_lmax_lincut:
                    CutBin = -1
                    for zBin in xrange(self.nbin):
                        if (ell<l_lincut_mean[zBin]):
                            CutBin = zBin
                            det_theory = np.linalg.det(Cov_theory[index, CutBin:, CutBin:])
                            det_observ = np.linalg.det(Cov_observ[index, CutBin:, CutBin:])
                            break
                    if (CutBin==-1):
                        break
            else:
                    det_theory = np.linalg.det(Cov_theory[index, :, :])
                    det_observ = np.linalg.det(Cov_observ[index, :, :])
            if (self.theoretical_error > 0):
                    det_cross_err = 0
                    for i in range(self.nbin):
                            newCov = np.copy(Cov_theory[index,:,:]) #MArchi#newCov = np.copy(Cov_theory)
                            newCov[:, i] = Cov_error[index,:, i] #MArchi#newCov[:, i] = Cov_error[:, i]
                            det_cross_err += np.linalg.det(newCov)

                    # Newton method
                    # Find starting point for the method:
                    start = 0
                    step = 0.001*det_theory/det_cross_err
                    error = 1
                    old_chi2 = -1.*data.boundary_loglike
                    error_tol = 0.01
                    epsilon_l = start
                    while error > error_tol:
                        vector = np.array([epsilon_l-step,
                                           epsilon_l,
                                           epsilon_l+step])
                        #print(vector.shape)
                    # Computing the function on three neighbouring points
                        function_vector = np.zeros(3, 'float64')
                        for k in range(3):
                            Cov_theory_plus_error = Cov_theory+vector[k]*Cov_error
                            det_theory_plus_error = np.linalg.det(Cov_theory_plus_error[index,:,:]) #MArchi#det_theory_plus_error = np.linalg.det(Cov_theory_plus_error)
                            det_theory_plus_error_cross_obs = 0
                            for i in range(self.nbin):
                                newCov = np.copy(Cov_theory_plus_error[index,:,:])#MArchi#newCov = np.copy(Cov_theory_plus_error)
                                newCov[:, i] = Cov_observ[index,:, i]#MArchi#newCov[:, i] = Cov_observ[:, i]
                                det_theory_plus_error_cross_obs += np.linalg.det(
                                    newCov)
                            try:
                                function_vector[k] = (2.*ell+1.)*self.fsky*(det_theory_plus_error_cross_obs/det_theory_plus_error + math.log(det_theory_plus_error/det_observ) - self.nbin ) + dof*vector[k]**2
                            except ValueError:
                            	warnings.warn("Euclid_lensing: Could not evaluate chi2 including theoretical error with the current parameters. The corresponding chi2 is now set to nan!")
                            	break
                            	break
                            	break
                            	chi2 = np.nan


                        # Computing first
                        first_d    = (function_vector[2]-function_vector[0]) / (vector[2]-vector[0])
                        second_d = (function_vector[2]+function_vector[0]-2*function_vector[1]) / (vector[2]-vector[1])**2

                        # Updating point and error
                        epsilon_l = vector[1] - first_d/second_d
                        error = abs(function_vector[1] - old_chi2)
                        old_chi2 = function_vector[1]
                # End Newton

                    Cov_theory_plus_error = Cov_theory + epsilon_l * Cov_error
                    det_theory_plus_error = np.linalg.det(Cov_theory_plus_error[index,:,:]) #MArchi#det_theory_plus_error = np.linalg.det(Cov_theory_plus_error)

                    det_theory_plus_error_cross_obs = 0
                    for i in range(self.nbin):
                        newCov = np.copy(Cov_theory_plus_error[index,:,:]) #MArchi#newCov = np.copy(Cov_theory_plus_error)
                        newCov[:, i] = Cov_observ[index,:, i] #MArchi#newCov[:, i] = Cov_observ[:, i]
                        det_theory_plus_error_cross_obs += np.linalg.det(newCov)

                    chi2 += (2.*ell+1.)*self.fsky*(det_theory_plus_error_cross_obs/det_theory_plus_error + math.log(det_theory_plus_error/det_observ) - self.nbin ) + dof*epsilon_l**2


            else:
                if self.use_lmax_lincut:
                            det_cross = 0.
                            for i in xrange(0,self.nbin-CutBin):
                                newCov = np.copy(Cov_theory[index, CutBin:, CutBin:])
                                newCov[:, i] = Cov_observ[index, CutBin:, CutBin+i]
                                det_cross += np.linalg.det(newCov)
                else:
                            det_cross = 0.
                            for i in xrange(self.nbin):
                                newCov = np.copy(Cov_theory[index, :, :])
                                newCov[:, i] = Cov_observ[index, :, i]
                                det_cross += np.linalg.det(newCov)

                if self.use_lmax_lincut:
                            chi2 += (2.*ell+1.)*self.fsky*(det_cross/det_theory + math.log(det_theory/det_observ) - self.nbin+CutBin)
                else:
                            chi2 += (2.*ell+1.)*self.fsky*(det_cross/det_theory + math.log(det_theory/det_observ) - self.nbin)

        # Finally adding a gaussian prior on the epsilon nuisance parameter, if
        # present
        if 'epsilon' in self.use_nuisance:
            epsilon = data.mcmc_parameters['epsilon']['current'] * \
                data.mcmc_parameters['epsilon']['scale']
            chi2 += epsilon**2

        #end = time.time()
        #print("time needed in s:",(end-start))

        return -chi2/2.

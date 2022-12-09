#Likelihood by Guillermo Franco Abellan 

import os 
import numpy as np
from montepython.likelihood_class import Likelihood_prior
import scipy.constants as conts


class BOSS_DR14_quasars(Likelihood_prior):


    def loglkl(self, cosmo, data):
        H_at_z = cosmo.Hubble(self.z) * conts.c / 1000.0
        rd = cosmo.rs_drag() * self.rd_rescale
#        rd = self.rd_fid_in_Mpc
        theo_H_rd_by_rdfid = H_at_z * rd / self.rd_fid_in_Mpc
        H_diff = theo_H_rd_by_rdfid - self.H_rd_by_rdfid_in_km_per_s_per_Mpc
        loglkl = -0.5 * ( H_diff ** 2) / (self.sigma ** 2)    
        return loglkl

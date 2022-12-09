#Likelihood by Guillermo Franco Abellan 

import os 
import numpy as np
from montepython.likelihood_class import Likelihood_prior
import scipy.constants as conts

class BOSS_DR12_Lya_combined_v2(Likelihood_prior):
 
    def loglkl(self, cosmo, data):
        H_at_z1 = cosmo.Hubble(self.z1)
        H_at_z2 = cosmo.Hubble(self.z2)
        rd = self.rd_fid_in_Mpc
        theo_D_H1_by_rd = (H_at_z1*rd)**(-1)
        theo_D_H2_by_rd = (H_at_z2*rd)**(-1)        
        D1_diff = theo_D_H1_by_rd - self.D_H1_by_rd
        D2_diff = theo_D_H2_by_rd - self.D_H2_by_rd
        chi2 = (D1_diff ** 2) / (self.sigma1 ** 2)
        chi2 += (D2_diff ** 2) / (self.sigma2 ** 2)
        loglkl = -0.5 * chi2
        return loglkl

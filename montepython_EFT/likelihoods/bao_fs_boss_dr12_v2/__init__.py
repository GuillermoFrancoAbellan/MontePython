#Likelihood by Guillermo Franco Abellan 

import os
import numpy as np
from montepython.likelihood_class import Likelihood_prior
import scipy.constants as conts

class bao_fs_boss_dr12_v2(Likelihood_prior):

    def loglkl(self, cosmo, data):
        H_at_z1 = cosmo.Hubble(self.z1) * conts.c / 1000.0
        H_at_z2 = cosmo.Hubble(self.z2) * conts.c / 1000.0
        H_at_z3 = cosmo.Hubble(self.z3) * conts.c / 1000.0
        rd = cosmo.rs_drag() * self.rs_rescale
#        rd = self.rd_fid_in_Mpc 
        theo_H1_rd_by_rdfid = H_at_z1 * rd / self.rd_fid_in_Mpc
        theo_H2_rd_by_rdfid = H_at_z2 * rd / self.rd_fid_in_Mpc
        theo_H3_rd_by_rdfid = H_at_z3 * rd / self.rd_fid_in_Mpc
        H1_diff = theo_H1_rd_by_rdfid - self.H1_rd_by_rdfid_in_km_per_s_per_Mpc
        H2_diff = theo_H2_rd_by_rdfid - self.H2_rd_by_rdfid_in_km_per_s_per_Mpc
        H3_diff = theo_H3_rd_by_rdfid - self.H3_rd_by_rdfid_in_km_per_s_per_Mpc
        chi2 = ( H1_diff ** 2) / (self.sigma1 ** 2)
        chi2 += ( H2_diff ** 2) / (self.sigma2 ** 2)
        chi2 += ( H3_diff ** 2) / (self.sigma3 ** 2)
        loglkl = - 0.5 * chi2
        return loglkl

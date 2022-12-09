import os
from montepython.likelihood_class import Likelihood_prior


class rs_rec_prior_planck(Likelihood_prior):

    # initialisation of the class is done within the parent Likelihood_prior. For
    # this case, it does not differ, actually, from the __init__ method in
    # Likelihood class.
    def loglkl(self, cosmo, data):

        rs = cosmo.rs_rec()
        loglkl = -0.5 * (rs - self.rs_rec) ** 2 / (self.sigma ** 2)
        return loglkl

import os
from montepython.likelihood_class import Likelihood_prior


class sh0es_Mb(Likelihood_prior):

    # initialisation of the class is done within the parent Likelihood_prior. For
    # this case, it does not differ, actually, from the __init__ method in
    # Likelihood class.
    def loglkl(self, cosmo, data):

        Mb = data.mcmc_parameters['M']['current']*data.mcmc_parameters['M']['scale']
        loglkl = -0.5 * (Mb - self.Mb) ** 2 / (self.sigma ** 2)
        return loglkl

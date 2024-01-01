"FUNCTIONS FOR TASKS"

from icet import ClusterSpace, ClusterExpansion
from trainstation import CrossValidationEstimator
import matplotlib.pyplot as plt 
import pandas as pd



def get_fit_data(fit_method,sc):
    
    cve = CrossValidationEstimator(fit_data=sc.get_fit_data(key='dft_energies_per_fu'), fit_method=fit_method)
    cve.validate()
    cve.train()

    return cve


def get_row(cve):
    
    row = dict()
    row['fit_method'] = fit_method
    row['rmse_validation'] = cve.rmse_validation
    row['rmse_train'] = cve.rmse_train
    row['BIC'] = cve.model.BIC
    row['n_parameters'] = cve.n_parameters
    row['n_nonzero_parameters'] = cve.n_nonzero_parameters
    
    return row

def get_cem_new(cve,cs):
    
    ce = ClusterExpansion(cluster_space=cs, parameters=cve.parameters, metadata=cve.summary)
    
    return ce
    
def plot_eci(ce):
    
    df_ce = ce.to_dataframe()

    radius_pair = [df_ce['radius'][i] for i in range(len(df_ce)) if df_ce['order'][i]==2]
    radius_trip = [df_ce['radius'][i] for i in range(len(df_ce)) if df_ce['order'][i]==3]

    eci_pair = [df_ce['eci'][j] for j in range(len(df_ce)) if df_ce['order'][j]==2]
    eci_trip = [df_ce['eci'][j] for j in range(len(df_ce)) if df_ce['order'][j]==3]

    fig, ax = plt.subplots()

    ax.set_xlabel("Radius($\AA$)")
    ax.set_ylabel("ECI(eV)")

    ax.scatter(radius_pair,eci_pair, c='darkorchid',label ='Pairs')
    ax.scatter(radius_trip,eci_trip, c='forestgreen',label ='Triplets')

    ax.legend(loc='best')
    
    return fig, ax       
from icet  import ClusterExpansion
from icet.tools.structure_generation import generate_sqs
import numpy as np
from multiprocessing import Pool

ce = ClusterExpansion.read('ce_site_energies')
cs = ce.get_cluster_space_copy()

Sr_conc = np.array([0.125,0.875])

def get_sqs(Sr_conc):
    target_concentrations = {'A':{'Sr':Sr_conc, 'Pb':1-Sr_conc}}
    sqs = generate_sqs(cluster_space=cs,max_size=16,include_smaller_cells=False,target_concentrations=target_concentrations,n_steps=500000)
    sqs.write('sqs_Sr_conc_{}.vasp'.format(Sr_conc))

if __name__ == "__main__":
    pool = Pool(processes=2)
    results = pool.map_async(get_sqs, Sr_conc)
    results.get()
    pool.close()

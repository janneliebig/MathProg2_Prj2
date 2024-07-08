import pandas as pd

from generate_datasets import Generate, DATA_TYPE
import plot_datasets
import clustering
import runtime

# generate, scale and plot standard datasets + print runtime table
# if plot is false -> just table
def std_datasets(plot : bool):
    gen = Generate(n_samples=1000, factor=0.5, m_noise=0.05, c_noise=0.05, random_state=1000)
    if plot: plot_datasets.plot_std_datasets(gen)

    gen.scale_datasets()
    t= [[runtime.messure(gen, d, c) for d in DATA_TYPE] for c in runtime.CLUSTER_ALGORITHM]

    print("%-20s%-20s  %s" % ('DATASET', 'ALGORITHM', 'TIME'))
    for d in DATA_TYPE:
        for c in runtime.CLUSTER_ALGORITHM:
            print("%-20s%-20s: %.10f sec" % (d.name, c.name, t[c.value][d.value]))

    if plot: plot_datasets.plot_std_datasets(gen)

#def spec_datasets(plot : bool):


# main:
std_datasets(plot=True)
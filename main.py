from generate_datasets import Generate, DATA_TYPE
import plot_datasets
import clustering
import runtime


gen = Generate(n_samples=1000, factor=0.5, m_noise=0.05, c_noise=0.05, random_state=1000)
plot_datasets.plot_datasets(gen)

gen.scale_datasets()

t = runtime.messure(gen, DATA_TYPE.CIRCLES, runtime.CLUSTER_ALGORITHM.DBSCAN)
print("Time:  " + str(t))

plot_datasets.plot_datasets(gen)
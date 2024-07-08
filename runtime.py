import time
import clustering
from generate_datasets import Generate, DATA_TYPE
from enum import Enum

class CLUSTER_ALGORITHM(Enum):
    KMEANS = 0
    WARD = 1
    DBSCAN = 2
    GAUSSIAN_MIXTURE = 3

gen = Generate(n_samples=1000, factor=0.5, m_noise=0.05, c_noise=0.05, random_state=1000)

# kMeans algorithm
"""
clustering.Cluster.kmeans(gen, DATA_TYPE.CIRCLES, 4)
clustering.Cluster.kmeans(gen, DATA_TYPE.BLOBS, 5)
clustering.Cluster.kmeans(gen, DATA_TYPE.MOONS, 3)
"""
# ward algorithm
"""
clustering.Cluster.ward(gen, DATA_TYPE.CIRCLES, 4)
clustering.Cluster.ward(gen, DATA_TYPE.BLOBS, 4)
clustering.Cluster.ward(gen, DATA_TYPE.MOONS, 4)
"""

# DBSCAN algorithm
"""
clustering.Cluster.dbscan(gen, DATA_TYPE.CIRCLES, 0.3)
clustering.Cluster.dbscan(gen, DATA_TYPE.BLOBS, 0.3)
clustering.Cluster.dbscan(gen, DATA_TYPE.MOONS, 0.3)
"""
# gaussianMixtrue algorithm
clustering.Cluster.gaussian_mixture(gen, DATA_TYPE.CIRCLES, 3)
clustering.Cluster.gaussian_mixture(gen, DATA_TYPE.BLOBS, 3)
clustering.Cluster.gaussian_mixture(gen, DATA_TYPE.MOONS, 3)

def messure(gen : Generate, dtype : DATA_TYPE, ctype : CLUSTER_ALGORITHM) -> float:
    start = time.time()
    if ctype == CLUSTER_ALGORITHM.KMEANS:
        clustering.Cluster.kmeans(gen, dtype, 4)
    elif ctype==CLUSTER_ALGORITHM.WARD:
        clustering.Cluster.ward(gen, dtype, 4)
    elif ctype == CLUSTER_ALGORITHM.DBSCAN:
        clustering.Cluster.dbscan(gen, dtype, 0.3)
    elif ctype == CLUSTER_ALGORITHM.GAUSSIAN_MIXTURE:
        clustering.Cluster.gaussian_mixture(gen, dtype, 4)
    end = time.time()
    return end - start

"""from sklearn.datasets import make_circles

X, y = make_circles(n_samples=1000, factor=0.5, noise=0.05)

print(X.shape)
print(y.shape)
"""
# K-Means
# 1 Number of clusters to split data into
# 2 Select K random points
# 3 Calculate distance between centroids and other points
# 4 Assign the points to the closest centroid
# 5 Calculate the centre of each cluster
# 6 Repeat 3-5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.preprocessing as preprocessing
from sklearn.preprocessing import StandardScaler
from enum import Enum
#from scale_datasets import Scaler
from sklearn import datasets, cluster
#n_samples = 1500

#X_4, y_4 = datasets.make_s_curve(n_samples, noise=0.05, random_state=10)
class DATA_TYPE(Enum):
    CIRCLES = 0
    MOONS = 1
    BLOBS = 2

class Generate:
    def __init__(self, n_samples, factor, c_noise, m_noise, random_state):
        self.circlesX, self.circlesY = self.circles(n_samples=n_samples, factor=factor, noise=c_noise)
        self.moonsX, self.moonsY = self.moons(n_samples=n_samples, noise=m_noise)
        self.blobsX, self.blobsY = self.blobs(n_samples=n_samples, random_state=random_state)
        self.is_scaled : bool = False

    def circles(self, n_samples : int, factor : float, noise : float) -> list:
        X,y = datasets.make_circles(n_samples=n_samples, factor=factor, noise=noise)
        return X,y

    def moons(self, n_samples : int, noise : float) -> list:
        X,y = datasets.make_moons(n_samples=n_samples, noise=noise)
        return X,y

    def blobs(self, n_samples : int, random_state : int) -> list:
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        # // transform data
        transformation_matrix = np.array([[0.8, -0.5],[-0.2, 0.6]])
        X = np.dot(X, transformation_matrix)
        return X,y
    
    def get_dataset(self, type : DATA_TYPE):
        if type == DATA_TYPE.CIRCLES:
            return [self.circlesX, self.circlesY]
        elif type == DATA_TYPE.MOONS:
            return [self.moonsX, self.moonsY]
        elif type == DATA_TYPE.BLOBS:
            return [self.blobsX, self.blobsY]
        else:
            raise Exception("No such dataset type.")
        
    def set_y(self, type : DATA_TYPE, y):
        if type == DATA_TYPE.CIRCLES:
            self.circlesY = y
        elif type == DATA_TYPE.MOONS:
            self.moonsY = y
        elif type == DATA_TYPE.BLOBS:
            self.blobsY = y
        else:
            raise Exception("No such dataset type.")
        
    def scale_datasets(self):
        self.circlesX, self.circlesY = Scaler.scale(self, DATA_TYPE.CIRCLES)
        self.moonsX, self.moonsY = Scaler.scale(self, DATA_TYPE.MOONS)
        self.blobsX, self.blobsY = Scaler.scale(self, DATA_TYPE.BLOBS)
        self.is_scaled = True
    
    def read_from_file(path : str):
        # Blabla
        print("read from file")
class Scaler:
    def scale(gen:Generate, type:DATA_TYPE):
        X,y = gen.get_dataset(type)
        scaler = StandardScaler().fit(X)
        X = scaler.transform(X)
        return X,y

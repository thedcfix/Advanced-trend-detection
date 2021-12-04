import numpy
from numpy.core.arrayprint import format_float_scientific
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import stockpicking_functions as sp
import classes

import time

# split an array into chunks of size=split
def splitData(data, split):

    data = numpy.array(data)
    data = data.reshape(-1, split)

    return data

# split an array into chunks of size=split up to max_days
def splitDataMaxDays(data, split, max_days):

    data = numpy.array(data)
    data = data[-max_days:]

    data = data.reshape(-1, split)

    return data

def splitAllSequences(data, split):

    queue = classes.Queue(split)
    flag = False

    for el in data:

        queue.put(el)

        if queue.isFull() and flag == True:
            res = numpy.concatenate((res, queue.get()), axis=0)
        elif queue.isFull() and flag == False:
            res = queue.get()
            flag = True
    
    return res


# divide and array by its mean
def normalize(array):

    avg = numpy.mean(array)
    res = numpy.divide(array, avg)

    return res

# create a KMeans clustering model
def createClusteringModel(n_clusters, n_init, max_iter, algorithm):

    # algorithm choice can be "auto" or "full"
    model = KMeans(n_clusters=n_clusters, n_init=n_init, max_iter=max_iter, algorithm=algorithm)

    return model

# train the KMeans clustering model
def trainModel(model, data):
    
    kmeans = model.fit(data)

    return kmeans

# find the cluster a sequence belongs to
def predict(model, record):

    return model.predict([record])

# get data about centroids
def getCentroids(model, showdata):

    centroids = []
    print("Centroids:\n")

    for el in model.cluster_centers_:
        if showdata:
            print(el, "\n")
        centroids.append(el)

    return centroids

# view centroids
def viewCentroids(model, n_cluster):

    fig = plt.figure("Trend analysis")
    i = 0

    for el in model.cluster_centers_:

        plt.subplot(int(str(n_cluster)+"1"+str(i+1)))
        plt.plot(model.cluster_centers_[i])
        i+=1

    plt.show()

# view centroids
def viewAdvancedCentroids(model, threshold):

    fig = plt.figure("Trend analysis")
    i = 0

    for el in model.cluster_centers_:
        
        var = sp.variance(el)
        if var > threshold:
            plt.plot(model.cluster_centers_[i])
        i+=1

    plt.show()
from sklearn import cluster
from matplotlib import pyplot
import numpy as np

def kMeans(data):
    k = 2
    adata=np.array(data)
    kmeans = cluster.KMeans(n_clusters=k)
    kmeans.fit(adata)

    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    for i in range(k):
        # select only data observations with cluster label == i
        ds = adata[np.where(labels==i)]
        # plot the data observations
        pyplot.plot(ds[:,0],ds[:,1],'o')
        # plot the centroids
        lines = pyplot.plot(centroids[i,0],centroids[i,1],'kx')
        # make the centroid x's bigger
        pyplot.setp(lines,ms=15.0)
        pyplot.setp(lines,mew=2.0)
    pyplot.show()

def main():
    data = []
    with open('data/tshirt.csv','r') as csvfile:
        _ = csvfile.__next__()
        for line in csvfile:
            height, weight = line.split(',')
            data.append([float(height), float(weight)])
    kMeans(data)

if __name__ == '__main__':
    main()
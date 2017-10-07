from collections import OrderedDict
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Function to get data from filepath
def getData(file):
    x = []
    y = []
    csvd = open(file, 'r')
    data = csv.reader(csvd)
    next(data)
    for er in data:
        x.append(int(er[3]))
        y.append(int(er[4]))
    ndata = list(zip(x, y))
    return ndata


# Function to manipulate the data with kmeans clusters
def Kmeans(custdata):

    # Kmeans with 5 clusters
    kmeans = KMeans(n_clusters=5)

    # Fitting the data with the model
    kmeans.fit(custdata)

    # Finding the centroids and the labels
    kcentroids = kmeans.cluster_centers_
    klabels = kmeans.labels_

    # Colors and labels
    kcolors = ["g", "y", "r", "b", "c"]
    klabel = ["C-1", "C-2", "C-3", "C-4", "C-5"]

    # Potters for the graph
    for i in range(len(custdata)):
        plt.scatter(custdata[i][0], custdata[i][1], c=kcolors[klabels[i]], label=klabel[klabels[i]])

    plt.scatter(kcentroids[:, 0], kcentroids[:, 1], label="Centroids", marker=".", s=100, linewidths=15, zorder=20)
    plt.title('Cluster of Customers')
    plt.xlabel('Annual Income(k$)')
    plt.ylabel('Spending Score(1-100)')

    # To display the graph with legends
    legendh, legendl = plt.gca().get_legend_handles_labels()
    dolabel = OrderedDict(zip(legendl, legendh))
    plt.legend(dolabel.values(), dolabel.keys())
    plt.show()


def main():
    path = "/Volumes/Sibi-CLG/PythonFall17/Python-FL17/Lab-3/Source/data/Customers.csv"
    data = getData(path)
    Kmeans(data)


if __name__ == "__main__":
    main()

import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics


# Function to split test and train data
def SplitData(bcancer):
    x = bcancer.data[:, :2]
    y = bcancer.target
    xtr, xte, ytr, yte = train_test_split(x, y, test_size=0.2)

    return xtr, xte, ytr, yte


# Function to find accuracy of data using linear kernel
def LinearKernel(xtr, xte, ytr, yte):
    svcmodel = svm.SVC()

    linearPrediction = svcmodel.set_params(kernel='linear').fit(xtr, ytr).predict(xte)

    linearAccuracy = metrics.accuracy_score(yte, linearPrediction)

    print "Linear Kernel Accuracy:", linearAccuracy


# Function to find accuracy of data using rbf kernel
def RBFKernel(xtr, xte, ytr, yte):
    svcmodel = svm.SVC()

    rbfPrediction = svcmodel.set_params(kernel='rbf').fit(xtr, ytr).predict(xte)

    rbfAccuracy = metrics.accuracy_score(yte, rbfPrediction)

    print "RBF Kernel Accuracy:", rbfAccuracy


def main():
    bcancer = datasets.load_breast_cancer()
    xtr, xte, ytr, yte = SplitData(bcancer)
    LinearKernel(xtr, xte, ytr, yte)
    RBFKernel(xtr, xte, ytr, yte)


if __name__ == "__main__":
    main()

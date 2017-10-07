import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Dataset Definition
# x-axis: Availabitliy of Doctors per 100,000 residents
# y-axis: Availability of Hospitals per 100,000 residents

# Function to get X,Y axis from an excel sheet for given columns
def getData(path, columns):
    x = []
    y = []
    # Using pandas library to extract columns from given excel file
    df = pd.read_excel(path, parse_cols=columns)
    # Appending the values to the array
    for i in df['X2']:
        x.append(i)

    for j in df['X3']:
        y.append(j)
    return x, y


# Function to get regression model
def LinearRegressionModel(a, b):

    # Converting to np array and reshaping
    x=np.array(a).reshape(-1,1)
    y=np.array(b).reshape(-1,1)

    # Using sklearn linear regression package
    lmodel = LinearRegression()

    # Fitting the data to the model
    lmodel.fit(x, y)

    # Adding points in the graph
    plt.scatter(x, y, color='g')

    # Adding prediction line int the graph
    plt.plot(x, lmodel.predict(x), color='b')
    plt.xlabel("Availabitliy of Doctors per 100,000 residents")
    plt.ylabel("Availability of Hospitals per 100,000 residents")

    # Show the graph
    plt.show()


def main():
    path = "/Volumes/Sibi-CLG/PythonFall17/Python-FL17/Lab-3/Source/data/data.xls"
    columns = "B,C"
    x, y = getData(path, columns)
    LinearRegressionModel(x, y)


if __name__ == "__main__":
    main()

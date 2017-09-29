# Gaussian Naive Bayes and Multinomial naive Bayes
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB


# Function to generate guassian naive bayes
def GuassianNaivebayes():
    print("****** GuassianNaivebayes ******")
    ds = datasets.load_iris()
    # test and train split
    data_train, data_test, target_train, target_test = train_test_split(ds.data, ds.target, test_size=0.4,
                                                                        random_state=0)
    # fit the model to the data
    model = GaussianNB()
    model.fit(data_test, target_test)
    print("****** Model ******")
    print(model)
    # make predictions
    expected = target_test
    predicted = model.predict(data_test)
    # performance evaluations
    print("****** Classification Report ******")
    print(metrics.classification_report(expected, predicted))
    print("****** Confusion Matrix ******")
    print(metrics.confusion_matrix(expected, predicted))
    print("****** Accuracy Score ******")
    print(metrics.accuracy_score(expected, predicted))
    print("****** Cohen Kappa Score ******")
    print(metrics.cohen_kappa_score(expected, predicted))


# Function to generate multinomial naive bayes
def MultinomialNaivebayes():
    print("****** MultinomialNaivebayes ******")
    ds = datasets.load_digits()
    # test and train split
    data_train, data_test, target_train, target_test = train_test_split(ds.data, ds.target, test_size=0.4,
                                                                        random_state=0)
    # fit the model to the data
    model = MultinomialNB()
    model.fit(data_test, target_test)
    print("****** Model ******")
    print(model)
    # make predictions
    expected = target_test
    predicted = model.predict(data_test)
    # performance evaluations
    print("****** Classification Report ******")
    print(metrics.classification_report(expected, predicted))
    print("****** Confusion Matrix ******")
    print(metrics.confusion_matrix(expected, predicted))
    print("****** Accuracy Score ******")
    print(metrics.accuracy_score(expected, predicted))
    print("****** Cohen Kappa Score ******")
    print(metrics.cohen_kappa_score(expected, predicted))


GuassianNaivebayes()
MultinomialNaivebayes()

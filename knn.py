# -*- coding: utf-8 -*-
"""KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h1vu21iZ1JaFWiFPXHmGtmchLPDBfCco
"""

#first import the library
import pandas as pd
from numpy import nan
import joblib
# datasert load
dataset = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
# dataset = pd.read_csv(data, names=names)
print(dataset.head()) #it prints 20 rows of data
#slicing
X_features_input = dataset.iloc[:, :-1].values #features[rows, columms]
print(X_features_input)
y_label_output = dataset.iloc[:, 4].values #labels
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_features_input, y_label_output, test_size=0.20, random_state=5)
#x_train = 80% of our features data(input)
#x_test = 20% of our features data(input)
#y_train = 80% of our lable data(output)
#y_test = 20 % of pur lable data(output)
#imported the algorithms from library
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
# to train the model you have to use the function of "fit()"
# while traininf we only pass the 80 percent of our data
classifier.fit(X_train, y_train) # X_train = features #y_train= lable
# now we have to take prediction on testing data
y_pred = classifier.predict(X_test) #here we only pass the features
filename = 'knn_model.sav'
joblib.dump(classifier, 'knn_model.sav')
 
# some time later...
 
# load the model from disk
loaded_model = joblib.load('knn_model.sav')
print('Accuracy of loaded model')
result = loaded_model.score(X_test, y_test)
print(result)


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(y_pred)
from sklearn.metrics import accuracy_score
print('Accuracy Score: ', accuracy_score(y_pred, y_test)) #y_pred is the output

from sklearn.metrics import f1_score
f1_metric = f1_score(y_test, y_pred, average='macro')
print("f1 score macro:", f1_metric)

from sklearn.metrics import f1_score
f1_metric_micro = f1_score(y_test, y_pred, average='micro')
print("f1 score micro:",f1_metric_micro)




#take input from the loaded model
input_sepal_length = float(input("Enter sepal length: "))
input_sepal_width = float(input("Enter sepal width:"))
input_petal_length = float(input("Enter petal Length: "))
input_petal_width = float(input("Enter petal width: "))
output = loaded_model.predict([[input_sepal_length, input_sepal_width,input_petal_length,input_petal_width ]])
print(output)
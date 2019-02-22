from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

#[height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

#Decision tree Classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict([[190, 70, 43]])
print(prediction)

#Random Forest Classifier
clf2 = RandomForestClassifier(n_estimators=2)
clf2 = clf2.fit(X,Y)
prediction = clf2.predict([[190, 70, 43]])
print(prediction)

#Kneighbors Classifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, Y)
prediction = neigh.predict([[190, 70, 43]])
print (prediction)

#Logistic Regression
clf3 = LogisticRegression()
clf3.fit(X,Y)
predicfrom sknn.mlp import Classifier, Layer
        import numpy as nption = clf3.predict([[190,70,43]])
print(prediction)

#Naive Bayes
clf4 = GaussianNB()
clf4 = clf4.fit(X,Y)
prediction = clf4.predict([[190,70,43]])
print(prediction)
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import tree\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.naive_bayes import GaussianNB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "#[height, weight, shoe size]\n",
    "X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],\n",
    "     [190, 90, 47], [175, 64, 39],\n",
    "     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]\n",
    "Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',\n",
    "     'female', 'male', 'male']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['male']\n"
     ]
    }
   ],
   "source": [
    "clf = tree.DecisionTreeClassifier()\n",
    "clf = clf.fit(X,Y)\n",
    "prediction = clf.predict([[190, 70, 43]])\n",
    "print(prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['male']\n"
     ]
    }
   ],
   "source": [
    "clf2 = RandomForestClassifier(n_estimators=2)\n",
    "clf2 = clf2.fit(X,Y)\n",
    "prediction = clf2.predict([[190, 70, 43]])\n",
    "print(prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['male']\n"
     ]
    }
   ],
   "source": [
    "neigh = KNeighborsClassifier(n_neighbors=3)\n",
    "neigh.fit(X, Y)\n",
    "prediction = neigh.predict([[190, 70, 43]])\n",
    "print (prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['female']\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Shivam\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:433: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",
      "  FutureWarning)\n"
     ]
    }
   ],
   "source": [
    "clf3 = LogisticRegression()\n",
    "clf3.fit(X,Y)\n",
    "predicfrom sknn.mlp import Classifier, Layer\n",
    "        import numpy as nption = clf3.predict([[190,70,43]])\n",
    "print(prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['male']\n"
     ]
    }
   ],
   "source": [
    "clf4 = GaussianNB()\n",
    "clf4 = clf4.fit(X,Y)\n",
    "prediction = clf4.predict([[190,70,43]])\n",
    "print(prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

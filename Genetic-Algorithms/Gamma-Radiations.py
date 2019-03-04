#!pip install TPOT
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#loading the data
telescope=pd.read_csv('MAGIC Gamma Telescope Data.csv')

#shuffle the data
telescope_shuffle=telescope.iloc[np.random.permutation(len(telescope))]
tele = telescope_shuffle.reset_index(drop = True)

#storing 2 classes
tele['Class']=tele['Class'].map({'g':0, 'h':1})
tele_class = tele['Class'].values

#split into training and testing data
training_indices, validation_indices = training_indices, testing_indices = train_test_split ( tele.index, stratify = tele_class, train_size= 0.75, test_size = 0.25)

#finding best model using genetic programming
tpot = TPOTClassifier(generations =5, verbosity = 2)
tpot.fit(tele.drop('Class', axis = 1).loc[training_indices].values, tele.loc[training_indices, 'Class'].values)

#score the accuracy
tpot.score(tele.drop('Class', axis=1).loc[validation_indices].values. tele.loc[validation_indices, 'Class'].values)

tpot.export('pipeline.py')

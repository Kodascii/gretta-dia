import pandas as pd
import numpy as np
import pickle

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris_df = pd.read_csv('iris.csv')
classes = ['Setosa', 'Versicolor', 'Virginica']

X = iris_df.drop('variety', axis=1)
y = iris_df[['variety']].replace(classes, [0, 1, 2])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
y_train = np.ravel(y_train)

iris_model = KNeighborsClassifier(n_neighbors=3)
iris_model.fit(X_train.values, y_train)

# Serialize the model to a file using pickle
with open('iris_model.pkl', 'wb') as model_file:
    pickle.dump(iris_model, model_file)
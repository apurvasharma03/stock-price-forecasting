import quandl
import pandas as pd
import numpy as np
import datetime

from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

df = quandl.get("WIKI/AMZN")

df = df[['Adj. Close']]

forecast_out = int(60) # predicting 30 days into future
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out) #  label column with data shifted 30 units up

X = np.array(df.drop(['Prediction'], 1))
X = preprocessing.scale(X)

X_forecast = X[-forecast_out:] # set X_forecast equal to last 30
X = X[:-forecast_out] # remove last 30 from X

y = np.array(df['Prediction'])
y = y[:-forecast_out]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# Training
clf = linear_model.LinearRegression()
clf.fit(X_train,y_train)
# Testing
confidence = clf.score(X_test, y_test)
print("confidence: ", confidence)

forecast_prediction = clf.predict(X_forecast)
print(forecast_prediction)

plt.scatter(X_test, y_test, color="black")
#plt.plot(X_test, y_train, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
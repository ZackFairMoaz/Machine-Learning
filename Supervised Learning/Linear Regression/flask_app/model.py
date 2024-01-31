import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pickle
import os
from app import app 

def train():
    df = pd.read_csv('Salary_Data.csv')

    X = df.iloc[:,:1]
    y = df.iloc[:,1:]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    scalar = MinMaxScaler()
    y_scaled_train = scalar.fit_transform(y_train)
    y_scaled_test = scalar.transform(y_test)

    model = LinearRegression()
    model.fit(X_train, y_scaled_train)
    pred = model.predict(X_test)
    pred = scalar.inverse_transform(pred)

    filename = 'Regression_Model.sav'
    pickle.dump(model, open(filename, 'wb'))

    static_dir = os.path.join(app.root_path, 'static')
    plt.scatter(X_train, scalar.inverse_transform(y_scaled_train), color='green')
    plt.plot(X_test, pred, color='red')
    plt.title('Salary as per experience')
    plt.xlabel("Experience in Years")
    plt.ylabel("Salary in USD")
    plt.legend(['Prediction', 'Train'])
    plt.box(False)
    plt.savefig(os.path.join(static_dir, 'linear_regression_plot.jpg'))

if __name__ == '__main__':
    train()
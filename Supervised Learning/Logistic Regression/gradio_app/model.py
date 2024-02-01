import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pickle

def train():
    df = pd.read_csv('heart.csv')

    X = df.drop('target',axis=1)
    Y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    pickle.dump(model, open('Regression_Model.sav', 'wb'))
    pickle.dump(scaler, open('scaler.pkl', 'wb'))

if __name__ == '__main__':
    train()
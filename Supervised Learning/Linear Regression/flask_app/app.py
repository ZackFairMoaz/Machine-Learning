from flask import Flask, request, render_template
from sklearn.preprocessing import MinMaxScaler
import pickle
import numpy as np
import pandas as pd
# import model

app = Flask(__name__, template_folder='Template', static_url_path='/static', static_folder='static')
scaler = MinMaxScaler()

# Fit the scaler to the entire target variable
df = pd.read_csv('Salary_Data.csv')
y = df.iloc[:, 1:]
scaler.fit(y)


@app.route("/")
def home():
    return render_template("home.html")

def ValuePredictor(to_predict):
    to_predict = np.array(to_predict).reshape(1, -1)
    result = model.predict(to_predict)
    return result[0]

@app.route("/", methods=["GET","POST"])
def result():
    if request.method == 'POST':
        years_of_experience = float(request.form['Years'])
        to_predict = np.array([years_of_experience]).reshape(1, -1)
        pred = float(ValuePredictor(to_predict))
        result = scaler.inverse_transform([[pred]])
        result = round(result[0][0], 2)
        return render_template("home.html", result=int(result))


if __name__ == '__main__':
    # model.train()
    model = pickle.load(open('Regression_Model.sav', 'rb'))
    app.run(host='0.0.0.0', port=5000)
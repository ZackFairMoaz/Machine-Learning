# Logistic Regression Heart Attack Prediction App

## Introduction

This project implements an intuitive and user-friendly web application made with Gradio that utilizes logistic regression to provide predictions of Heart attack possibility based on certain key factors relating to ones health.

The dataset, heart.csv, consists of 14 columns:

1. Age
2. Sex
3. Chest pain type (4 values)
4. Resting blood pressure
5. Serum cholestoral in mg/dl
6. Fasting blood sugar > 120 mg/dl
7. Resting electrocardiographic results (values 0,1,2)
8. Maximum heart rate achieved
9. Exercise induced angina
10. Oldpeak = ST depression induced by exercise relative to rest
11. The slope of the peak exercise ST segment
12. Number of major vessels (0-3) colored by flourosopy
13. Thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
14. Target: 0 = less chance of heart attack 1 = more chance of heart attack

Dataset is taken for learning purpose. Source of the data : https://archive.ics.uci.edu/ml/datasets/Heart+Disease

## What is Logistic Regression

Logistic regression is a data analysis technique that uses mathematics to find the relationships between two data factors. It then uses this relationship to predict the value of one of those factors based on the other. The prediction usually has a finite number of outcomes, like yes or no.

In mathematics as the equation between x and y. The logit function maps y as a sigmoid function of x.

In many cases, multiple explanatory variables affect the value of the dependent variable. To model such input datasets, logistic regression formulas assume a linear relationship between the different independent variables. You can modify the sigmoid function and compute the final output variable as 

y = f(β0 + β1x1 + β2x2+… βnxn)

The symbol β represents the regression coefficient. The logit model can reverse calculate these coefficient values when you give it a sufficiently large experimental dataset with known values of both dependent and independent variables. 

## Types of Logistic Regression

* Binary logistic regression: Works well for binary classification problems that have only two possible outcome (0-1 / Yes-No)
* Multinomial logistic regression: Analyzes problems that have several possible outcomes as long as the number of outcomes is finite (25%, 50%, 75%, 100%)
* Ordinal logistic regression: ordered logit model, is a special type of multinomial regression for problems in which numbers represent ranks rather than actual values (rank your service as poor, fair, good, or excellent)

## Notebook Section

### Prerequisites

* Notebook and Dataset: Download the ***Heart_attack_prediction.ipynb*** and ***heart.csv***

* Python Environment: Make sure you have Python3 installed on your system. You can download it from https://www.python.org/downloads/.

* Open the notebook in VSCode and use the Jupyter extension to run cells. Optionally, you can use Jupyter Notebook as well

* Libraries: Install the required Python libraries using the following commands:

```bash
pip install pandas
pip install matplotlib
pip install seaborn
pip install scikit-learn
```

### Dataset Exploration

The dataset is explored using the Jupyter Notebook Heart_attack_prediction.ipynb. The notebook includes:

* Reading and loading the dataset.
* Displaying information and summary statistics of the dataset.

### Model Training and Evaluation

The notebook further explores the linear regression model for predicting salaries. Key steps include:

* Splitting the dataset into training and testing sets.
* Scaling the X labels using Standard scaling.
* Building and training the logistic regression model.
* Evaluating the model's performance using metrics such as accuracy.
* Saving the trained model as Regression_Model.sav using the pickle library for inference.
* Saving the scaler used for scaling as scaler.pkl for consistent preprocessing during inference.

## Gradio App Section

### Get Started Locally

To get started locally all you need is gradio which you can install in python using

```bash
pip install gradio
```

Gradio is an open-source Python library designed for fast and straightforward UI generation for machine learning models. It allows developers to create interactive and customizable user interfaces without extensive coding. Gradio supports a wide range of input components, making it easy to integrate with various model types, and it provides a seamless way to deploy machine learning models for real-time inference with minimal effort.

### Running Gradio App

1. Download the 'gradio_app' folder from the repository or clone the repo with

   ```sh
   git clone https://github.com/ZackFairMoaz/Machine-Learning.git
   ```

> [!NOTE]
> To download a folder from GitHub, navigate to your desired repository, select the folder you want to download from GitHub, copy the URL, navigate to https://download-directory.github.io/ and paste the URL into the text box, and hit enter.

2. Open a terminal or command prompt.
3. Navigate to the 'gradio_app' folder.
4. Run the following command to run local server:

```bash
python app.py
```
5. Once the Gradio app is up and running, you should see a link to local host, use CTRL+Click to open, alternatively you can run the url mentioned below in your web browser

## Usage

Access the application by running the script file and opening a web browser to navigate to http://127.0.0.1:7860.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Your insights and improvements are highly appreciated.

## License

[MIT](https://choosealicense.com/licenses/mit/)



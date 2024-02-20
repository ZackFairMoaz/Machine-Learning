# Linear Regression Salary Prediction App

## Introduction

This project implements an intuitive and user-friendly web application that utilizes linear regression to provide accurate salary predictions based on an individual's years of professional experience.

The dataset, Salary_Data.csv, consists of two columns: "YearsExperience" and "Salary,"

## What is Linear Regression

Linear regression is a data analysis technique that predicts the value of unknown data by using another related and known data value. It mathematically models the unknown or dependent variable and the known or independent variable as a linear equation. For instance, suppose that you have data about your expenses and income for last year. Linear regression techniques analyze this data and determine that your expenses are half your income. They then calculate an unknown future expense by halving a future known income.

At its core, a simple linear regression technique attempts to plot a line graph between two data variables, x and y. As the independent variable, x is plotted along the horizontal axis. Independent variables are also called explanatory variables or predictor variables. The dependent variable, y, is plotted on the vertical axis. You can also refer to y values as response variables or predicted variables.

### Steps in linear regression

For this overview, consider the simplest form of the line graph equation between y and x; y=c*x+m, where c and m are constant for all possible values of x and y. So, for example, suppose that the input dataset for (x,y) was (1,5), (2,8), and (3,11). To identify the linear regression method, you would take the following steps:

* Plot a straight line, and measure the correlation between 1 and 5.
* Keep changing the direction of the straight line for new values (2,8) and (3,11) until all values fit.
* Identify the linear regression equation as y=3*x+2.
* Extrapolate or predict that y is 14 when x is

### Types of Linear Regression

* Simple linear regression: Y= β0*X + β1 + ε
* Multiple linear regression: Y= β0*X0 + β1X1 + β2X2+…… βnXn+ ε
* Logistic regression:  Use logarithmic functions to compute the regression line iwth a prediction being a value between 0 and 1

Where β0 and β1 are two unknown constants representing the regression slope, whereas ε (epsilon) is the error term.

## Notebook Section

### Prerequisites

* Notebook and Dataset: Download the ***Salary_Prediction_Exploration.ipynb*** and ***Salary_Data.csv***

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

The dataset is explored using the Jupyter Notebook Salary_Prediction_Exploration.ipynb. The notebook includes:

* Reading and loading the dataset.
* Displaying information and summary statistics of the dataset.
* Visualizing the distribution of salaries.
* Plotting a scatter plot to visualize the correlation between years of experience and salary.

### Model Training and Evaluation

The notebook further explores the linear regression model for predicting salaries. Key steps include:

* Splitting the dataset into training and testing sets.
* Scaling the target variable using Min-Max scaling.
* Building and training the linear regression model.
* Evaluating the model's performance using Root Mean Squared Error and visualizing predictions.
* Saving the trained model as Regression_Model.sav using the pickle library for inference.

## Flask App Section

### Get Started Locally

To get started locally all you need is docker which you can download from https://www.docker.com/

Docker is a platform that allows developers to package, distribute, and run applications in containers. Containers are lightweight, portable, and isolated environments that encapsulate everything needed to run an application, including code, runtime, system tools, libraries, and settings. Docker simplifies the process of building, shipping, and deploying applications by providing a consistent environment across different systems, making it easier to develop and deploy software in various environments, from development to production

### Creating Docker Image

1. Download the 'flask_app' folder from the repository or clone the repo with

   ```sh
   git clone https://github.com/ZackFairMoaz/Machine-Learning.git
   ```

> [!NOTE]
> To download a folder from GitHub, navigate to your desired repository, select the folder you want to download from GitHub, copy the URL, navigate to https://download-directory.github.io/ and paste the URL into the text box, and hit enter.

2. Open a terminal or command prompt.
3. Navigate to the 'flask_app' folder.
4. Run the following command to build the Docker image:

```bash
docker build -t <name> .
```
5. Once the Docker image is built, run the following command to start the Docker container:

```bash
docker run -p 5000:5000 --rm <name>
```

> [!NOTE]
> * ***docker build*** is a command to build a Docker image.
> * ***-t*** flag is used to tag the image with a name and optionally a tag.
> * ***name*** is placeholder name of the image which can be customized to preference.
> * ***.*** period represents the build context. It tells Docker to use the current directory as the build context.
> * ***'docker run'*** is a command used in Docker to create and start a new container based on a specified image.
> * ***rm*** flag helps delete the container immediately after it exits.
> * ***-p 5000:5000:*** flag maps port 5000 from the Docker container to port 5000 on the host machine.

## Usage

Access the application by running the image in a container and opening a web browser to navigate to http://127.0.0.1:5000.

(Optionally, you can un-comment the model.train() line in app.py to train the model whenever the app starts)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Your insights and improvements are highly appreciated.

## License

[MIT](https://choosealicense.com/licenses/mit/)



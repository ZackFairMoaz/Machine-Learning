# Linear Regression Salary Prediction App

## Getting Started

This project implements a simple web application for predicting salary based on years of experience using linear regression.

### Prerequisites

To get started locally all you need is docker which you can download from https://www.docker.com/

## Creating Docker Image

1. Download the 'flask_app' folder from the repository.
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

Note

* name is placeholder name of the image which can be customized to preference
* rm command helps delete the container immediately after it exits

## Usage

Access the application by opening a web browser and navigating to http://127.0.0.1:5000.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)



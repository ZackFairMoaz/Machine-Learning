## Usage

Download the flask_app folder from the repository.
Open a terminal or command prompt.
Navigate to the flask_app folder.
Run the following command to build the Docker image:

docker build -t <image_name> .

Once the Docker image is built, run the following command to start the Docker container:

docker run -p 5000:5000 <image_name>

Access the application by opening a web browser and navigating to http://127.0.0.1:5000.
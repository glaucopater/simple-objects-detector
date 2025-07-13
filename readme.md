## Object Detection Web Application

This project is a web-based object detection application that uses deep learning models to identify objects in images. The application allows users to input a URL of an image, and it will detect and highlight the objects present in the image.

**Features**

* Object detection using deep learning models
* Image processing and analysis
* Web-based interface for user input and output
* Support for multiple image formats

**Technical Details**

* The application uses the Hugging Face Transformers library to load pre-trained object detection models.
* The `product_detector.py` file contains the object detection logic, which uses the `DetrImageProcessor` and `DetrForObjectDetection` classes to process images and detect objects.
* The `web_app.py` file contains the Flask web application code, which handles user input and output, and interfaces with the object detection logic.
* The `templates` directory contains the HTML templates for the web application's user interface.

**Requirements**

* Python 3.7+
* Flask 3.1.1+
* Hugging Face Transformers 4.53.0+
* Torch 2.7.1+
* Torchvision 0.22.1+
* Other dependencies listed in `requirements.txt`

**Usage**

Conda or VirtualEnv are suggested

## VirtualEnv setup

1. Clone the repository 
2. Switch to a conda or virtual env:

- python -m venv venv...
- source ./venv/bin/activate or in Windows source .\venv\Scripts\activate

and install the dependencies using `pip install -r requirements.txt`.

3. Run the web application using `python web_app.py`.
4. Open a web browser and navigate to `http://localhost:5000`.
5. Input a URL of an image and click the "Run Detection" button to detect objects in the image.

## Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t object-detector .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 object-detector
   ```
3. Open a web browser and navigate to `http://localhost:5000`.

## Docker Compose Setup

1. Make sure you have Docker Compose installed.
2. Run the following command to build and start the service:
   ```bash
   docker-compose up
   ```
3. Open a web browser and navigate to `http://localhost:5000`.

**Note:** The first time you run this, it will download the object detection model, which may take some time. Subsequent runs will be much faster as the model is cached in a Docker volume.



**License**

This project is licensed under the MIT License. See `LICENSE` for details.

Please let me know if you'd like me to modify or add to this draft!
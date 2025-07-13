 # Simple Object Detector

This project is a web-based object detection application that uses the `facebook/detr-resnet-50` model from Hugging Face to identify objects in images. The application provides a user-friendly interface to enter an image URL, view the detected objects with bounding boxes, and see the analysis results in JSON format.


![Demo](/public/demo.png)


## Features

*   **CORS Handling:** Uses a backend proxy to bypass CORS errors when fetching images from external URLs.
*   **Object Detection:** Utilizes a pre-trained DETR model for accurate object detection.
*   **Web Interface:** A clean and modern UI for easy interaction.
*   **Image Validation:** Both frontend and backend validation to ensure valid image URLs are processed.
*   **Result Persistence:** Saves the analysis results, including the original URL, file type, and a SHA256 hash of the image, to a `results` directory.
*   **Dockerized:** Comes with `Dockerfile` and `docker-compose.yml` for easy setup and deployment.
*   **Model Caching:** Caches the downloaded Hugging Face model to a Docker volume for faster startup on subsequent runs.
*   **Dependency Caching:** Caches pip packages to a Docker volume to speed up the build process.

## Technical Details

*   **Backend:** Flask
*   **Frontend:** HTML, CSS, JavaScript
*   **Object Detection:** Hugging Face Transformers, PyTorch
*   **Containerization:** Docker, Docker Compose

## Getting Started

### Prerequisites

*   Docker
*   Docker Compose

### Running the Application

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd simple-objects-detector
    ```

2.  **Run with Docker Compose:**

    ```bash
    docker-compose up --build
    ```

3.  **Access the application:**

    Open your web browser and navigate to `http://localhost:5000`.

**Note:** The first time you run the application, it will download the object detection model, which may take some time. Subsequent runs will be much faster as the model is cached in a Docker volume.

## Usage

1.  Enter the URL of an image in the input field.
2.  Click the "Run Detection" button.
3.  The image will be displayed with bounding boxes around the detected objects.
4.  The JSON output below the image will show the detailed analysis results.
5.  The analysis results will also be saved as a JSON file in the `results` directory.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

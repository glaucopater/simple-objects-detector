from flask import Flask, request, jsonify, render_template
import torch
import torchvision
import torchvision.transforms as transforms
from object_detector import ObjectDetector
import json
import os
from datetime import datetime
import requests
import hashlib

app = Flask(__name__)

# Define the routes for the APP


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data['url']

    # Validate the URL
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        content_type = response.headers.get('content-type')
        if not content_type or not content_type.startswith('image/'):
            return jsonify({"error": "The provided URL is not an image."}), 400
        
        # Get the image content
        image_content = response.content
        # Hash the image content
        sha256_hash = hashlib.sha256(image_content).hexdigest()

    except requests.RequestException as e:
        return jsonify({"error": f"Error fetching URL: {e}"}), 400

    detector = ObjectDetector()
    detection_response = detector.run_detection(url)

    # Add additional fields to the response
    detection_response['original_url'] = url
    detection_response['file_type'] = content_type
    detection_response['file_hash'] = sha256_hash

    print(detection_response)

    # Save the response to a file
    if not os.path.exists('results'):
        os.makedirs('results')
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"results/analysis_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(detection_response, f, indent=4)

    return jsonify(detection_response)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
import torch
import torchvision
import torchvision.transforms as transforms
from product_detector import ObjectDetector


app = Flask(__name__)

# Define the routes for the APP


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    detector = ObjectDetector()
    data = request.get_json()
    url = data['url']
    response = detector.run_detection(url)
    print(response)

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

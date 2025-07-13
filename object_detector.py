from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests
import time


class ObjectDetector:
    def __init__(self, model_name="facebook/detr-resnet-50", revision="no_timm"):
        self.device = torch.device(
            "cuda:0" if torch.cuda.is_available() else "cpu")
        print(self.device)
        self.processor = DetrImageProcessor.from_pretrained(
            model_name, revision=revision)
        self.model = DetrForObjectDetection.from_pretrained(
            model_name, revision=revision)

    def load_image(self, url):
        return Image.open(requests.get(url, stream=True).raw)

    def detect_objects(self, image, threshold=0.9):
        inputs = self.processor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        target_sizes = torch.tensor([image.size[::-1]])  # (height, width)
        results = self.processor.post_process_object_detection(
            outputs, target_sizes=target_sizes, threshold=threshold
        )
        return results

    def print_detected_objects(self, results):
        scores = results[0]["scores"].to(self.device)
        labels = results[0]["labels"].to(self.device)
        boxes = results[0]["boxes"].to(self.device)
        for score, label, box in zip(scores, labels, boxes):
            box = [round(i, 2) for i in box.tolist()]
            print(
                f"Detected {self.model.config.id2label[label.item()]} with confidence "
                f"{round(score.item(), 3)} at location {box}"
            )

    def print_detected_objects_json(self, results):
        scores = results[0]["scores"].to(self.device)
        labels = results[0]["labels"].to(self.device)
        boxes = results[0]["boxes"].to(self.device)
        detected_objects = []
        for score, label, box in zip(scores, labels, boxes):
            box = [round(i, 2) for i in box.tolist()]
            detected_object = {
                "label": self.model.config.id2label[label.item()],
                "confidence": round(score.item(), 3),
                "location": box
            }
            detected_objects.append(detected_object)
        return detected_objects

    def run_detection(self, url, threshold=0.9):
        print("Running detection...")
        start_time = time.time()
        image = self.load_image(url)
        results = self.detect_objects(image, threshold=threshold)
        execution_time = time.time() - start_time
        detected_objects = self.print_detected_objects_json(results)

        output = {
            "detected_objects": detected_objects,
            "execution_time": round(execution_time, 2)
        }

        return output


# Usage
# detector = ObjectDetector()
# url = "https://plus.unsplash.com/premium_photo-1750757386362-247b8407a0f3?q=80&w=772&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
# detector.run_detection(url)

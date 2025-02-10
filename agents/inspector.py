import os
from ultralytics import YOLO

class Inspector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")  # Load the YOLOv8 model

    def analyze_images(self, image_path):
        """Check if image exists before analysis and process YOLOv8 results properly."""
        if not os.path.exists(image_path):
            print(f"❌ Error: {image_path} not found! Using a default image.")
            image_path = "default_image.jpg"  # Set a fallback image
        
        results = self.model(image_path)  # Runs inference
        detections = results[0]  # Get the first result object

        # Extract detected objects
        if len(detections.boxes) > 0:
            detected_objects = [self.model.names[int(box.cls)] for box in detections.boxes]
            return f"🚨 Damage Detected: {', '.join(detected_objects)}"
        
        return "✅ No issues detected."

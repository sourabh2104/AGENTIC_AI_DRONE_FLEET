import torch
from ultralytics import YOLO

class AnomalyDetector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)  # Load pre-trained YOLOv8 model

    def detect_anomalies(self, image_path):
        """Analyzes images and detects potential hazards."""
        results = self.model(image_path)
        detected_objects = results[0].names  # Extract detected classes
        
        hazards = [obj for obj in detected_objects if obj in ["crack", "leak", "obstacle"]]
        
        if hazards:
            return f"⚠️ Anomalies Detected: {', '.join(hazards)}. Rerouting drones..."
        return "✅ No hazards detected. Continuing mission."

import os
import cv2
import json
import numpy as np
from ultralytics import YOLO
from pyzbar.pyzbar import decode
from PIL import Image

os.environ["WANDB_MODE"] = "disabled"
os.environ["WANDB_SILENT"] = "true"

# Load your trained model weights
model = YOLO("/content/drive/MyDrive/1pharma/runs/detect/qr_detection3/weights/best.pt")

def process_image(image_path, model):
    image_id = os.path.splitext(os.path.basename(image_path))[0]
    img = cv2.imread(image_path)
    results = model(img)
    # Detections
    detections = results[0].boxes.xyxy.cpu().numpy() # xmin, ymin, xmax, ymax
    qrs = []
    for box in detections:
        x1, y1, x2, y2 = box[:4]
        # Crop QR region
        crop = img[int(y1):int(y2), int(x1):int(x2)]
        # Decode QR using pyzbar
        decoded_objects = decode(Image.fromarray(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)))
        value = decoded_objects[0].data.decode('utf-8') if decoded_objects else "UNKNOWN"
        qrs.append({
            "bbox": [int(x1), int(y1), int(x2), int(y2)],
            "value": value
        })
    return {"image_id": image_id, "qrs": qrs}

def save_json(result, output_file):
    with open(output_file, "w") as f:
        json.dump(result, f, indent=2, separators=(',', ': '))
    print(f"JSON saved to {output_file}")

# Example usage
image_path = "/content/drive/MyDrive/1pharma/Testclrimages/img202.jpg" #provide the path
result = process_image(image_path, model)
output_file = f"{os.path.splitext(os.path.basename(image_path))[0]}.json"
save_json(result, output_file)
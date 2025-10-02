import os
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# Disable Weights & Biases logging if unwanted
os.environ['WANDB_MODE'] = 'disabled'
os.environ['WANDB_SILENT'] = 'true'

from ultralytics import YOLO

# Model initialization
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data="data.yaml",  # Path to your dataset YAML
    epochs=25,
    imgsz=640,
    batch=32,
    name="qrdetection"
)


# Validation
metrics = model.val(data="data.yaml", imgsz=640, batch=16)
print(metrics)
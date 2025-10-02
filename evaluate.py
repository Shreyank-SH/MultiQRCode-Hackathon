import os
from ultralytics import YOLO

os.environ["WANDB_MODE"] = "disabled"
os.environ["WANDB_SILENT"] = "true"

model = YOLO("/content/drive/MyDrive/1pharma/runs/detect/qr_detection3/weights/best.pt") # best.pt path

results = model.predict(
    source="/content/drive/MyDrive/1pharma/Testclrimages",  # path to your test images
    imgsz=640,              
    conf=0.35,              # confidence threshold
    save=True               # save output results
)

# Optionally: print out summary statistics
for r in results:
    print(r)

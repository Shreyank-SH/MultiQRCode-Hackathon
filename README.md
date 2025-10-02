# MultiQRCode-Hackathon
---
All training and validation results are saved in the respective folders named `training results` and `validation results` in the project directory.

## Data Preprocessing

Data preprocessing for this project was done manually using **Roboflow**:

1. **Sign Up & Project Creation**  
   Register at [roboflow.com](https://roboflow.com/) and create a new Object Detection project.

2. **Image Upload**  
   Upload **200 raw images** containing QR codes.

3. **Annotation**  
   Draw bounding boxes around each QR code in every image.

4. **Preprocessing Applied**
   - Auto-Orient: 
   - Resize: Images stretched to **640x640 pixels**

5. **Augmentations Applied**
   - Flip: Horizontal, **50% chance**  
   - Rotation: Between **-15° and +15°**  
   - Brightness: Between **-8% and +8%**  
   - Blur: Up to **0.2px**

6. **Output**  
   Each original image was augmented to create **3 total versions**  
   (200 original images → **582 augmented images**) for the train set.

7. **Export**  
   Dataset exported in **YOLO v8 format** (bounding box labels compatible with YOLO).

**Dataset Link:** [Roboflow Project](https://app.roboflow.com/1pharma/annotation-k7xrm/3)

---

## Quick Steps

1. Annotate images as described above in Roboflow.  
2. Apply preprocessing and augmentation configurations.  
3. Export dataset as **YOLO v8 (ZIP)**.  
4. Extract images and labels for local training.  

🔗 [Quick Steps Reference](https://github.com/Dhyanms/multiqr-hackathon/tree/main#quick-steps-1)

---

## Output Format

Both annotation and training use **YOLO format label files**:

0 0.342 0.487 0.123 0.156

0 0.678 0.234 0.098 0.134


**Format:**  
<class_id> <x_center> <y_center> < width> < height>
---

## Installation

- Clone this repository:
git clone https://github.com/Shreyank-SH/MultiQRCode-Hackathon.git
cd MultiQRCode-Hackathon

text
- Ensure Python 3.8+ is installed.
- Install requirements (add your actual requirements if needed):
pip install -r requirements.txt

- Download and extract the Roboflow-exported dataset into the `data/` directory.

## Training

- Modify YOLO model config as needed (e.g., image size, batch size).
- Example training command:
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640

- Monitor training output for metrics like mAP and loss.
- All training and validation results are saved in the respective folders named `training results` and `validation results` in the project directory.

## Results

| Class | Images | Instances | Box(P) | R | mAP50 | mAP50-95 |
|-------|--------|-----------|--------|---|-------|----------|
| all   | 582    | 2437      | 0.967  |0.946 | 0.988 | 0.833  |


## Inference

For inference, simply run the code by changing the image path. A JSON file containing the detection results will be generated and downloaded automatically.

## Limitations

- Limited dataset size (582 training images after augmentation).
- Performance depends on quality and variety of annotated data.
- May have challenges with very small or overlapping QR codes.

## Challenges Faced

- Manual annotation was time-consuming.
- Maintaining consistent augmentation settings for realistic variability.
- Balancing augmentation to avoid overfitting or underfitting.

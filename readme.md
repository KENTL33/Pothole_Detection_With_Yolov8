# pothole_detection_with_yolov8
Real-time pothole detection using YOLOv8 trained on custom dataset.

## 🚀 Live Demo
**Try the model instantly in your browser:**
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/KENTL33/pothole-detector)
[**Click here to visit the Pothole Detector App**](https://huggingface.co/spaces/KENTL33/pothole-detector)

## Google Colab File 
You can access the YOLOv8 segmentation and tracking implementation via the Google Colab link provided below.

[`Google Colab File`](https://colab.research.google.com/drive/1OCq7GHOmr_8IiW2Xx4A1A0sjzaxuqWC7?usp=sharing)

<h2>Clone the repository</h2>

```bash
!git clone https://github.com/KENTL33/pothole_detection_with_yolov8.git
```
<h2>Go to the cloned folder</h2>

```bash
cd pothole_detection_with_yolov8
```
<h2>Install the Dependencies</h2>

```bash
!pip install -r requirements.txt
```
<h2>Importing YOLO and a roboflow workspace for Image Segmentation</h2>

```python
from roboflow import Roboflow
rf = Roboflow(api_key="{the api key}")
project = rf.workspace("{name of workspace}").project("name-of-project")
dataset = project.version(1).download("yolov8")
```

<h2>Pothole dataset</h2>

[`Roboflow Workspace`](https://universe.roboflow.com/hiteshram/object-detection-bounding-box-ftfs5/dataset/1)

Run the code with mentioned command below.
- For training the data
```python
!yolo task=detect mode=train model=yolov8m.pt data={dataset.location}/data.yaml epochs={number of epochs} imgsz=640
```
- For yolov8 segmentation + Tracking & prediction
```python
!yolo task=detect mode=predict model={HOME}/runs/detect/train/weights/best.pt conf=0.25 source='/content/drive/MyDrive/demo.mp4'
```

<h2>Acknowledgements</h2>

<p>This project uses YOLOv8 for pothole detection. Special thanks to the following resources:</p>
<ul>
  <li>
    <strong>Reference Code:</strong> 
    <a href="https://github.com/mounishvatti/pothole_detection_yolov8/blob/main/PotholeDetectionUsingYOLO.ipynb">Pothole Detection using YOLOv8</a> by mounishvatti.
  </li>
  <li>
    <strong>Dataset:</strong> 
    <a href="https://universe.roboflow.com/hiteshram/object-detection-bounding-box-ftfs5/dataset/1">Roboflow Universe</a>
  </li>
</ul>

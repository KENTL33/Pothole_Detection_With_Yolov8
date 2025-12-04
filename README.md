# Pothole_Detection_With_Yolov8
Real-time pothole detection using YOLOv8 trained on custom dataset.

## Google Colab File 
You can access the YOLOv8 segmentation and tracking implementation via the Google Colab link provided below.

[`Google Colab File`](https://colab.research.google.com/drive/1OCq7GHOmr_8IiW2Xx4A1A0sjzaxuqWC7?usp=sharing)

<h2>Clone the repository</h2>

```bash
!git clone https://github.com/KENTL33/Pothole_Detection_With_Yolov8.git
```
<h2>Go to the cloned folder</h2>

```bash
cd Pothole_Detection_With_Yolov8
```
<h2>Install the Dependencies</h2>

```bash
!pip install ultralytics
```
```bash
!pip install roboflow
```
```bash
!pip install fastapi kaleido python_multipart uvicorn
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

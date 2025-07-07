import cv2 
from ultralytics import YOLO, ASSETS
from roboflow import Roboflow

# Perform object detection on image
rf = Roboflow(api_key="oNzWc2457obhugStsE8V")
project = rf.workspace("tunku-abdul-rahman-university-of-management-and-technology-ttt1n").project("wood-defects-8lcdv")
version = project.version(7)
dataset = version.download("yolov11")

# Load the model
yolo = YOLO('yolo11n-seg.pt')

# Train the model
train_reuslt = yolo.train(
    data="../Wood-Defects-7/data.yaml",
    epochs=10, # number of training epochs
    imgsz=640, # training image size
    device=0, # device to run on
)

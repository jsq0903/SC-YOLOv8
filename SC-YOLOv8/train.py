from ultralytics import YOLO
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':

   
    model = YOLO('yolov8n.pt')                                               # Load model with pretrained weights
    model = YOLO('yolov8-our.yaml')                                          # # Alternatively, you can load a specific model.Path:SC-YOLOv8/ultralytics/cfg/models/v8

    results = model.train(data='CR7-DET.yaml', epochs=300, batch size=16)    # Load additional training parameters from default.yaml.Path:SC-YOLOv8/ultralytics/cfg/default.yaml


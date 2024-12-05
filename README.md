A High-Precision And Real-Time Lightweight Detection Model for Small Defects in Cold-Rolled Steel

#1. Installation and Usage Instructions
## 1.1 Clone the Repository
     https://github.com/jsq0903/SC-YOLOv8.git
     
## 1.2 Install Dependencies
     python 3.8.15
     PyTorch 1.13.1
     NVIDIA GPU+CUDA
# 2. Usage
## 2.1 Prepare the Dataset

- CR7-DET/         # https://github.com/jsq0903/CR7-DET.
- GC10-DET/        # https://github.com/lvxiaoming2019/GC10-DET-Metallic-Surface-Defect-Datasets.git
- NEU-DET/         # https://drive.google.com/file/d/1qrdZlaDi272eA79b0uCwwqPrm2Q_WI3k/view?pli=1
  
Once downloaded, organize your dataset folder as follows:
- `dataset/`
  - `images/`          # Folder containing image files
    - `dents1.jpg`
    - `dents2.jpg`
    - `.....`
  - `labels/`          # Folder containing annotation files，
    - `dents1.txt`
    - `dents2.txt`
    - `.....`
## 2.2 Organize Your Dataset Into Train, Test, and Validation Sets
After downloading and organizing your dataset, you need to specify the path to your dataset YAML file. The YAML file contains the necessary configuration and paths for the dataset.

For CR7-DET, use CR7-DET.yaml.
For GC10-DET, use GC10-DET.yaml.
For NEU-DET, use NEU-DET.yaml.
These YAML files can be found in the following directory: SC-YOLOv8/ultralytics/cfg/datasets/

You must split your dataset into three parts: training set, testing set, and validation set. Place the images into the respective folders and update the paths accordingly. For example:

train:  E:/data/dataest/CR7-DET/images/train/
test:   E:/data/dataest/CR7-DET/images/test/
val:    E:/data/dataest/CR7-DET/images/val/
Make sure the paths to your datasets in the YAML file match the folder structure you’ve created on your local machine.
## 2.3 Train the Model
To start training the model, use the train.py

Code:

from ultralytics import YOLO
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':
    
    # Load model with pretrained weights or configuration file
    model = YOLO('yolov8n.pt')   # Using pretrained weights (can also choose yolov8n.yaml for architecture)
    
    # Alternatively, load a specific model configuration
    model = YOLO('yolov8-our.yaml')  # For our SC-YOLOv8, path: SC-YOLOv8/ultralytics/cfg/models/v8/yolov8-our.yaml
    # model = YOLO('yolov8n.yaml')  # For a basic YOLOv8 model, path: SC-YOLOv8/ultralytics/cfg/models/v8/yolov8n.yaml
    # model = YOLO('yolov8-cbam.yaml')  # For CBAM-enhanced YOLOv8, path: SC-YOLOv8/ultralytics/cfg/models/v8/yolov8-cbam.yaml
    # model = YOLO('yolov8-dsconv.yaml')  # For DSConv-enhanced YOLOv8, path: SC-YOLOv8/ultralytics/cfg/models/v8/yolov8-dsconv.yaml

    # Start training the model with specified parameters
    results = model.train(
        data='lengzha.yaml',       # Path to dataset YAML:SC-YOLOv8/ultralytics/cfg/datasets/lengzha.yaml(GC10-DET.yaml or NEU-DET.yaml)
        epochs=200,                # Number of epochs to train for
        batch_size=16              # Batch size
    )                              #additional hyperparameters and settings from SC-YOLOv8/ultralytics/cfg/default.yaml
                                                                              
## 2.4 Evaluate the model
    python test.py 
CODE:
from ultralytics import YOLO
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
if __name__ == '__main__':
    # Load the trained model (best.pt file)
    model = YOLO('')  # Path to the trained model (best.pt)
    # Evaluate the model on the test dataset
    metrics = model.val(split='test', data='CR7-DET.yaml')  # Evaluate the model on the test set using CR7-DET.yaml configuration




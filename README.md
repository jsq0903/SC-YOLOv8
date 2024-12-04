# A High-Precision And Real-Time Lightweight Detection Model for Small Defects in Cold-Rolled Steel
# 1. Installation and Usage Instructions
## 1.1 Clone the Repository
     https://github.com/jsq0903/SC-YOLOv8.git
     
## 1.2 Install Dependencies
     python 3.8.15
     PyTorch 1.13.1
     NVIDIA GPU+CUDA
# 2. Usage
## 2.1 Prepare the Dataset

- lengzha/         # https://github.com/jsq0903/CR7-DET.
- GC10-DET/        # https://github.com/lvxiaoming2019/GC10-DET-Metallic-Surface-Defect-Datasets.git
- NEU-DET/         # https://drive.google.com/file/d/1qrdZlaDi272eA79b0uCwwqPrm2Q_WI3k/view?pli=1

- `dataset/`
  - `images/`          # 图像文件夹
    - `dents1.jpg`
    - `dents2.jpg`
    - `.....`
  - `labels/`          # 标注文件夹
    - `dents1.txt`
    - `dents2.txt`
    - `.....`

## 2.2 Train the Model
    python train.py 


    from ultralytics import YOLO
    import os
    os.environ["GIT_PYTHON_REFRESH"] = "quiet"
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

    if __name__ == '__main__':
    
        model = YOLO('yolov8n.pt')                                            # 权重设置
        model = YOLO('yolov8n.yaml')                                          # 模型架构---SC-YOLOv8/ultralytics/cfg/models/v8/yolov8.yaml
        results = model.train(data='lengzha.yaml', epochs=300)                # 参数设置---SC-YOLOv8/ultralytics/cfg/default.yaml or model.train(参数='',里面自行设置)
                                                                              # lengzha.yaml, GC10-DET.yaml, NEU-DET.yaml---SC-YOLOv8/ultralytics/cfg/datasets
                                                                              
## 2.3 Evaluate the model
    python val.py 





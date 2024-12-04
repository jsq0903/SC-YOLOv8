# A High-Precision And Real-Time Lightweight Detection Model for Small Defects in Cold-Rolled Steel
# 1.Installation and Usage Instructions
## 1.1 Clone the Repository
     https://github.com/jsq0903/SC-YOLOv8.git
     
## 1.2 Install Dependencies
     python	3.8.15
     PyTorch 1.13.1
     NVIDIA GPU+CUDA
# 2.Usage
## 2.1 Prepare the Dataset

### lengzha/         # https://github.com/jsq0903/CR7-DET.
### GC10-DET/        # https://github.com/lvxiaoming2019/GC10-DET-Metallic-Surface-Defect-Datasets.git
### NEU-DET/         # https://drive.google.com/file/d/1qrdZlaDi272eA79b0uCwwqPrm2Q_WI3k/view?pli=1
'''
    ├── image/       # Contains .jpg images of steel strips
    │   ├── dents1.jpg
    │   ├── dents2.jpg
    │   └── ...
    ├── label/       # Corresponding .txt annotations for images
    │   ├── dents1.txt
    │   ├── dents2.txt
    │   └── ...
'''

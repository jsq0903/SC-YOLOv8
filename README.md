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

- lengzha/         # https://github.com/jsq0903/CR7-DET.
- GC10-DET/        # https://github.com/lvxiaoming2019/GC10-DET-Metallic-Surface-Defect-Datasets.git
- NEU-DET/         # https://drive.google.com/file/d/1qrdZlaDi272eA79b0uCwwqPrm2Q_WI3k/view?pli=1

lengzha/
├── image/       # 存放冷轧带钢的图像文件 (.jpg 格式)
│   ├── dents1.jpg
│   ├── dents2.jpg
│   └── ...
├── label/       # 存放与图像对应的标注文件 (.txt 格式)
│   ├── dents1.txt
│   ├── dents2.txt
│   └── ...

# 数据集结构

- `dataset/`
  - `images/`          # 图像文件夹
    - `image1.jpg`
    - `image2.jpg`
    - `image3.jpg`
  - `labels/`          # 标注文件夹
    - `image1.json`
    - `image2.json`
    - `image3.json`
  - `README.md`        # 数据集说明文件




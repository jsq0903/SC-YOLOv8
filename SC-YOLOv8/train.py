from ultralytics import YOLO
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':

   
    model = YOLO('yolov8n.pt')                                              # 权重设置
    model = YOLO('yolov8-our.yaml')                                          # 模型架构
    results = model.train(data='lengzha.yaml', epochs=300, batch size=16)    # 超参数设置



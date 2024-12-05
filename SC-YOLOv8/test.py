from ultralytics import YOLO
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':

    model = YOLO('')                                                      # 训练集上训练好的best.pt 
    metrics = model.val(split='test',data='CR7-DET.yaml')  # 在验证集上评估模型


from ultralytics import YOLO
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':

    model = YOLO('')         # Load the trained model (best.pt file)
    metrics = model.val(split='test',data='CR7-DET.yaml') # Evaluate the model on the test using CR7-DET.yaml


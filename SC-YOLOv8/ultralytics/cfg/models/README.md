## Models


```python

from ultralytics import YOLO

model = YOLO("model.yaml")  # build a YOLOv8n model from scratch # 模型结构
# YOLO("model.pt")  use pre-trained model if available
model.info()  # display model information
model.train(data="coco128.yaml", epochs=100)  # train the model

```



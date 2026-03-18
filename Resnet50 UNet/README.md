# ResNet50 UNet

Vào [Kaggle Notebook](https://www.kaggle.com/code/hieu0469/pruned-quantized-resnet50-unet-cityscapes-2/notebook) để xem chi tiết hơn.

## Kết quả test sau prune 75% và quantize về int8:

| | Accuracy | Dice | IoU | Size | CPU run time | |
|:--- | :--- | :--- | :--- | :--- | :--- | :---|
|Original | 84.3% | 44.77% | 35.13% | 130.46 MB | 2.53s |  [Download](https://drive.google.com/file/d/16IMlZtAX3xz2Yd23o5E1bGrHmcp39MpY/view?usp=sharing)|  
|Pruned  | 86.34% | 45.14% | 35.71% | 26.08 MB| 0.97s |[Download](https://drive.google.com/file/d/10Vr6EPUvjxsD8TgirTSeHH8fk8ms_WQK/view?usp=sharing)|
|Quantized   | 86.1% | 45.03% | 35.48% | 6.48 MB | 0.07s | [Download](https://drive.google.com/file/d/1DCLJxZkapAVgIEXKuIuvN9goLsFuHws4/view?usp=sharing)|


<img width="988" height="331" alt="image" src="https://github.com/user-attachments/assets/0e6651fb-d12f-440e-b4f1-6940b27f5172" />

<img width="985" height="326" alt="image" src="https://github.com/user-attachments/assets/11d6af04-2c5d-48da-858d-27d67a1bda22" />

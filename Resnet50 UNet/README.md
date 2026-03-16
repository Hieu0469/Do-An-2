# ResNet50 UNet

[Kaggle Notebook](https://www.kaggle.com/code/hieu0469/pruned-quantized-resnet50-unet-cityscapes-2/notebook)

## Kết quả test sau prune 75% và quantize về int8:

| | Accuracy | Dice | IoU | Size | CPU run time |
|:--- | :--- | :--- | :--- | :--- | :--- |
|Original | 84.3% | 44.77% | 35.13% | 130.46MB | 2.53s |   
|Pruned  | 86.34% | 45.14% | 35.71% | 26.08MB| 0.97s |
|Quantized  | 86.1% | 45.03% | 35.48% | 6.48MB | 0.07s |


<img width="988" height="331" alt="image" src="https://github.com/user-attachments/assets/0e6651fb-d12f-440e-b4f1-6940b27f5172" />

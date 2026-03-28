# ResNet50 PSPNet

Vào [Kaggle Notebook](https://www.kaggle.com/code/hieu0469/pruned-quantized-resnet50-unet-cityscapes-2) để xem chi tiết hơn.

## Kết quả test sau prune 90% và quantize về int8:

| | Accuracy | Dice | IoU | Size | CPU run time | |
|:--- | :--- | :--- | :--- | :--- | :--- | :---|
|Original | 80.36% | 38.25% | 28.85% | 98.19 MB | 0.05s |  [Download](https://drive.google.com/file/d/1FF1DpDWlhdbAgn236R4MplW84Jwga12_/view?usp=sharing)|  
|Pruned  | 80.91% | 32.56% | 25.44% | 23.5 MB| 0.32s |[Download](https://drive.google.com/file/d/1BHJIPpW6FrKLtdqB5xMX0qjHWhYR9a8h/view?usp=sharing)|
|Quantized   | 80.72% | 32.03% | 25.07% | 5.92 MB | 0.06s | [Download](https://drive.google.com/file/d/1lH5PuU0-fTIgYYjBRRFlfrbH4tDrknDv/view?usp=sharing)|


<img width="967" height="310" alt="image" src="https://github.com/user-attachments/assets/dbd8d17b-5481-46fd-850e-846144fd126a" />

<img width="970" height="315" alt="image" src="https://github.com/user-attachments/assets/1d88865f-305b-4af8-92b9-730a38e84434" />




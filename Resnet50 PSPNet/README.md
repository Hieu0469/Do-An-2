# ResNet50 PSPNet

Vào [Kaggle Notebook](https://www.kaggle.com/code/hieu0469/pruned-quantized-resnet50-pspnet-cityscapes) để xem chi tiết hơn.

## Kết quả test sau prune 90% và quantize về int8:

| | Accuracy | Dice | IoU | Size | CPU run time | |
|:--- | :--- | :--- | :--- | :--- | :--- | :---|
|Original | 80.36% | 38.25% | 28.85% | 98.19 MB | 0.05s |  [Download](https://drive.google.com/file/d/1FF1DpDWlhdbAgn236R4MplW84Jwga12_/view?usp=sharing)|  
|Pruned  | 80.91% | 32.56% | 25.44% | 23.5 MB| 0.32s |[Download](https://drive.google.com/file/d/17EBrwd1NybPwmflsZqVwvEOh4ZLNUag4/view?usp=sharing)|
|Quantized   | 80.72% | 32.03% | 25.07% | 5.92 MB | 0.06s | [Download](https://drive.google.com/file/d/1ThYK0adyZVPcNLYfdtxpSxnQVNrT8572/view?usp=drive_link)|

Note: input size: 192x192

<img width="926" height="670" alt="image" src="https://github.com/user-attachments/assets/fe005c64-eaec-4701-aeb3-a024dc26d849" />





# ResNet50 FPN

[Kaggle Notebook](https://www.kaggle.com/code/hillsp/pruned-quantized-resnet50-fpn-cityscapes?scriptVersionId=304276875)

## Kết quả test sau prune 75% và quantize về int8:

| | Accuracy | Dice | IoU | Size | CPU run time | |
|:--- | :--- | :--- | :--- | :--- | :--- | :---|
|Original | 82.81% | 40.23% | 31.20% | 104.82 MB | 1.83s |  [Download](https://drive.google.com/file/d/1V7oCz2MLA7b0E9vV7N45LXpMZiUztAkl/view?usp=sharing)|  
|Pruned  | 80.91% | 32.56% | 25.44% | 23.5 MB| 0.32s |[Download](https://drive.google.com/file/d/1BHJIPpW6FrKLtdqB5xMX0qjHWhYR9a8h/view?usp=sharing)|
|Quantized   | 80.72% | 32.03% | 25.07% | 5.92 MB | 0.06s | [Download](https://drive.google.com/file/d/1lH5PuU0-fTIgYYjBRRFlfrbH4tDrknDv/view?usp=sharing)|


<img width="614" height="220" alt="image" src="https://github.com/user-attachments/assets/caca56c8-e819-4e6a-890e-46b19928d835" />

<img width="615" height="224" alt="image" src="https://github.com/user-attachments/assets/9c70b606-a7d4-41ed-a3a2-d5236ed81af8" />



# WaSR ResNet50 imu

Vào [Colab Notebook](https://colab.research.google.com/drive/1-kwH78pF_8KEUvEf1vHJX4SvpcbeAotv) để xem chi tiết hơn.

## Kết quả test sau prune 50% và quantize về int8:

| | Accuracy | Dice | IoU | Size | CPU run time | |
|:--- | :--- | :--- | :--- | :--- | :--- | :---|
|Original | 77.77% | 30.34% | 22.77% | 267.27 MB | 0.93s |  [Download](https://drive.google.com/file/d/13KWItsrZWVg4UZSvz97oc5KenccPZ1ac/view?usp=drive_link)|  
|Pruned  | 77.66% | 35.31% | 25.79% | 221.7 MB| 0.81s |[Download](https://drive.google.com/file/d/1ZuBp6mSqtF7X6mfCDIafCfvDKHis03rl/view?usp=drive_link)|
|Quantized   | 81.64% | 41.74% | 31.67% | 54.56 MB | 0.07s | [Download](https://drive.google.com/file/d/13Fb59HPx5y7g3iMdelLIUntY3daaf3Zv/view?usp=drive_link)|

<img width="1333" height="459" alt="image" src="https://github.com/user-attachments/assets/ae87ac03-260c-45ef-899e-f31d9465a01c" />

<img width="1333" height="459" alt="image" src="https://github.com/user-attachments/assets/4b972b87-6bac-48d6-ad1a-f9985827b3e4" />

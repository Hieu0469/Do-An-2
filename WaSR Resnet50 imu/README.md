# WaSR ResNet50 imu

Vào [Colab Notebook](https://colab.research.google.com/drive/1-kwH78pF_8KEUvEf1vHJX4SvpcbeAotv) để xem chi tiết hơn.

## Kết quả test sau prune 50% và quantize về int8:

| | Accuracy | Dice | IoU | Size | CPU run time | |
|:--- | :--- | :--- | :--- | :--- | :--- | :---|
|Original | 76.68% | 29.78% | 22.10% | 241.38 MB | 0.13s |  [Download](https://drive.google.com/file/d/1Mgl_-DFvXnvpFuaV1NWqgIye7n18SAqf/view?usp=drive_link)|  
|Pruned  | 76.98% | 32.57% | 24.44% | 128.62 MB| 0.09s |[Download](https://drive.google.com/file/d/1kn3e6TTpOz2zbQvxQv7oRvWWvfjz309i/view?usp=drive_link)|
|Quantized   | 79.15% | 32.57% | 24.44% | 32.05 MB | 0.07s | [Download](https://drive.google.com/file/d/1ta7CyhZFCxwKltAE6PskdQr2os4inqKU/view?usp=sharing)|

<img width="1333" height="459" alt="image" src="https://github.com/user-attachments/assets/ae87ac03-260c-45ef-899e-f31d9465a01c" />

<img width="1333" height="459" alt="image" src="https://github.com/user-attachments/assets/4b972b87-6bac-48d6-ad1a-f9985827b3e4" />

# eWaSR ResNet18 imu

Vào [Colab Notebook](https://colab.research.google.com/drive/1rI2kuru3nSMKPrwfMHx8rOy4qIXHOB07#scrollTo=jMIEzuu2hTbn) để xem chi tiết hơn.

## Kết quả test sau prune 50% và quantize về int8:

| | Accuracy | Dice | IoU | Size | CPU run time | |
|:--- | :--- | :--- | :--- | :--- | :--- | :---|
|Original | 76.68% | 29.78% | 22.10% | 241.38 MB | 0.13s |  [Download](https://drive.google.com/file/d/1Mgl_-DFvXnvpFuaV1NWqgIye7n18SAqf/view?usp=drive_link)|  
|Pruned  | 76.98% | 32.57% | 24.44% | 128.62 MB| 0.09s |[Download](https://drive.google.com/file/d/1kn3e6TTpOz2zbQvxQv7oRvWWvfjz309i/view?usp=drive_link)|
|Quantized   | 79.15% | 32.57% | 24.44% | 32.05 MB | 0.07s | [Download](https://drive.google.com/file/d/1ta7CyhZFCxwKltAE6PskdQr2os4inqKU/view?usp=sharing)|


<img width="1599" height="553" alt="image" src="https://github.com/user-attachments/assets/93138fdd-4841-48dd-a363-58c2dcbd3449" />

<img width="1600" height="555" alt="image" src="https://github.com/user-attachments/assets/54ca1010-163e-4de4-aff6-5a1257797e15" />

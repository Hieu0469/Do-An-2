# Thư viện test model
Tổng hợp các function dùng để test model

## Cài đặt các thư viện cần thiết:
```bash
!pip install onnx
!pip install onnxruntime
!pip install onnxscript
!pip install segmentation-models-pytorch
!git clone https://github.com/Hieu0469/eWaSR2
!git clone https://github.com/Hieu0469/MyTorchPruning.git
```
## Example:
1. Khai báo đường dẫn đến ảnh
```python
img_path = "Path/to/image"
```

2. Convert ảnh sang tensor
```python
from convert_input import ConvertInput
x = ConvertInput(img_path) # (3, H, W) -> (1, 3, H, W) normalized
```

3. Load model đã lượng tử hóa
```python
import onnxruntime as ort
#Load model
session = ort.InferenceSession("Path/to/onnx/file", providers=['CPUExecutionProvider'])

input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

print(f"Input name: {input_name}")
print(f"Output name: {output_name}")
```



5. Predict
```python
outputs = session.run([output_name], {input_name: x.cpu().numpy()})
```

5. Show ảnh đã predict
```python
from convert_output import ConvertOutput

predicted_mask = ConvertOutput(torch.from_numpy(outputs[0]))  # Convert the output to a colorized image
plt.imshow(predicted_mask)
plt.title("Predicted Mask")
plt.show()
```

6. Kiểm tra độ chính xác
```python
from accuracy_function import accuracy_function, iou_function, f1_score_function, dice_coefficient_function

preds = outputs[0]  # Shape: (1, C, H, W)
output_idx = np.argmax(preds, axis=1).squeeze()  # Shape: (H, W)
mask_idx = y.numpy().squeeze()  # Shape: (H, W)
print("Accuracy:", accuracy_function(torch.from_numpy(output_idx), torch.from_numpy(mask_idx)))
print("IoU:", iou_function(torch.from_numpy(output_idx), torch.from_numpy(mask_idx), num_classes=34))
print("F1 Score:", f1_score_function(torch.from_numpy(output_idx), torch.from_numpy(mask_idx), num_classes=34))
print("Dice Coefficient:", dice_coefficient_function(torch.from_numpy(output_idx), torch.from_numpy(mask_idx), num_classes=34))
```

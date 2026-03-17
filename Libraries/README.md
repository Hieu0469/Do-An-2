# Thư viện test model
Tổng hợp các function dùng để test model bao gồm  
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
session = ort.InferenceSession("{}_quantized_final.onnx".format(model_name), providers=['CPUExecutionProvider'])

input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

print(f"Input name: {input_name}")
print(f"Output name: {output_name}")

#Example

```



5. Predict
```python
outputs = session.run([output_name], {input_name: x.cpu().numpy()})
```

5. Show ảnh đã predict
```python
predicted_mask = ConvertOutput(torch.from_numpy(outputs[0]))  # Convert the output to a colorized image
plt.imshow(predicted_mask)
plt.title("Predicted Mask")
plt.show()
```

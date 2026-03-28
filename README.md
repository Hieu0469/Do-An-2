# Do An 2
## Models Comparison on Cityscapes Dataset
**So sánh và đánh giá các mô hình khác nhau sau khi đã prune và quantize**

Dữ liệu đánh giá: Dataset [Cityscapes](https://www.kaggle.com/datasets/electraawais/cityscape-dataset).

Số lượng ảnh để đánh giá: 500

Các mô hình được so sánh bao gồm:
- ResNet50 UNet
- ResNet50m FPN
- eWaSR ResNet18 imu

## Kết quả
<img width="1518" height="323" alt="image" src="https://github.com/user-attachments/assets/01364341-8f67-42bf-a110-7ccb9b2488c7" />

Các thông tin khác:
- Framework: Pytorch
- Kích thước ảnh đầu vào: 256 x 256
- CPU: AMD Ryzen 5 5500U (2.1GHz)

## Quy trình thực hiện
1. Load model đã train
```python
import torch
import torch.nn as nn
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.load(base_model_load_path,map_location=torch.device(device),weights_only=False)
print("Model loaded successfully")
```

2. Prune model bằng thư viện [Torch-Pruning](https://github.com/VainF/Torch-Pruning)
```python
import torch_pruning as tp
if prune_load_path is None:
    model.eval()
    model.to(device)
    img = torch.randn(1,3,256,256).to(device)
    example_inputs = img
    # 1. Importance criterion, here we calculate the L2 Norm of grouped weights as the importance score
    imp = tp.importance.GroupMagnitudeImportance(p=2) 
    # 2. Initialize a pruner with the model and the importance criterion
    ignored_layers = []
    last_layer = list(model.modules())[-4]
    ignored_layers.append(last_layer) # DO NOT prune the final classifier!
    pruner = tp.pruner.BasePruner( # We can always choose BasePruner if sparse training is not required.
        model,
        example_inputs,
        importance=imp,
        pruning_ratio=0.5, # remove 75% channels
        # pruning_ratio_dict = {model.conv1: 0.2, model.layer2: 0.8}, # customized pruning ratios for layers or blocks
        ignored_layers=ignored_layers,
        isomorphic=True, # enable isomorphic pruning to improve global ranking
        global_pruning=True, # global pruning
        round_to=8,
    )
    base_macs, base_nparams = tp.utils.count_ops_and_params(model, example_inputs)
    tp.utils.print_tool.before_pruning(model) # or print(model)
    pruner.step()
    tp.utils.print_tool.after_pruning(model) # or print(model), this util will show the difference before and after pruning
    macs, nparams = tp.utils.count_ops_and_params(model, example_inputs)
    print(f"MACs: {base_macs/1e9} G -> {macs/1e9} G, #Params: {base_nparams/1e6} M -> {nparams/1e6} M")
else:
    torch.load(prune_load_path,map_location=torch.device(device),weights_only=False)
```

3. Lượng tử hóa mô hình và xuất ra file onnx
```python
import onnx
from onnxruntime.quantization import quantize_static, CalibrationDataReader, QuantType
import copy

model_fp32 = copy.deepcopy(model)

# --- BƯỚC 1: Export FP32 ---
dummy_input = torch.rand(1,3,256,256).to(device)
model_fp32.eval()
torch.onnx.export(
    model_fp32, 
    dummy_input, 
    "{}_fp32.onnx".format(model_name), 
    opset_version=13,
    input_names=['input'],   # Đặt tên cố định là 'input' ở đây
    output_names=['output'], # Đặt tên output luôn cho chuyên nghiệp
    dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
)
# --- BƯỚC 2: Định nghĩa Calibration (Cần thiết cho Static Quantization) ---
class MyDataReader(CalibrationDataReader):
    def __init__(self, dataloader):
        self.enum_data = iter([{'input': x.numpy()} for x, y in dataloader])
    def get_next(self):
        return next(self.enum_data, None)

# Giả sử bạn có một dataloader nhỏ cho calibration
dr = MyDataReader(testloader)

# --- BƯỚC 3: Lượng tử hóa file ONNX ---
quantize_static(
    "{}_fp32.onnx".format(model_name),
    "{}_quantized_final.onnx".format(model_name),
    dr,
    quant_format=QuantType.QInt8 # Hoặc QUInt8 tùy vào phần cứng
)
```
4. Load model đã lượng tử hóa
```python
import onnxruntime as ort
#Load model
session = ort.InferenceSession("{}_quantized_final.onnx".format(model_name), providers=['CPUExecutionProvider'])

input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

print(f"Input name: {input_name}")
print(f"Output name: {output_name}")

#Example
x,y = dataset[0] # Shape: 3, H, W 
input_data = x.unsqueeze(dim=0).numpy() #Shape: 1, 3, H, W

outputs = session.run([output_name], {input_name: input_data})
print("Success")
```

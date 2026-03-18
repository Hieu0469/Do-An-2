import torch
from convert_input import ConvertInput, Normalize
import numpy as np

def ConvertInputWasr(input_image,input_imu_mask=None):
    # Convert the input image to a tensor and normalize it
    # Input: input_image is a file path to the image
    # Output: normalized_image is a tensor of shape (1, 3, H, W) normalized
    tensor_image = ConvertInput(input_image)
    output_image = tensor_image.numpy().astype(np.float32)  # Add batch dimension

    if input_imu_mask is not None:
        tensor_imu_mask = torch.from_numpy(input_imu_mask).float().unsqueeze(0)  # Add batch dimension
        output_mask = tensor_imu_mask.unsqueeze(0).numpy().astype(np.float32)
    else:
        input_imu_mask = torch.zeros((1, 1)).bool()  # Default mask if none provided
        output_mask = input_imu_mask.unsqueeze(0).numpy().astype(np.float32) # Add batch dimension
    
    return output_image, output_mask
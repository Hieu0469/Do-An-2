import torch
import cv2
from colormap import Colorize


def ConvertOutput(output_tensor):
    # Convert the model's output tensor to a colorized image
    # Input: output_tensor is a tensor of shape (1, num_classes, H, W)
    # Output: colorized_image is a 3D array (H, W, 3) where each pixel's color corresponds to its predicted class
    predicted_mask = output_tensor[0].argmax(dim=0).cpu().numpy()  # Get the predicted class for each pixel
    colorized_image = Colorize(predicted_mask)  # Convert class indices to colors
    return colorized_image
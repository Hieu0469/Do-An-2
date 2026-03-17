import torch
import cv2

def Normalize(tensor):
    mean = torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)
    std = torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)
    return (tensor - mean) / std

def unorm(tensor):
    mean = torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)
    std = torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)
    return tensor * std + mean

def load_image_as_tensor(image_path):
    # Load the image using OpenCV
    # Input: image_path is a file path to the image
    # Output: image_tensor is a tensor of shape (3, H, W) normalized
    image = cv2.imread(image_path,cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (256, 256)) # Resize to match model input size (adjust as needed)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Could not load image at {image_path}")
        return None
    
    # Convert the image from BGR to RGB format
    
    # Convert the image to a PyTorch tensor and normalize it
    image = torch.from_numpy(image).float().permute(2, 0, 1) / 255.0
        
    return image


def ConvertInputPath(input_image):
    # Convert the input image to a tensor and normalize it
    # Input: input_image is a file path to the image
    # Output: normalized_image is a tensor of shape (3, H, W) normalized
    tensor_image = load_image_as_tensor(input_image)
    normalized_image = Normalize(tensor_image)
    return normalized_image.unsqueeze(0)  # Add batch dimension

def ConvertInputTensor(input_image_tensor):
    # Convert the input image tensor to a normalized tensor
    # Input: input_image_tensor is a tensor of shape (3, H, W)
    # Output: normalized_image is a tensor of shape (3, H, W) normalized
    normalized_image = Normalize(input_image_tensor)
    return normalized_image.unsqueeze(0)  # Add batch dimension

def ConvertInput(input_image):
    # Convert the input image (file path or tensor) to a normalized tensor
    # Input: input_image can be a file path (str) or a tensor of shape (3, H, W)
    # Output: normalized_image is a tensor of shape (3, H, W) normalized
    if isinstance(input_image, str):
        return ConvertInputPath(input_image)
    elif isinstance(input_image, torch.Tensor):
        return ConvertInputTensor(input_image)
    else:
        raise ValueError("Input must be a file path or a tensor")

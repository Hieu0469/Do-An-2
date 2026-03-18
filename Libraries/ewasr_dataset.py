
from torch.utils.data import Dataset
import os
import cv2
import torch
import numpy as np
import PIL.Image as Image
import torchvision.transforms as transforms
trainsize = 256
class EwasrDataset(Dataset):
    def __init__(self, root_dir, label_dir=None,txt_file=None, transform=None,
                normalize_t = None,include_original = False):
        super().__init__()
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.transform = transform
        self.list_img = []
        self.txt_file = txt_file
        self.list_label_img = []
        for filename in os.listdir(root_dir):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                self.list_img.append(os.path.join(self.root_dir, filename))
        for filename in os.listdir(self.label_dir):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                self.list_label_img.append(os.path.join(self.label_dir, filename))
        self.list_img.sort()
        self.list_label_img.sort()

    def __len__(self):
        return len(self.list_img)

    def __getitem__(self, idx):
        img = self.list_img[idx]
        img_path = os.path.join(self.root_dir, img)
        img = Image.open(img_path).convert("RGB")
        img = img.resize((trainsize, trainsize), Image.BILINEAR)

        mask_img = self.list_label_img[idx]
        mask_path = os.path.join(self.label_dir, mask_img)
        mask = Image.open(mask_path)
        mask = mask.resize((trainsize, trainsize), Image.NEAREST)

        img = np.array(img)
        mask = np.array(mask).astype(np.int64)  # không one-hot

        if self.transform:
            transformed = self.transform(image=img, mask=mask)
            img = transformed['image']
            mask = transformed['mask']

        # convert to tensor
        if not isinstance(img, torch.Tensor):
            img = torch.from_numpy(img).float().permute(2,0,1)/255.0


        if not isinstance(mask, torch.Tensor):
            mask = torch.from_numpy(mask).long()# (H, W)
        else:
            mask = mask.long()
        imu_mask = torch.zeros((1, 1)).bool()
        return {'image': img,'imu_mask' : imu_mask}, {'segmentation': mask}
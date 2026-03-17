from torch.utils.data import Dataset
import os
import cv2
import torch
import numpy as np


trainsize = 256
class MyDataset(Dataset):
    def __init__(self, root_dir, label_dir=None,txt_file=None, transform=None):
        '''Custom dataset for loading images and their corresponding segmentation masks.
        Args:
            root_dir (str): Directory containing the input images.
            label_dir (str, optional): Directory containing the segmentation masks. If None, only images will be loaded. Defaults to None.
            txt_file (str, optional): Path to a text file containing image paths and labels (not used in this implementation). Defaults to None.
            transform (callable, optional): A function/transform to apply to the images and masks. Defaults to None.
        '''        
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
        image = cv2.imread(img_path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (trainsize, trainsize))
        if self.label_dir is not None:
            mask_img = self.list_label_img[idx]
            mask_path = os.path.join(self.label_dir, mask_img)
            mask = cv2.imread(mask_path)
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
            mask = cv2.resize(mask, (trainsize,trainsize),interpolation=cv2.INTER_NEAREST)


        if self.transform is not None:
            if self.label_dir is not None:
                transformed = self.transform(image=image, mask=mask)
                image = transformed['image']
                mask = transformed['mask']
            else:
                transformed = self.transform(image=image)
                image = transformed['image']
                return image
        else:
            image = torch.from_numpy(image).float().permute(2, 0, 1) / 255.0
            if self.label_dir is not None:
                mask = torch.from_numpy(mask).long()

            else:
                return image
        return image, mask
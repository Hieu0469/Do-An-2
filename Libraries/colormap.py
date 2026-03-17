import cv2
import torch
import numpy as np

COLORMAP = [
        [  0,   0,   0],  #0: background
        [0, 0, 0],
        [  0,   0, 255],  #1
        [  0, 220, 220],  #2
        [200, 200, 0],  #3: backward-faced sign
        [ 60,  20, 220],  #4
        [ 70,  70,  70],  #5
        [ 200,   0,  200],  #6: road
        [150,  250, 150],  #7: sidewalk
        [142,   0,   0],  #8
        [153, 153, 153],  #9
        [70, 70, 70],  #10: building
        [156, 102, 102],  #11
        [180, 130,  70],  #12
        [230,   0,   0],  #13: forward-faced sign
        [232,  35, 244],  #14: footbridge
        [150, 150, 75],  #15
        [90, 90, 120],  #16 pole/fence
        [156, 102, 102],  #17
        [0, 35,  70],  #18: traffic light
        [230,   0,   0],  #19
        [0,  70, 0],  #20: tree
        [0, 100, 0],  #21: grass
        [70, 130, 180],  #22: sky
        [128, 128, 0],  #23: pedestrian
        [255, 0, 0],  #24: biker
        [120,0,0],  #25: car
        [0,0,128],  #26
        [0,50,128],  #27: truck/bus
        [20,50,90],  #28
        [20,180,100],  #29
        [70,160,40],  #30
        [45,80,20],  #31: motorbike
        [20,160,140],  #32: bike
        [120,120,120]
]

def Colorize(segmentation_map):
    # Input: segmentation_map is a 2D array of class indices
    # Output: color_image is a 3D array (H x W x 3) where each pixel's color corresponds to its class index

    # Create an empty color image
    color_image = np.zeros((segmentation_map.shape[0], segmentation_map.shape[1], 3), dtype=np.uint8)

    # Map each class index to its corresponding color
    for class_index in range(len(COLORMAP)):
        color_image[segmentation_map == class_index] = COLORMAP[class_index]
    return color_image
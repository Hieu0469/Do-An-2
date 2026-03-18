import torch
import numpy as np

def accuracy_function(pred, target):
    # pred: (H, W) - predicted class indices
    # target: (H, W) - ground truth class indices
    # Input: pred and target are expected to be 2D tensors of the same shape
    # Output: accuracy as a float value between 0 and 1

    if pred.shape != target.shape:
        raise ValueError("Shape of pred and target must be the same. Got pred shape: {}, target shape: {}".format(pred.shape, target.shape))
    pred = pred.flatten()
    target = target.flatten()
    correct = (pred == target).sum().item()
    total = target.numel()
    accuracy = correct / total if total > 0 else 0.0
    return accuracy

def iou_function(pred, target, num_classes=34):
    # pred: (H, W) - predicted class indices
    # target: (H, W) - ground truth class indices
    # num_classes: total number of classes in the segmentation task
    # Output: IoU for each class as a list of floats

    if pred.shape != target.shape:
        raise ValueError("Shape of pred and target must be the same. Got pred shape: {}, target shape: {}".format(pred.shape, target.shape))
    ious = []
    for cls in range(num_classes):
        pred_cls = (pred == cls)
        target_cls = (target == cls)
        intersection = (pred_cls & target_cls).sum().item()
        union = (pred_cls | target_cls).sum().item()
        iou = intersection / union if union > 0 else 0.0
        ious.append(iou)
    return sum(ious) / len(ious) if ious else 0.0

def f1_score_function(pred, target, num_classes=34):
    # pred: (H, W) - predicted class indices
    # target: (H, W) - ground truth class indices
    # num_classes: total number of classes in the segmentation task
    # Output: F1 score for each class as a list of floats

    if pred.shape != target.shape:
        raise ValueError("Shape of pred and target must be the same. Got pred shape: {}, target shape: {}".format(pred.shape, target.shape))
    f1_scores = []
    for cls in range(num_classes):
        pred_cls = (pred == cls)
        target_cls = (target == cls)
        tp = (pred_cls & target_cls).sum().item()  # True Positives
        fp = (pred_cls & ~target_cls).sum().item()  # False Positives
        fn = (~pred_cls & target_cls).sum().item()  # False Negatives
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
        f1_scores.append(f1_score)
    return sum(f1_scores) / len(f1_scores) if f1_scores else 0.0

def dice_coefficient_function(pred, target, num_classes=34):
    # pred: (H, W) - predicted class indices
    # target: (H, W) - ground truth class indices
    # num_classes: total number of classes in the segmentation task
    # Output: Dice coefficient for each class as a list of floats

    if pred.shape != target.shape:
        raise ValueError("Shape of pred and target must be the same. Got pred shape: {}, target shape: {}".format(pred.shape, target.shape))
    dice_coefficients = []
    for cls in range(num_classes):
        pred_cls = (pred == cls)
        target_cls = (target == cls)
        intersection = (pred_cls & target_cls).sum().item()
        dice_coefficient = 2 * intersection / (pred_cls.sum().item() + target_cls.sum().item()) if (pred_cls.sum().item() + target_cls.sum().item()) > 0 else 0.0
        dice_coefficients.append(dice_coefficient)
    return sum(dice_coefficients) / len(dice_coefficients) if dice_coefficients else 0.0

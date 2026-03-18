
import torch
import torch.nn as nn
import os
import sys
sys.path.append(r"E:/work/DL/Code/eWaSR2")
from wasr.decoders import EWaSRDecoder
from wasr.utils import IntermediateLayerGetter
from segmentation_models_pytorch.encoders import get_encoder
from collections import OrderedDict
class ewasr_resnet18_imu(nn.Module):
    def __init__(self,num_classes,imu=True):
        super(ewasr_resnet18_imu,self).__init__()
        
        self.imu = True
        backbone = get_encoder('resnet18',depth=4,weights="imagenet")
        return_layers = {
            'layer4': 'out',
            'layer1': 'skip1',
            'layer2': 'skip2',
            'layer3': 'aux'
        }
        backbone = IntermediateLayerGetter(backbone, return_layers=return_layers)
        ch = 512
        decoder = EWaSRDecoder(
                                num_classes=num_classes,
                                ch= ch, #512 if kwargs.get("ch") is None else kwargs["ch"], 
                                L=6, 
                                imu = imu,
                                mixer="CCCCSS",
                                ch_sim=256,
                                enricher="SS",
                                project=False
                                )
        self.backbone = backbone
        self.decoder = decoder
        
    def forward(self, x):
        features = self.backbone(x['image'])
        
        features['imu_mask'] = x['imu_mask'].float().unsqueeze(1)
        features = (features['out'], features['aux'], features['skip2'], features['skip1'], features['imu_mask'])
        aux = features[1]
        x = self.decoder(*features)

        # # Return segmentation map and aux feature map
        output = OrderedDict([
            ('out', x),
            ('aux', aux)
        ])

        return output
import numpy as np
import torch
import torch.nn as nn

class AddFuse(nn.Module):
    def __init__(self, model_cfg):
        super().__init__()

    def forward(self, data_dict):

        data_dict['spatial_features_2d']=torch.add(data_dict['spatial_features_2d'],data_dict['spatial_features_2d_dpc']) / 2
        # print(data_dict['spatial_features_2d'].size())
        # torch.Size([4, 512, 200, 176])

        return data_dict

class CatFuse(nn.Module):
    def __init__(self, model_cfg):
        super().__init__()

    def forward(self, data_dict):

        data_dict['spatial_features_2d']=torch.cat((data_dict['spatial_features_2d'], data_dict['spatial_features_2d_dpc']), 1)
        # print(data_dict['spatial_features_2d'].size())
        # torch.Size([4, 1024, 200, 176])
        
        return data_dict

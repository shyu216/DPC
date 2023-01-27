# DPC
3D Object Detection based on Densified Point Cloud

# Env.
## CSE Linux

- Using GPU
```
srun --gres=gpu:1 -w gpu36 --pty /bin/bash
```

# Dataset
## KITTI

# PreProcessor 
## SFD

## PENet

- Densify PC
```
CUDA_VISIBLE_DEVICES="0" python main.py -b 1 -n pe --evaluate ./pe.pth.tar --test   --data-folder-save ../testresult --data-folder ../depthcompletiondataset/kitti_depth/depth
```

# Deep Learning Model
OpenPCDet
# DPC
3D Object Detection based on Densified Point Cloud

# env
## cse linux

- using gpu
```
srun --gres=gpu:1 -w gpu36 --pty /bin/bash
```

# dataset
## kitti

# preprocessor 
## SFD

## PENet

- densify pc
```
CUDA_VISIBLE_DEVICES="0" python main.py -b 1 -n pe --evaluate ./pe.pth.tar --test   --data-folder-save ../testresult --data-folder ../depthcompletiondataset/kitti_depth/depth
```

# deep learning model
OpenPCDet
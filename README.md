# DPC
3D Object Detection based on **Densified** **Point** **Cloud**

# Env.
## CSE Linux

- Using GPU
```
srun --gres=gpu:1 -w gpu34 --pty /bin/bash

sbatch my.cmd

squeue -u user -w gpuid

scancel jobid
```
reference: [Use Slurm to Submit Job](https://i.cse.cuhk.edu.hk/technical/gpgpu-hpc-service/slurm/)

# Dataset
## KITTI

# PreProcessor 
## SFD

## PENet

- Densify PC
```
CUDA_VISIBLE_DEVICES="0" python main.py -b 1 -n pe --evaluate ./pe.pth.tar --test   --data-folder-save ../testresult --data-folder ../depthcompletiondataset/kitti_depth/depth

CUDA_VISIBLE_DEVICES="0" python main.py -b 1 -n pe --evaluate ./pe.pth.tar --test   --data-folder-save ../testresult --data-folder ./
```



































# Deep Learning Model
OpenPCDet
# DPC
3D Object Detection based on **Densified** **Point** **Cloud**

# Env.
## CSE Linux

- Using GPU
```
srun --gres=gpu:1 -w gpu38 --pty /bin/bash

sbatch my.cmd

squeue -u user -w gpuid

scancel jobid
```
reference: [Use Slurm to Submit Job](https://i.cse.cuhk.edu.hk/technical/gpgpu-hpc-service/slurm/)

# Dataset
## KITTI

# PreProcessor 
## SFD
```
python depth_to_lidar.py
python lidar_to_depth.py
```

## PENet

- Densify PC
```
CUDA_VISIBLE_DEVICES="0" python main.py -b 1 -n pe --evaluate ./pe.pth.tar --test   --data-folder-save ./somewhere --data-folder ../depthcompletiondataset/kitti_depth/depth

CUDA_VISIBLE_DEVICES="0" python main.py -b 1 -n pe --evaluate ./pe.pth.tar --test   --data-folder-save ./somewhere --data-folder ./

nohup python main.py -b 1 -n pe --evaluate ./pe.pth.tar --test   --data-folder-save ../testing --data-folder ./ &
```

```
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
```


# Object Detector
## OpenPCdet
```
python train.py --cfg_file cfgs/kitti_models/voxel_rcnn_car.yaml --epochs 100 --max_ckpt_save_num 100
python test.py --cfg_file cfgs/kitti_models/voxel_rcnn_car.yaml --batch_size 10 --eval_all

tensorboard --logdir tensorboard

python test.py --cfg_file cfgs/kitti_models/voxel_rcnn_car.yaml --batch_size 10 --ckpt ../../models/voxel_rcnn_car_84.54.pth


python train_dpc.py --cfg_file cfgs/kitti_models/second_dpc.yaml

python test.py --cfg_file cfgs/kitti_models/second.yaml --batch_size 10 --ckpt /research/dept8/fyp22/lj2202/models/second_7862.pth
```































# Deep Learning Model
OpenPCDet
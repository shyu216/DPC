# Records of SFD Setup (2022 Mar 20)

1. after download/build/enter the container

adding -user means it will be write in ~/ rather than /usr/local/

cd SFD
python setup.py develop --user
cd pcdet/ops/iou3d/cuda_op
python setup.py develop --user
cd ../../../..
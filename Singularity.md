# Records of Singularity Setup (2022 Mar 20)

In our CSE linux, the docker container can be used with the help of Singulariy.

1. pull docker
```
singularity pull docker://scrin/dev-spconv
```
if docker command is: 
```
docker pull scrin/dev-spconv
```
2. add some path in the .bashrc

need to create these paths in advance
```
export SINGULARITY_CACHEDIR=/research/dept8/fyp22/lj2202/Singularity/cache
export SINGULARITY_LOCALCACHEDIR=/research/dept8/fyp22/lj2202/Singularity/localcache
export SINGULARITY_TMPDIR=/research/dept8/fyp22/lj2202/Singularity/tmp
export PATH="$PATH:/usr/sbin"

export SINGULARITY_BIND="/usr/local/cuda-10.2:/usr/local/cuda-10.2,/usr/local/cuda-10.0:/usr/local/cuda,/usr/local/cuda-10.1/:/usr/local/cuda-10.1,/research:/research"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64/:/.singularity.d/libs:/usr/local/cuda-10.1/lib64/"
```
3. ask admin for help to add some other path

4. run it in gpu
```
srun --gres=gpu:1 -w gpu38 --pty /bin/bash

singularity shell --nv pcdet-pytorch1.5_latest.sif 
```

5. done!


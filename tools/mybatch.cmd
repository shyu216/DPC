#!/bin/bash
#SBATCH --job-name=lj2202
#SBATCH --mail-user=shyu0@cse.cuhk.edu.hk
#SBATCH --mail-type=ALL
#SBATCH --output=/research/dept8/fyp22/lj2202/DPC/tools/output.txt ##Do not use "~" point to your home!
#SBATCH --gres=gpu:1
#SBATCH -p gpu_24h

## Below is the commands to run , for this example,
## Create a sample helloworld.py and Run the sample python file
## Result are stored at your defined --output location



# Installation
**scMultiNet**
A deep adversarial network model for multi-task analysis of single-cell omics data
## Environment requirements:
scMultiNet requires Python 3.8.x and Pytorch.
We have tested the GPU version on the NVIDIA RTX 2080 Ti platform with CUDA version 11.1.
For example, we suggest to install the dependencies in a conda environment.
### Conda Environment
```
conda create -n scMultiNet python=3.8
conda activate scMultiNet
```
and then you can use pip to install the following **dependencies** within the scMultiNet environment.
### Dependencies
- python 3.8.10
- h5py 3.9.0
- torch 1.9.0+cu111
- anndata 0.9.2
- scanpy 1.9.3
- scikit-learn 0.22.2

## Quick Start
1. Prepare the input data in h5 format. (See readme in 'data' folder)

2. You can run **scMultiNet** using the tutorial document provided, which guides you through the process step by step. Alternatively, you can run scMultiNet directly using the following command in your terminal:

```
python train.py --dataset=BMNC
```
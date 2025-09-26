# Installation

**scMultiNet**: A deep adversarial network model for multi-task analysis of single-cell omics data.  
🔗 GitHub: [Biowust/scMultiNet](https://github.com/Biowust/scMultiNet)

---

## Environment Requirements

- **Python**: 3.8.x  
- **PyTorch**: GPU version recommended  
- **Tested Platform**: NVIDIA RTX 2080 Ti with **CUDA 11.1**

We recommend creating a dedicated conda environment for installation.

### Create Conda Environment
```bash
conda create -n scMultiNet python=3.8
conda activate scMultiNet
```

### Install Dependencies
After activating the environment, install the following dependencies via `pip`:

- python==3.8.10  
- h5py==3.9.0  
- torch==1.9.0+cu111  
- anndata==0.9.2  
- scanpy==1.9.3  
- scikit-learn==0.22.2  

---

## Quick Start

1. **Prepare Input Data**  
   - Format: `.h5`  
   - See the `data/` folder README for details.

2. **Run scMultiNet**  
   - You can either follow the tutorial document step by step,  
     or run directly with the following command:

```bash
python train.py --dataset=BMNC
```
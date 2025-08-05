
# m6A-mediated RNA Regulation Modeling

## Description
This repository contains the Python implementation of a mathematical model for RNA regulation mediated by m6A modifications. The model uses an analogy to epidemic spreading models to represent transitions between states: Unmodified (U), Modified (M), and Degraded (D).

## Files
- m6A_RNA_Modeling_Code.py: Main script for simulation and visualization.
- Figures:
  - simulation_results.png
  - conceptual_model.png

## Requirements
- Python 3.x
- numpy
- matplotlib
- networkx
- scipy

## How to Run
1. Install dependencies:
   ```bash
   pip install numpy matplotlib networkx scipy
   ```
2. Run the script:
   ```bash
   python m6A_RNA_Modeling_Code.py
   ```
The script generates:
- A simulation plot showing RNA state dynamics over time.
- A conceptual diagram of the mRNA transition model.

## Citation
If you use this code, please cite:
[Your Name], "Mathematical Modeling of m6A-Mediated RNA Regulation," 2025.

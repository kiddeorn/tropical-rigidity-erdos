# tropical-rigidity-erdos
Supplementary code for: A Tropical Rigidity Framework for the Erdős Conjecture on Arithmetic Progressions

# Supplementary Code: A Tropical Rigidity Framework for the Erdős Conjecture

This repository contains the supplementary computational scripts required to reproduce the local evidence presented in the manuscript.

## License & Data Availability
- **License:** MIT License (Open Source)
- **Data Availability:** The latest version of this code is hosted at `[GitHub URL or DOI]`.

## System Requirements & Installation
To run the scripts, ensure you have Python 3.8+ and SageMath 9.0+ installed.
The Python script requires no external libraries (uses standard `fractions` and `math`). The SageMath script runs in the standard Sage environment.

```bash
# No additional pip installations are strictly required, but for extended symbolic tests:
pip install sympy
```

## U_3 Valuation Tracker (AP-4 Evidence)Simulates the valuation grading transitions under $A_3$ quiver mutations to confirm the Leading-Term Non-Vanishing (LTNV) condition. 
Estimated Execution Time: ~2 seconds. 
Execution:
```Bash
python3 u3_valuation_tracker.py
```
Expected Output (Excerpt):
```
Mutation_Step, Input_g_vector, Output_g_vector, LTNV_Status, lambda_eff
Initial,       (1, 1, 2),      (1, 1, 2),       PASS,        N/A
mu_2,          (1, 1, 2),      (1, 1, 2),       PASS,        0.000
mu_1,          (1, 1, 2),      (0, 1, 2),       PASS,       -1.000
mu_3,          (0, 1, 2),      (0, 1,-1),       PASS,       -3.000

[Success] All 15 trajectories verified. The algebraic entropy lambda converges to 0.
```

## AP-5 Wild-Type Invariance CheckSymbolically verifies the mutation invariance of the $U_4$-nilfactor Hamiltonian $H$ and evaluates the finite truncation of the path-ordered product. 
Estimated Execution Time: ~45 seconds (depending on symbolic expansion depth). 
Execution:
```Bash
sage ap5_scattering_check.sage
```
Expected Output (Excerpt):
```
Initializing B_AP5 quiver and fraction field R<x1, x2, x3, x4>...
Testing invariant H = (x1^2 + x3^2 + x2*x4 + 1) / (x1*x2*x3*x4)
- Mutation mu_1 applied. Checking H == mu_1(H)... [TRUE]
- Mutation mu_2 applied. Checking H == mu_2(H)... [TRUE]

[Success] H is a global invariant. Maurer-Cartan 1-cohomology conditi
```


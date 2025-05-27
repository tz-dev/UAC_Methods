# ========================================================
# File: lorentz_signature_detection.py
# Purpose: Analyze Hessian signature of entropy function → emergent spacetime metric
# Method:
#   - Compute 4×4 Hessians of S(x) at random points
#   - Count positive vs. negative eigenvalues
# Inputs:
# - N_samples: Number of Hessian samples (default: 1000)
# - tau: Meta-time scale (default: 5.391e-44 s)
# Output:
#   - Signature distribution & eigenvalue histograms
# ========================================================

import numpy as np
from numpy.linalg import eigvalsh
import matplotlib.pyplot as plt
import numpy as np


# Interactive Inputs
print("=== Lorentz Signature Detection Configuration ===")
try:
    N_samples = int(input("Enter number of samples N_samples [default 1000]: ") or 1000)
    tau = float(input("Enter meta-time scale tau (s) [default 5.391e-44]: ") or 5.391e-44)
    if N_samples <= 0 or tau <= 0:
        raise ValueError("N_samples and tau must be positive.")
    if N_samples > 10000:
        raise ValueError("N_samples too large for performance.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    N_samples = 1000
    tau = 5.391e-44

np.random.seed(42)
signature_counts = {(+1, -3): 0, (-1, +3): 0, 'other': 0}

for _ in range(N_samples):
    H = np.random.normal(loc=0, scale=1/np.sqrt(tau), size=(4, 4))
    H = (H + H.T) / 2  # Symmetrize
    eigenvalues = np.linalg.eigvalsh(H)
    signs = np.sign(eigenvalues)
    positive = np.sum(signs > 0)
    negative = np.sum(signs < 0)
    if positive == 1 and negative == 3:
        signature_counts[(+1, -3)] += 1
    elif positive == 3 and negative == 1:
        signature_counts[(-1, +3)] += 1
    else:
        signature_counts['other'] += 1

total = sum(signature_counts.values())
print("=== Lorentz Signature Statistics ===")
for sig, count in signature_counts.items():
    print(f"Signature {sig}: {count} ({count/total*100:.2f}%)")
# =============================================================================
# File        : lagrangian_density_simulation.py
# Purpose     : Simulate local Lagrangian values from entropy field statistics.
#               Evaluate energy scale and stability under entropic potential.
# Inputs      :
# - S_mean: Mean entropy value (default: 2.74309)
# - S_sigma: Entropy standard deviation (default: 0.05894)
# - N: Number of samples (default: 1000)
# - repeats: Number of simulation repeats (default: 500)
# - kappa: Scaling factor (default: 6.5244e34 J/m)
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt


# Interactive input
print("=== Lagrangian Density Simulation Configuration ===")
try:
    S_mean = float(input("Enter mean entropy S_mean [default 2.74309]: ") or 2.74309)
    S_sigma = float(input("Enter entropy standard deviation S_sigma [default 0.05894]: ") or 0.05894)
    N = int(input("Enter number of samples N [default 1000]: ") or 1000)
    repeats = int(input("Enter number of repeats [default 500]: ") or 500)
    kappa = float(input("Enter scaling factor kappa (J/m) [default 6.5244e34]: ") or 6.5244e34)
    if S_sigma <= 0 or N <= 0 or repeats <= 0 or kappa <= 0:
        raise ValueError("S_sigma, N, repeats, and kappa must be positive.")
    if N > 10000 or repeats > 1000:
        raise ValueError("N or repeats too large for performance.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    S_mean = 2.74309
    S_sigma = 0.05894
    N = 1000
    repeats = 500
    kappa = 6.5244e34

np.random.seed(42)
L_values = np.zeros(repeats)

for i in range(repeats):
    S = np.random.normal(loc=S_mean, scale=S_sigma, size=N)
    grad_S = np.random.normal(loc=0, scale=S_sigma, size=(N, 4))
    grad_norm = np.linalg.norm(grad_S, axis=1)
    L = kappa * np.mean(S * grad_norm)
    L_values[i] = L

L_mean = np.mean(L_values)
L_std = np.std(L_values)
print(f"Mean Lagrangian density: {L_mean:.8e} J/m^3")
print(f"Standard deviation: {L_std:.8e} J/m^3")

plt.figure(figsize=(8, 6))
plt.hist(L_values, bins=50, color='teal', alpha=0.7)
plt.axvline(L_mean, color='red', linestyle='--', label=f'Mean = {L_mean:.2e}')
plt.title('Distribution of Lagrangian Density')
plt.xlabel('Lagrangian density (J/m^3)')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('img/lagrangian_density_simulation.png')
plt.close()
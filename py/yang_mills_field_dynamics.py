# ========================================================
# File: yang_mills_field_dynamics.py
# Purpose: Simulate SU(2)-like Yang–Mills dynamics from entropy field A^a_μ
# Parameters:
#   - g = 0.65 (gauge coupling)
#   - κ = ħ / l_meta (field scale)
# Inputs:
#   - S_mean: Mean entropy (default: 2.74309)
#   - S_sigma: Entropy standard deviation (default: 0.05894)
#   - N: Number of samples (default: 1000)
# Output:
#   - Energy density histogram per color index
# ========================================================

import numpy as np
import matplotlib.pyplot as plt

print("=== Yang-Mills Field Dynamics Configuration ===")
try:
    S_mean = float(input("Enter mean entropy S_mean [default 2.74309]: ") or 2.74309)
    S_sigma = float(input("Enter entropy standard deviation S_sigma [default 0.05894]: ") or 0.05894)
    N = int(input("Enter number of samples N [default 1000]: ") or 1000)
    if S_sigma <= 0 or N <= 0:
        raise ValueError("S_sigma and N must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    S_mean = 2.74309
    S_sigma = 0.05894
    N = 1000

# Constants
hbar = 1.054571817e-34  # J·s
l_meta = 1.616e-35  # m
g = 0.65  # Gauge coupling
kappa = hbar / l_meta  # Field scale

# Entropy samples
np.random.seed(42)
S = np.random.normal(S_mean, S_sigma, N)

# Gauge field (simplified)
A = np.random.normal(0, S_sigma * kappa, (N, 3, 4))  # a=1,2,3; mu=0,1,2,3
F = np.zeros((N, 3, 4, 4))  # Field strength tensor

# Structure constants (simplified)
def f_abc(a, b, c):
    return (a - b) * (b - c) * (c - a) / 2

# Compute field strength tensor
for i in range(N):
    for a in range(3):
        for mu in range(4):
            for nu in range(4):
                partial_term = (A[i, a, nu] - A[i, a, mu]) / l_meta if mu != nu else 0
                gauge_term = 0
                for b in range(3):
                    for c in range(3):
                        gauge_term += g * f_abc(a, b, c) * A[i, b, mu] * A[i, c, nu]
                F[i, a, mu, nu] = partial_term + gauge_term

# Energy density
rho = np.zeros((N, 3))
for i in range(N):
    for a in range(3):
        electric = sum(F[i, a, 0, j]**2 for j in range(1, 4))
        magnetic = -0.25 * sum(F[i, a, mu, nu]**2 for mu in range(1, 4) for nu in range(mu + 1, 4))
        rho[i, a] = electric + magnetic

mean_rho = np.mean(rho, axis=0)

print("=== Yang-Mills Field Dynamics Results ===")
for a in range(3):
    print(f"Mean energy density (color {a}): {mean_rho[a]:.8e} J/m^3")

# Visualization
plt.figure(figsize=(8, 6))
plt.hist(rho.flatten(), bins=50, color='blue', alpha=0.7)
plt.xlabel('Energy density [J/m^3]')
plt.ylabel('Frequency')
plt.title('Yang-Mills Energy Density Distribution')
plt.grid(True)
plt.savefig('img/c2_4_yangmills_energy_density_histogram.png')
plt.close()
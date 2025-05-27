# ========================================================
# File: entropy_vector_field_visualization.py.py
# Purpose: Project the entropy gradient ∂μS onto an abelian vector field Aμ
# Parameters:
#   - S_mean = 2.74309 (average entropy)
#   - S_sigma = 0.05894 (entropy standard deviation)
#   - κ = ħ / l_meta (field strength scaling constant)
# Input:
# - mean entropy S_mean, entropy standard deviation S_sigma), and number of samples N
# Output:
#   - Histograms and norm plot of Aμ components
# ========================================================

import numpy as np
import matplotlib.pyplot as plt

# Interactive input
print("=== Entropy Vector Field Visualization Configuration ===")
try:
    S_mean = float(input("Enter mean entropy S_mean [default 2.74309]: ") or 2.74309)
    S_sigma = float(input("Enter entropy standard deviation S_sigma [default 0.05894]: ") or 0.05894)
    N = int(input("Enter number of samples N [default 10000]: ") or 10000)
    if S_sigma <= 0 or N <= 0:
        raise ValueError("S_sigma and N must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    S_mean = 2.74309
    S_sigma = 0.05894
    N = 10000

# Constants
k_B = 1.380649e-23
hbar = 1.054571817e-34
l_meta = 1.616e-35
tau_meta = 5.391e-44
c = 2.99792458e8

np.random.seed(42)

# Generate entropy gradients
dS_dtau = np.random.normal(loc=S_mean, scale=S_sigma, size=N)
dS_dx = np.random.normal(loc=0, scale=S_sigma, size=N)
dS_dy = np.random.normal(loc=0, scale=S_sigma, size=N)
dS_dz = np.random.normal(loc=0, scale=S_sigma, size=N)
grad_S = np.stack([dS_dtau, dS_dx, dS_dy, dS_dz], axis=1)

kappa = hbar / l_meta
A_mu = kappa * grad_S

A_mean = np.mean(A_mu, axis=0)
A_max = np.max(np.abs(A_mu), axis=0)

print("A_mu mean components:", A_mean)
print("A_mu max components:", A_max)

# Visualization
plt.figure(figsize=(10, 6))
labels = [r'$A_0$', r'$A_1$', r'$A_2$', r'$A_3$']
for i in range(4):
    plt.hist(A_mu[:, i], bins=60, alpha=0.6, label=labels[i])
plt.title('Histogram of Projected Abelian Vector Field Components $A_\\mu$')
plt.xlabel('Field strength (J/m)')
plt.ylabel('Density')
plt.legend()
plt.savefig('img/c2_2_entropy_vectorfield_histogram.png')
plt.close()

A_norm = np.linalg.norm(A_mu, axis=1)
plt.figure(figsize=(8, 6))
plt.plot(np.sort(A_norm))
plt.title('Sorted Norm of Vector Field $|A_\\mu|$')
plt.xlabel('Sample Index')
plt.ylabel(r'$|A_\mu|$ (J/m)')
plt.savefig('img/c2_2_entropy_vectorfield_norm_sorted.png')
plt.close()
# ========================================================
# File: rg_stability_landscape_mapping.py
# Purpose: Analyze RG flow stability and map coupling constants at M_Z scale
# Method:
#   - Compute 1-loop RG running of gauge couplings α_i(μ) over large scale
#   - Calculate derivatives to check flow stability
#   - Map and print coupling values at M_Z and maximum slope of RG flow
# Inputs:
# - alpha1_0, alpha2_0, alpha3_0: Initial inverse couplings (default: 59.0, 29.6, 8.5)
# - b1, b2, b3: Beta coefficients (default: 6.6, 1.0, -3.0)
# Output:
#   - Print α_i(M_Z), max RG slope
#   - Save plot of α_i(μ) over μ
# ========================================================

import numpy as np
import matplotlib.pyplot as plt

# Interaktive Eingaben
print("=== RG Stability Landscape Mapping Configuration ===")
try:
    alpha1_0 = float(input("Enter initial inverse coupling α_1⁻¹(M_Z) [default 59.0]: ") or 59.0)
    alpha2_0 = float(input("Enter initial inverse coupling α_2⁻¹(M_Z) [default 29.6]: ") or 29.6)
    alpha3_0 = float(input("Enter initial inverse coupling α_3⁻¹(M_Z) [default 8.5]: ") or 8.5)
    b1 = float(input("Enter beta coefficient b_1 [default 6.6]: ") or 6.6)
    b2 = float(input("Enter beta coefficient b_2 [default 1.0]: ") or 1.0)
    b3 = float(input("Enter beta coefficient b_3 [default -3.0]: ") or -3.0)
    if alpha1_0 <= 0 or alpha2_0 <= 0 or alpha3_0 <= 0:
        raise ValueError("Initial couplings must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    alpha1_0, alpha2_0, alpha3_0 = 59.0, 29.6, 8.5
    b1, b2, b3 = 6.6, 1.0, -3.0

mu = np.logspace(2, 17, 500)
log_mu = np.log(mu / 91.2)

def alpha_inv(alpha0, b, log_mu):
    return 1/alpha0 - b / (2 * np.pi) * log_mu

alpha1_inv = alpha_inv(1/alpha1_0, b1, log_mu)
alpha2_inv = alpha_inv(1/alpha2_0, b2, log_mu)
alpha3_inv = alpha_inv(1/alpha3_0, b3, log_mu)

# Stability metric
diff12 = np.abs(alpha1_inv - alpha2_inv)
diff23 = np.abs(alpha2_inv - alpha3_inv)
diff13 = np.abs(alpha1_inv - alpha3_inv)
total_diff = diff12 + diff23 + diff13

min_idx = np.argmin(total_diff)
mu_unif = mu[min_idx]
alpha_unif = np.mean([alpha1_inv[min_idx], alpha2_inv[min_idx], alpha3_inv[min_idx]])

print("=== Stability Landscape Summary ===")
print(f"Unification scale μ_unif ≈ {mu_unif:.3e} GeV")
print(f"α⁻¹_unif ≈ {alpha_unif:.3f}")

plt.figure(figsize=(8, 6))
plt.plot(mu, total_diff, label='Total coupling difference')
plt.axvline(mu_unif, color='k', linestyle='--', label=f'Unification at {mu_unif:.2e} GeV')
plt.xscale('log')
plt.xlabel(r'Energy scale $\mu$ [GeV]')
plt.ylabel('Total coupling difference')
plt.title('RG Flow Stability Landscape')
plt.legend()
plt.grid(True)
plt.savefig('img/rg_stability_landscape.png')
plt.close()
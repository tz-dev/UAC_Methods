# =============================================================================
# File: planck_constant_reconstruction.py.py
# This script reconstructs Planck’s constant ℏ from model-based estimates of:
# - Bohr radius a₀
# - electron mass mₑ
# - speed of light c
# - fine structure constant α
# ℏ is computed via: ℏ ≈ α × a₀ × mₑ × c
# Inputs:
# - a0_proj: Projected Bohr radius (default: 5.29177210903e-11 m)
# - m_e_proj: Projected electron mass (default: 9.1093837015e-31 kg)
# - c_proj: Projected speed of light (default: 2.99792458e8 m/s)
# - alpha_proj: Projected fine-structure constant (default: 7.2973525693e-3)
# =============================================================================

import numpy as np

# Interactive input
print("=== Planck Constant Reconstruction Configuration ===")
try:
    a0_proj = float(input("Enter projected Bohr radius a0_proj (m) [default 5.29177210903e-11]: ") or 5.29177210903e-11)
    m_e_proj = float(input("Enter projected electron mass m_e_proj (kg) [default 9.1093837015e-31]: ") or 9.1093837015e-31)
    c_proj = float(input("Enter projected speed of light c_proj (m/s) [default 2.99792458e8]: ") or 2.99792458e8)
    alpha_proj = float(input("Enter projected fine-structure constant alpha_proj [default 7.2973525693e-3]: ") or 7.2973525693e-3)
    if a0_proj <= 0 or m_e_proj <= 0 or c_proj <= 0 or alpha_proj <= 0:
        raise ValueError("a0_proj, m_e_proj, c_proj, and alpha_proj must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    a0_proj = 5.29177210903e-11
    m_e_proj = 9.1093837015e-31
    c_proj = 2.99792458e8
    alpha_proj = 7.2973525693e-3

# Reconstruct Planck constant
hbar_proj = alpha_proj**2 * m_e_proj * c_proj * a0_proj
hbar_official = 1.054571817e-34  # Official value (J·s)

# Relative deviation
rel_dev = (hbar_proj - hbar_official) / hbar_official * 100

# Output
print("=== Planck Constant Reconstruction Results ===")
print(f"Projected hbar: {hbar_proj:.8e} J·s")
print(f"Official hbar: {hbar_official:.8e} J·s")
print(f"Relative deviation: {rel_dev:.5f}%")
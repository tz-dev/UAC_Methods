# ========================================================
# File: thomson_cross_section_projection.py
# Purpose: Calculate the Thomson scattering cross section using projected constants
# Method:
#   - Use projected fine-structure constant α, reduced Planck constant ħ, electron mass m_e, and speed of light c
#   - Calculate σ_T = (8π/3) * (α ħ / (m_e c))^2
#   - Compare with official Thomson cross section σ_T_official
# Inputs:
#   - alpha_proj: Fine-structure constant (default: 7.2973525693e-3)
#   - hbar_proj: Reduced Planck constant (default: 1.054571817e-34 J·s)
#   - m_e_proj: Electron mass (default: 9.1093837015e-31 kg)
#   - c: Speed of light (default: 2.99792458e8 m/s)
# Output:
#   - Print projected and official σ_T (m^2)
#   - Print relative deviation (%)
# ========================================================

import numpy as np

print("=== Thomson Cross Section Projection Configuration ===")
try:
    alpha_proj = float(input("Enter fine-structure constant alpha_proj [default 7.2973525693e-3]: ") or 7.2973525693e-3)
    hbar_proj = float(input("Enter reduced Planck constant hbar_proj (J·s) [default 1.054571817e-34]: ") or 1.054571817e-34)
    m_e_proj = float(input("Enter electron mass m_e_proj (kg) [default 9.1093837015e-31]: ") or 9.1093837015e-31)
    c = float(input("Enter speed of light c (m/s) [default 2.99792458e8]: ") or 2.99792458e8)
    if alpha_proj <= 0 or hbar_proj <= 0 or m_e_proj <= 0 or c <= 0:
        raise ValueError("All inputs must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    alpha_proj = 7.2973525693e-3
    hbar_proj = 1.054571817e-34
    m_e_proj = 9.1093837015e-31
    c = 2.99792458e8

# Calculate Thomson cross section
sigma_T = (8 * np.pi / 3) * (alpha_proj * hbar_proj / (m_e_proj * c))**2
sigma_T_official = 6.6524587158e-29  # m^2

# Relative deviation
rel_dev = (sigma_T - sigma_T_official) / sigma_T_official * 100

print("=== Thomson Cross Section Results ===")
print(f"Projected sigma_T: {sigma_T:.8e} m^2")
print(f"Official sigma_T: {sigma_T_official:.8e} m^2")
print(f"Relative deviation: {rel_dev:.5f}%")
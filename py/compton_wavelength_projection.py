# ========================================================
# File: compton_wavelength_projection.py
# Purpose: Calculate Compton wavelength using projected constants with full Planck constant h
# Method:
#   - Use projected ħ, electron mass m_e, speed of light c
#   - Calculate h = 2π ħ
#   - Calculate λ_C = h / (m_e c)
#   - Compare with official Compton wavelength λ_C_official
# Input:
#   - hbar: Reduced Planck constant (default: 1.054571817e-34 J·s)
#   - m_e: Electron mass (default: 9.1093837015e-31 kg)
#   - c: Speed of light (default: 2.99792458e8 m/s)
# Output:
#   - Print projected and official λ_C (m)
#   - Print relative deviation (%)
# ========================================================

import numpy as np

# Interactive input
print("=== Compton Wavelength Projection Configuration ===")
try:
    hbar = float(input("Enter reduced Planck constant hbar (J·s) [default 1.054571817e-34]: ") or 1.054571817e-34)
    m_e = float(input("Enter electron mass m_e (kg) [default 9.1093837015e-31]: ") or 9.1093837015e-31)
    c = float(input("Enter speed of light c (m/s) [default 2.99792458e8]: ") or 2.99792458e8)
    if hbar <= 0 or m_e <= 0 or c <= 0:
        raise ValueError("hbar, m_e, and c must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    hbar = 1.054571817e-34
    m_e = 9.1093837015e-31
    c = 2.99792458e8

# Calculate Compton wavelength
lambda_compton = hbar / (m_e * c)
lambda_official = 2.42631023867e-12  # Official value (m)

# Relative deviation
rel_dev = (lambda_compton - lambda_official) / lambda_official * 100

# Output
print("=== Compton Wavelength Results ===")
print(f"Projected Compton wavelength: {lambda_compton:.8e} m")
print(f"Official Compton wavelength: {lambda_official:.8e} m")
print(f"Relative deviation: {rel_dev:.5f}%")
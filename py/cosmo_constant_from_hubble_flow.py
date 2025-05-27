# ========================================================
# File: cosmo_constant_from_hubble_flow.py
# Purpose: Calculate cosmological constant Λ from projected Hubble constant
# Method:
#   - Use projected Hubble constant H0_proj from C.6.2
#   - Calculate Λ = 3 * H0_proj^2 / c^2
#   - Compare with official cosmological constant Λ_official
# Input:
# - Hubble constant H0_proj
# - Speed of light c (m/s) 
# Output:
#   - Print projected and official Λ (m^-2)
#   - Print relative deviation (%)
# ========================================================

import numpy as np

# Interaktive Eingaben
print("=== Cosmological Constant Calculation Configuration ===")
try:
    H0_proj = float(input("Enter projected Hubble constant H0_proj (1/s) [default 2.26908425e-18]: ") or 2.26908425e-18)
    c = float(input("Enter speed of light c (m/s) [default 2.99792458e8]: ") or 2.99792458e8)
    if H0_proj <= 0 or c <= 0:
        raise ValueError("H0_proj and c must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    H0_proj = 2.26908425e-18
    c = 2.99792458e8

# Calculate cosmological constant Λ
Lambda_proj = 3 * H0_proj**2 / c**2
Lambda_official = 1.1056e-52  # m^-2 (official value)

# Relative deviation calculation
rel_dev = (Lambda_proj - Lambda_official) / Lambda_official * 100

# Output
print("=== Cosmological Constant from Projected Hubble Constant ===")
print(f"Λ_proj = {Lambda_proj:.10e} m^-2")
print(f"Λ_official = {Lambda_official:.10e} m^-2")
print(f"Relative deviation: {rel_dev:.5f}%")
# =============================================================================
# File        : mass_and_g_projection.py
# Purpose     : Estimate gravitational constant G using model-derived ℏ, c, and Planck scale
# Formula     : G ≈ L_eff² · c³ / ħ
# Inputs:
# - hbar: Reduced Planck constant (default: 1.054571817e-34 J·s)
# - c: Speed of light (default: 2.99792458e8 m/s)
# - L_eff: Effective length scale (default: 1.616255e-35 m)
# Ouput:
# - Projected G
# - Official G
# - Relative deviation
# =============================================================================

import numpy as np

print("=== Gravitational Constant Projection Configuration ===")
try:
    hbar = float(input("Enter reduced Planck constant hbar (J·s) [default 1.054571817e-34]: ") or 1.054571817e-34)
    c = float(input("Enter speed of light c (m/s) [default 2.99792458e8]: ") or 2.99792458e8)
    L_eff = float(input("Enter effective length scale L_eff (m) [default 1.616255e-35]: ") or 1.616255e-35)
    if hbar <= 0 or c <= 0 or L_eff <= 0:
        raise ValueError("All inputs must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    hbar = 1.054571817e-34
    c = 2.99792458e8
    L_eff = 1.616255e-35

# Calculate gravitational constant
G = L_eff**2 * c**3 / hbar
G_official = 6.67430e-11  # m^3 kg^-1 s^-2

# Relative deviation
rel_dev = (G - G_official) / G_official * 100

print("=== Gravitational Constant Results ===")
print(f"Projected G: {G:.8e} m^3 kg^-1 s^-2")
print(f"Official G: {G_official:.8e} m^3 kg^-1 s^-2")
print(f"Relative deviation: {rel_dev:.5f}%")
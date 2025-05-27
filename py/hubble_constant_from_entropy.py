# ========================================================
# File: hubble_constant_from_entropy.py
# Purpose: Project the Hubble constant from entropic flow rate and scaling factor
# Method:
#   - Use Boltzmann constant, speed of light, universe age, and entropic timescale τ
#   - Calculate entropic flow rate S_dot = k_B / τ
#   - Calculate entropic volume V = c^3 * t_universe^2
#   - Compute projected Hubble constant H0_proj = (S_dot / V) * beta_H
#   - Compare with official Hubble constant H0_official
# Input: scaling factor beta_H, entropic timescale tau, universe age
#   - 
# Output:
#   - Print τ, S_dot, V, projected and official H0
#   - Print relative deviation (%)
# ========================================================

import numpy as np

# Interactive Input
print("=== Hubble Constant from Entropic Projection Configuration ===")
try:
    beta_H = float(input("Enter scaling factor beta_H [default 3.645e83]: ") or 3.645e83)
    tau = float(input("Enter entropic timescale tau (s) [default 4.35e17]: ") or 4.35e17)
    t_universe = float(input("Enter universe age t_universe (s) [default 4.35e17]: ") or 4.35e17)
    if tau <= 0 or t_universe <= 0:
        raise ValueError("tau and t_universe must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    beta_H = 3.645e83
    tau = t_universe = 4.35e17

# Physical constants
k_B = 1.380648e-23     # Boltzmann constant [J/K]
c = 2.99792458e8       # speed of light [m/s]

# Intermediate quantities
S_dot = k_B / tau      # entropic flow rate [J/s]
V = c**3 * t_universe**2  # entropic volume scale [m^3·s]

# Calculate projected Hubble constant
H0_proj = (S_dot / V) * beta_H
H0_official = 2.26854594e-18  # 1/s (official value)

# Relative deviation
rel_dev = (H0_proj - H0_official) / H0_official * 100

# Output
print("=== Hubble Constant from Entropic Projection ===")
print(f"τ = {tau:.3e} s")
print(f"Ṡ = {S_dot:.8e} J/s")
print(f"V = {V:.8e} m³·s")
print(f"H0 (projected) = {H0_proj:.8e} 1/s")
print(f"H0 (official)  = {H0_official:.8e} 1/s")
print(f"Relative deviation: {rel_dev:.5f}%")
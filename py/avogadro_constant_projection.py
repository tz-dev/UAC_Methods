# ========================================================
# File: avogadro_constant_projection.py
# Purpose: Estimate Avogadro's number from projected atomic mass unit scaling
# Method:
#   - Use projected atomic mass unit m_u_proj
#   - Calculate N_A_proj = 1 gram / m_u_proj
#   - Compare with official Avogadro number N_A_official
# Inputs:
#   - m_u: Atomic mass unit (default: 1.66053906660e-27 kg)
# Output:
#   - Print projected and official N_A
#   - Print relative deviation (%)
# ========================================================

import numpy as np

print("=== Avogadro Constant Projection Configuration ===")
try:
    m_u = float(input("Enter atomic mass unit m_u (kg) [default 1.66053906660e-27]: ") or 1.66053906660e-27)
    if m_u <= 0:
        raise ValueError("m_u must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    m_u = 1.66053906660e-27

# Calculate Avogadro's number
N_A = 1e-3 / m_u  # 1 g = 1e-3 kg
N_A_official = 6.02214076e23

# Relative deviation
rel_dev = (N_A - N_A_official) / N_A_official * 100

print("=== Avogadro Constant Results ===")
print(f"Projected N_A: {N_A:.8e}")
print(f"Official N_A: {N_A_official:.8e}")
print(f"Relative deviation: {rel_dev:.5f}%")
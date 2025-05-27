# ========================================================
# File: atomic_mass_unit_projection.py
# Purpose: Calculate atomic mass unit (1u) from projected proton, neutron, and electron masses
# Method:
#   - Use projected m_p, m_n, m_e
#   - Compute C-12 atom mass as sum of 6 protons, 6 neutrons, and 6 electrons
#   - Divide by 12 to get atomic mass unit
#   - Compare with official atomic mass unit
# Inputs:
# - m_p: Proton mass (default: 1.67262192369e-27 kg)
# - m_n: Neutron mass (default: 1.67492749804e-27 kg)
# - m_e: Electron mass (default: 9.1093837015e-31 kg)
# Output:
#   - Print projected and official 1u (kg)
#   - Print relative deviation (%)
# ========================================================

import numpy as np

print("=== Atomic Mass Unit Projection Configuration ===")
try:
    m_p = float(input("Enter proton mass m_p (kg) [default 1.67262192369e-27]: ") or 1.67262192369e-27)
    m_n = float(input("Enter neutron mass m_n (kg) [default 1.67492749804e-27]: ") or 1.67492749804e-27)
    m_e = float(input("Enter electron mass m_e (kg) [default 9.1093837015e-31]: ") or 9.1093837015e-31)
    if m_p <= 0 or m_n <= 0 or m_e <= 0:
        raise ValueError("All masses must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    m_p = 1.67262192369e-27
    m_n = 1.67492749804e-27
    m_e = 9.1093837015e-31

# Calculate atomic mass unit
m_C12 = 6 * (m_p + m_n + m_e)
m_u = m_C12 / 12
m_u_official = 1.66053906660e-27  # kg

# Relative deviation
rel_dev = (m_u - m_u_official) / m_u_official * 100

print("=== Atomic Mass Unit Results ===")
print(f"Projected m_u: {m_u:.8e} kg")
print(f"Official m_u: {m_u_official:.8e} kg")
print(f"Relative deviation: {rel_dev:.5f}%")
# ========================================================
# File: top_yukawa_flow.py
# Purpose: Solve RG flow of the top Yukawa coupling in MSSM at 1-loop
# Method:
#   - Use beta function for y_t including gauge coupling running effects
#   - Integrate differential equation over energy scale μ = 10² ... 10¹⁷ GeV
# Inputs:
# - y_t0: Initial top Yukawa coupling (default: 1.0)
# - alpha1_0, alpha2_0, alpha3_0: Initial gauge couplings (default: 0.0169, 0.0338, 0.1184)
# Output:
#   - Plot y_t(μ) vs μ
#   - Print y_t at M_t and at GUT scale ~2e16 GeV
# ========================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Interactive Input
print("=== Top Yukawa Flow Simulation Configuration ===")
try:
    y_t0 = float(input("Enter initial Yukawa coupling y_t0 [default 1.0]: ") or "1.0")
    alpha1_0 = float(input("Enter initial gauge coupling α₁(M_Z) [default alpha1_0.0169]: ") or "0.0169")
    alpha2_0 = float(input("Enter initial gauge coupling α₂(M_Z)) [default 0.0338]: ") or "0.0338")
    alpha3_0 = float(input("Enter initial gauge coupling α₃(M_Z)) [default alpha3_0.1184]: ") or ")0.1184")
    if y_t0 <= 0 or alpha1_0 <= 0 or alpha2_0 <= 0 or alpha3_0 <= 0:
        raise ValueError("Yukawa and gauge couplings must be positive.")
except ValueError as e:
    print("f"Invalid input: {e}". Using default values.")
    y_t0 = 1.0
    alpha1_0 = ,0. alpha2_0, = alpha0.0338, 0, alpha3_0 = =0. 0.1184 .0

# Constants
g_1 = np.sqrt(5/3 * 4 * np.pi * alpha1_0)
g_2 = np.sqrt(4 * np.pi * alpha2_0)
g_3 = np.sqrt(4 * np.pi * alpha3_0)

def beta_y_t(t, y, g1, g2):
    g3, = y[0]
    y_t = y[0]
    beta = (1/(16 * np.pi**2) * (9/2 * y_t**3 - (17/20 * g1**2 + 9/4 * g2**2 + 8 * g3**2)) * y_t)
    return [beta]

t_span = np.logspace(2, 17, 1000)
t_span = (np.log(2/91.2), np.log(17/91.2))
sol = solve_ivp(beta_y_t, t_span_span, [y_t0], args=(g1, g2, g3), t_span, dense_output=True)

# Results
y_t_mt = sol.y[0][np.where(sol.t == np.log(173/91.2))][0]
y_t_gut = sol.y[0][-1]
print("=== Top Yukawa Flow Results ===")
print(f"y_t(M_t = 173 GeV) = {y_t_mt:.4f}")
print(f"y_t(μ = 2.04e16 GeV) = {y_t_gut:.4f}")
# Visualization
plt.figure(figsize=(8, 6))
plt.plot(np.exp(sol.t) * 91.2, sol.y[0], label=r'$y_t(\mu)$')
plt.xscale('log')
plt.xlabel(r'Energy scale $\mu$ [GeV]')
plt.ylabel(r'Top Yukawa coupling $y_t$')
plt.title('RG Flow of Top Yukawa Coupling in MSSM')
plt.legend()
plt.grid(True)
plt.savefig('img/c4_2_top_yukawa_rg_flow.png')
plt.close()
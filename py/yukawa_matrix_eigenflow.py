# ========================================================
# File: yukawa_matrix_eigenflow.py
# Purpose: Compute RG flow of Yukawa matrix eigenvalues for up-type quarks
# Method:
#   - Initialize diagonal Yukawa matrix with realistic quark Yukawas at low scale
#   - Use simplified 1-loop RGE for diagonal elements
#   - Integrate and track eigenvalues over energy scale μ = 10² ... 10¹⁷ GeV
# Inputs:
# - Y0_diag: Diagonal elements of initial Yukawa matrix (default: [0.01, 0.04, 0.99])
# - A: RGE parameter A (default: 0.5)
# - B: RGE parameter B (default: 4.5/(16 * pi^2))
# Output:
#   - Plot eigenvalues λ_i(μ)
#   - Print eigenvalues at GUT scale
# ========================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Interactive input
print("=== Yukawa Matrix Eigenflow Configuration ===")
try:
    Y0_diag = []
    for i in range(3):
        val = float(input(f"Enter Yukawa matrix diagonal element Y0[{i}] [default {0.01 * 10**(2*i)}]: ") or 0.01 * 10**(2*i))
        Y0_diag.append(val)
    A = float(input("Enter RGE parameter A [default 0.5]: ") or 0.5)
    B = float(input("Enter RGE parameter B [default 0.01797]: ") or 4.5/(16 * np.pi**2))
    if any(y <= 0 for y in Y0_diag) or A < 0 or B < 0:
        raise ValueError("Yukawa elements, A, and B must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    Y0_diag = [0.01, 0.04, 0.99]
    A = 0.5
    B = 4.5/(16 * np.pi**2)

Y0 = np.diag(Y0_diag)

def beta_yukawa(t, y, A, B):
    Y = y.reshape(3, 3)
    dY_dt = np.zeros_like(Y)
    for i in range(3):
        dY_dt[i, i] = Y[i, i] * (A - B * Y[i, i]**2)
    return dY_dt.flatten()

t_span = (np.log(173/91.2), np.log(2.04e16/91.2))
sol = solve_ivp(beta_yukawa, t_span, Y0.flatten(), args=(A, B), dense_output=True)

# Extract eigenvalues
eigenvalues = []
t_eval = np.linspace(t_span[0], t_span[1], 100)
for t in t_eval:
    Y_t = sol.sol(t).reshape(3, 3)
    eigvals = np.linalg.eigvalsh(Y_t)
    eigenvalues.append(eigvals)
eigenvalues = np.array(eigenvalues)

print("=== Yukawa Eigenvalue Flow Results ===")
print(f"Eigenvalues at GUT scale (μ = 2.04e16 GeV): {eigenvalues[-1]}")

# Visualization
plt.figure(figsize=(8, 6))
for i in range(3):
    plt.plot(np.exp(t_eval) * 91.2, eigenvalues[:, i], label=f'λ_{i+1}')
plt.xscale('log')
plt.xlabel(r'Energy scale $\mu$ [GeV]')
plt.ylabel('Yukawa eigenvalues')
plt.title('RG Flow of Yukawa Matrix Eigenvalues')
plt.legend()
plt.grid(True)
plt.savefig('img/yukawa_eigenvalue_flow.png')
plt.close()
# ========================================================
# File: susy_parameter_variation.py
# Purpose: Simulate entropy-based mass splitting via SUSY projection
# Parameters:
#   - α_S = 0.015 (entropic scaling)
#   - ω = π (projection frequency)
#   - θ = π/4 (phase offset)
#   - Base mass = electron mass
# Inputs:
# - alpha_S: Scaling factor (default: 0.1)
# - omega: Frequency parameter (default: 0.5)
# - theta: Phase parameter (default: 0.0)
# - N: Number of samples (default: 10000)# Output:
#   - Mass histograms and projection states
# ========================================================
import numpy as np
import matplotlib.pyplot as plt

# Interactive Inputs
print("=== SUSY Parameter Variation Configuration ===")
try:
    alpha_S = float(input("Enter scaling factor alpha_S [default 0.1]: ") or 0.1)
    omega = float(input("Enter frequency omega [default 0.5]: ") or 0.5)
    theta = float(input("Enter phase theta [default 0.0]: ") or 0.0)
    N = int(input("Enter number of samples N [default 10000]: ") or 10000)
    if alpha_S <= 0 or omega <= 0 or N <= 0:
        raise ValueError("alpha_S, omega, and N must be positive.")
    if N > 100000:
        raise ValueError("N too large for performance.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default values.")
    alpha_S = 0.1
    omega = 0.5
    theta = 0.0
    N = 10000

np.random.seed(42)
m0 = 1e-27  # Reference mass (kg)
S = np.random.normal(loc=0, scale=1, size=N)
delta_m = alpha_S * m0 * np.sin(omega * S + theta)

m_susy = m0 + delta_m
m_susy_mean = np.mean(m_susy)
m_susy_std = np.std(m_susy)

print("=== SUSY Mass Splitting Results ===")
print(f"Mean SUSY mass: {m_susy_mean:.8e} kg")
print(f"Mass standard deviation: {m_susy_std:.8e} kg")

plt.figure(figsize=(8, 6))
plt.hist(m_susy, bins=50, color='purple', alpha=0.7)
plt.axvline(m_susy_mean, color='red', linestyle='--', label=f'Mean = {m_susy_mean:.2e}')
plt.title('SUSY Mass Splitting Distribution')
plt.xlabel('Mass (kg)')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('img/susy_mass_splitting.png')
plt.close()
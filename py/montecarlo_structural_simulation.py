# ========================================================
# File: montecarlo_structural_simulation.py
# Purpose: Simulate entropic lensing effect via Monte Carlo sampling of 2D entropy gradient field
# Method:
#   - Generate random 2D points in [-1,1]^2
#   - Define entropy field S(r) = exp(-r^2) centered at origin
#   - Compute numerical gradient of entropy field at sample points
#   - Normalize gradient vectors as approximate light ray directions
#   - Calculate lensing angles and statistics
# Input:
#   - number of Monte Carlo samples and the plot range for the x,y axes
# Output:
#   - Print mean and standard deviation of deviation angles in degrees
#   - Save quiver plot of entropic lensing rays
# ========================================================

import numpy as np
import matplotlib.pyplot as plt

# Interaktive Eingaben
print("=== Monte Carlo Entropic Lensing Configuration ===")
N = int(input("Enter number of samples [default 1000000]: ") or 1000000)
plot_range = float(input("Enter plot range for x,y axes [default 1.0]: ") or 1.0)

np.random.seed(42)
x = np.random.uniform(-plot_range, plot_range, N)
y = np.random.uniform(-plot_range, plot_range, N)

r = np.sqrt(x**2 + y**2)
S = np.exp(-r**2)

dS_dx = -2 * x * np.exp(-r**2)
dS_dy = -2 * y * np.exp(-r**2)

norm = np.sqrt(dS_dx**2 + dS_dy**2) + 1e-10
dx_ray = dS_dx / norm
dy_ray = dS_dy / norm

theta = np.arctan2(dy_ray, dx_ray)
theta_deg = np.degrees(theta)

theta_mean = np.mean(theta_deg)
theta_std = np.std(theta_deg)

print("=== Monte Carlo Entropic Lensing Prediction ===")
print(f"Samples: {N}")
print(f"Mean deviation angle: {theta_mean:.4f}°")
print(f"Standard deviation:   {theta_std:.4f}°")

plt.figure(figsize=(6, 6))
plt.quiver(x, y, dx_ray, dy_ray, color='blue', alpha=0.5, scale=20)
plt.title("Monte Carlo Entropic Lensing Rays")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.savefig("img/entropic_lensing_rays.png")
plt.show()
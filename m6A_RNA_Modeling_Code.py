
# m6A-mediated RNA Regulation Model
# Author: [Your Name]
# Description: This script implements a mathematical model for m6A-dependent RNA regulation
# based on a three-state system (Unmodified -> Modified -> Degraded) using an epidemic model analogy.

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from scipy.integrate import odeint

# -------------------------------
# 1. Define the ODE system
# -------------------------------
def rna_model(y, t, alpha, beta, gamma, delta):
    u, m, d = y
    du = -alpha * u + beta * m - delta * u
    dm = alpha * u - (beta + gamma) * m
    dd = delta * u + gamma * m
    return [du, dm, dd]

# -------------------------------
# 2. Parameters and initial conditions
# -------------------------------
alpha = 0.4  # Methylation rate
beta = 0.2   # Demethylation rate
gamma = 0.3  # Decay of modified RNA
delta = 0.1  # Basal decay of unmodified RNA
y0 = [1.0, 0.0, 0.0]  # Initial fractions of [U, M, D]
time = np.linspace(0, 20, 200)

# Solve ODE
solution = odeint(rna_model, y0, time, args=(alpha, beta, gamma, delta))
u, m, d = solution.T

# -------------------------------
# 3. Plot simulation results
# -------------------------------
plt.figure(figsize=(8, 5))
plt.plot(time, u, label="Unmodified (U)", linewidth=2)
plt.plot(time, m, label="m6A Modified (M)", linewidth=2)
plt.plot(time, d, label="Degraded (D)", linewidth=2)
plt.title("Simulation of mRNA Dynamics")
plt.xlabel("Time (arbitrary units)")
plt.ylabel("Fraction of mRNA")
plt.legend()
plt.grid(True)
plt.savefig("simulation_results.png")
plt.show()

# -------------------------------
# 4. Conceptual Model Diagram
# -------------------------------
G = nx.DiGraph()
G.add_nodes_from(["Unmodified (U)", "Modified (M)", "Degraded (D)"])
edges = [
    ("Unmodified (U)", "Modified (M)", "α"),
    ("Modified (M)", "Unmodified (U)", "β"),
    ("Unmodified (U)", "Degraded (D)", "δ"),
    ("Modified (M)", "Degraded (D)", "γ")
]
G.add_edges_from([(u, v) for u, v, l in edges])
pos = {"Unmodified (U)": (-1, 0), "Modified (M)": (1, 0), "Degraded (D)": (0, -1.5)}

plt.figure(figsize=(7, 5))
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=4000, font_size=10, arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): l for u, v, l in edges})
plt.title("Conceptual Model of m6A-mediated RNA Regulation")
plt.savefig("conceptual_model.png")
plt.show()

 #Exercice 4
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
r = 2
a = 0.05
beta = 1
generations = 30
host_pop = [20]
parasitoid_pop = [2]

# Modèle
for t in range(generations):
    H_next = host_pop[-1] * np.exp(-a * parasitoid_pop[-1]) * r
    P_next = host_pop[-1] * (1 - np.exp(-a * parasitoid_pop[-1])) * beta
    host_pop.append(H_next)
    parasitoid_pop.append(P_next)

# Graphique
time = range(generations + 1)
plt.plot(time, host_pop, label="Hôtes")
plt.plot(time, parasitoid_pop, label="Parasitoïdes")
plt.xlabel("Temps (générations)")
plt.ylabel("Population")
plt.legend()
plt.title("Modèle de Nicholson-Bailey")
plt.show()
 #Exercice 3
import numpy as np
from scipy.stats import norm

def correlation_test(X, Y, r0):
    n = len(X)
    r = np.corrcoef(X, Y)[0, 1]
    Z = 0.5 * np.log((1 + r) / (1 - r))
    Z0 = 0.5 * np.log((1 + r0) / (1 - r0))
    T = (Z - Z0) * np.sqrt(n - 3)
    p_value = 2 * (1 - norm.cdf(abs(T)))
    return r, p_value

# Exemple de données
X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]

# Tests
r, p0 = correlation_test(X, Y, 0)
print(f"Corrélation: {r}, p-valeur pour r0=0: {p0}")
r, p6 = correlation_test(X, Y, 0.6)
print(f"Corrélation: {r}, p-valeur pour r0=0.6: {p6}")

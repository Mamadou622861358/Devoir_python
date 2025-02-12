#Exercice 2
import numpy as np

BOS = [2.67, 1.00, 1.21, 3.09, 3.43, 4.71, 3.88, 3.08, 4.10, 2.62, 1.01, 5.93]
MER = [6.83, 3.63, 7.20, 2.68, 2.05, 2.96, 1.04, 0.00, 0.03, 6.71, 8.28, 6.85]

# Calcul des précipitations totales et moyennes
total_BOS = sum(BOS)
mean_BOS = np.mean(BOS)
total_MER = sum(MER)
mean_MER = np.mean(MER)

# Mois où les précipitations sont supérieures à la moyenne
months_above_mean_BOS = [i + 1 for i, val in enumerate(BOS) if val > mean_BOS]
months_above_mean_MER = [i + 1 for i, val in enumerate(MER) if val > mean_MER]

# Mois où les précipitations de Boston sont inférieures à celles de Seattle
months_BOS_less_MER = [i + 1 for i, (b, m) in enumerate(zip(BOS, MER)) if b < m]

print(f"Total BOS: {total_BOS}, Moyenne BOS: {mean_BOS}")
print(f"Total MER: {total_MER}, Moyenne MER: {mean_MER}")
print(f"Mois > Moyenne BOS: {months_above_mean_BOS}")
print(f"Mois > Moyenne MER: {months_above_mean_MER}")
print(f"Mois BOS < MER: {months_BOS_less_MER}")
import matplotlib.pyplot as plt

from pret import estimation_pret
import locale
locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'

# on fait une liste de revenu entre 1400€ et 5000€ par tranche de 25€
x = [a for a in range(1400, 5000, 25)]
y = []
y2 = []
y3 = []
for i in x:
    pret_possible = estimation_pret.pret_max_en_fonction_du_salaire(i, 2/100/12, 25)
    y.append(pret_possible)
    y2.append(pret_possible*.1)
    y3.append(pret_possible*1.1)

fig, ax = plt.subplots()
ax.plot(x, y, 'r') # emprunt possible
ax.plot(x, y2, 'g') # apport conseillé
ax.plot(x, y3, color = 'blue', linestyle='dashed') # argent total
ax.format_coord = lambda x,y: f"x={round(x,2):n}, y={round(y,2):n}"

plt.show() # affiche la figure à l'écran
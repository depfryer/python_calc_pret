import matplotlib.pyplot as plt

from pret import estimation_pret
import locale
locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'


x = [a for a in range(40, 400, 10)]
y = []

for i in x:
    duree_pret = estimation_pret.duree_emprunt_max_mois(6500, 4.62/100, i)
    y.append(duree_pret)

fig, ax = plt.subplots()
ax.plot(x, y, 'r') 
ax.format_coord = lambda x,y: f"x={round(x,2):n}, y={round(y,2):n}"

plt.show() # affiche la figure à l'écran
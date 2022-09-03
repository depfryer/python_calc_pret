from beautifultable import BeautifulTable
from pret import estimation_pret, pret


# pret initial
a = pret(valeur_initial=3500, taux_annuel=4.62/100, duree_mois=48)
print('='*8, 'plan initial', '='*8, '\n')
print("emprunt : ", a.valeur_initial)
print("taux annuel : ", a.taux_annuel)
print("duree en mois prevu : ", a.duree_mois)
print("mensualité prevu", round(a._mensualite, 2))


print('='*30, '\n')



tableau_remboursement = [
    (0, -3000),
]
r, interet_payer = a.remboursement_en_avance(tableau_remboursement)


print('changment dans le temps')
table1 = BeautifulTable()
table1.columns.header = ["MOIS", "changement"]
for i in tableau_remboursement:
    table1.rows.append(i)


table = BeautifulTable()

table.columns.header = ["MOIS", "RESTANT",
                        "PAYER", "INTERET"]

table.set_style(BeautifulTable.STYLE_COMPACT)
table.columns.alignment['MOIS'] = BeautifulTable.ALIGN_RIGHT
# table.columns.alignment['RESTANT'] = BeautifulTable.ALIGN_LEFT
# table.columns.alignment['PAYER'] = BeautifulTable.ALIGN_LEFT
# table.columns.alignment['INTERET'] = BeautifulTable.ALIGN_LEFT
for i in r:
    table.rows.append(i)

print(table1)
print(table)
print('interet finalement payer : ', round(interet_payer, 2))

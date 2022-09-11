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
tableau_mensualite = [
    (0, 100),
]
mois_debut = 9
annee_debut = 2022

r, interet_payer = a.remboursement_en_avance(tableau_remboursement, tableau_mensualite)


table1 = BeautifulTable()
table1.columns.header = ["MOIS", "changement"]
for i in tableau_remboursement:
    table1.rows.append(i)



table2 = BeautifulTable()
table2.columns.header = ["MOIS", "changement"]
for i in tableau_mensualite:
    table2.rows.append(i)


table = BeautifulTable()



mois = ('janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre')

table.columns.header = ["DATE", "MOIS", "RESTANT",
                        "PAYER", "INTERET"]

table.set_style(BeautifulTable.STYLE_COMPACT)
table.columns.alignment['MOIS'] = BeautifulTable.ALIGN_RIGHT
table.columns.alignment['DATE'] = BeautifulTable.ALIGN_LEFT
# table.columns.alignment['PAYER'] = BeautifulTable.ALIGN_LEFT
# table.columns.alignment['INTERET'] = BeautifulTable.ALIGN_LEFT

a = mois_debut
for i in r:

    table.rows.append([f"{mois[a%12]} {annee_debut}"]+  list(i))
    a+= 1
    if(a%12 ==1 ):
        annee_debut +=1

print('changement du capital')
print(table1)

print('changement des mensualité')
print(table2)
print(table)
print('interet finalement payer : ', round(interet_payer, 2))

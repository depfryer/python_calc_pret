import unittest
from unittest import result
from pret import estimation_pret


class test_estimation_pret(unittest.TestCase):
    
    def test_emprunt_max_possible(self):
        result = estimation_pret.emprunt_max_possible(interet_annuel=12*0.4/100, mensualite=973.44, duree_mois=20*12)
        # dummypret = pret(type_de_pret=0,valeur_initial=150000, taux_annuel=12*0.4/100, duree_mois=20*12)
        self.assertEqual(round(result), 150001)

    def test_duree_emprunt_max_mois(self):
        result = estimation_pret.duree_emprunt_max_mois(emprunt=150000, interet_annuel=12*0.4/100, mensualite=973.44)
        self.assertEqual(round(result), 20*12)

    def test_pret_max_en_fonction_du_salaire(self):
        result = estimation_pret.pret_max_en_fonction_du_salaire(salaire_net=1500, interet_annuel=2/100, duree_annee=20)
        self.assertEqual(round(result), 88953)

if __name__ == '__main__':
    unittest.main()
import unittest
from pret import pret


class test_pret(unittest.TestCase):


    
    def test_mensualite(self):
        dummypret = pret(type_de_pret=0,valeur_initial=150000, taux_annuel=12*0.4/100, duree_mois=20*12)
        self.assertEqual(dummypret.calcul_mensualite(), 973.44)

    def test_total_interet(self):
        dummypret = pret(type_de_pret=0,valeur_initial=150000, taux_annuel=12*0.4/100, duree_mois=20*12)
        self.assertEqual(dummypret.calcul_total_interet(), 83624.69)

    def test_total(self):
        dummypret = pret(type_de_pret=0,valeur_initial=150000, taux_annuel=12*0.4/100, duree_mois=20*12)
        self.assertEqual(dummypret.calcul_total(), 233624.69) # 83624.69 + 150000
    def test_mensuel(self):
        dummypret = pret(type_de_pret=0,valeur_initial=150000, taux_annuel=12*0.4/100, duree_mois=20*12)
        with open(".//test//test_pret_calculparmois.txt", "r") as f:
            self.assertEqual(str(dummypret.calcul_par_mois()),f.readline() ) 

if __name__ == '__main__':
    unittest.main()
from . import pret
from . import estimation_pret

class rachat_credit:
    def __init__(self, credit_original: pret,nombre_de_mois_ecoule:int, nouveau_taux: float) -> None:
        deja_payer = credit_original.calcul_par_mois()[nombre_de_mois_ecoule-1][1]
        self.reste_a_payer = (credit_original.get_valeur_initial() - deja_payer)
        self.remboursement_anticipe = self.reste_a_payer*3/100
        self.a= estimation_pret.duree_emprunt_max_mois(self.reste_a_payer +self.remboursement_anticipe, nouveau_taux, credit_original.calcul_mensualite())
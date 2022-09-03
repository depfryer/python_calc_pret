from math import log
from pret import pret

class estimation_pret:
    def emprunt_max_possible(interet_annuel :float, mensualite:float, duree_mois:int):
        # return mensualite/duree_mois *(1-(1/(1+duree_mois)**interet))
        interet = interet_annuel/12
        return mensualite * (((1 + interet)**duree_mois - 1)/(interet * (1+interet) ** duree_mois ))


    def duree_emprunt_max_mois(emprunt:int, interet_annuel:float, mensualite:int):
        '''
        emprunt : valeur voulant etre emprunter

        interet en taux annuel

        mensualite mensualité voulu par mois
        '''
        interet = interet_annuel/12
        return ((log(mensualite)- log(mensualite - interet * emprunt))/ (log(1+interet)))

    def pret_max_en_fonction_du_salaire(salaire_net:int, interet_annuel:float,  duree_annee:int):
        return estimation_pret.emprunt_max_possible(interet_annuel, salaire_net*.30, duree_annee*12)
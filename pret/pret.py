from decimal import *


class pret:

    def __init__(self, valeur_initial: int, taux_annuel: float, duree_mois: int, type_de_pret: int = 0, mois_ecoule: int = 0) -> None:
        """
        __init__ _summary_

        _extended_summary_

        Args:
            valeur_initial (int, optional): somme de depart du pret. Defaults to None.
            taux_annuel (float, optional): valeur du taux annuel 4% -> 0.04. Defaults to None.
            duree_mois (int, optional): duree du pret en mois. Defaults to None.
            type_de_pret (int, optional): type de pret, si proportionnel(0) ou actuariel(1). Defaults to proportionnel.
            mois_ecoule (int, optional): nombre de mois deja payer. Defaults to 0.
        """
        self._type_de_pret = type_de_pret
        self._taux_annuel = self._calcul_taux_pret_annuel(taux_annuel)
        self._valeur_initial = valeur_initial
        self._duree_mois = duree_mois
        self._mois_ecoule = mois_ecoule
        self._actualiser()

    def _calcul_taux_pret_annuel(self, taux_annuel):
        '''
        le "taux" peut changer en fonction de si c'est un pret proportionnelle ou actuarielle 
        proportionnelle =  taux /12
        actuarielle = taux variable sur l'année
        '''
        if self._type_de_pret == 0:
            return taux_annuel
        elif self._type_de_pret == 1:
            return (1 + taux_annuel)**12-1
        else:
            raise AttributeError

    def calcul_total_interet(self) -> float:
        """
        calcul_total _summary_

        permet de calculer le totat payer 

        Returns:
            float : somme total a remboursé
        """
        self.valeur_total_interet = self._duree_mois * \
            self._mensualite - self._valeur_initial
        return round(self.valeur_total_interet, 2)

    def calcul_mensualite(self) -> float:
        """
        calcul_mensualite _summary_

        permet de calculer les mensualite constante

        Returns:
            float: somme a payer mensuellement (arrondi)
        """
        self._mensualite = self._valeur_initial * (self._taux_annuel/12) / \
            (1-(1 + self._taux_annuel/12) ** -self._duree_mois)
        return round(self._mensualite, 2)


    def calcul_total(self) -> float:
        """
        calcul_total _summary_

        permet de calculer le totat payer a la fin du pret 

        Returns:
            float : somme total a remboursé
        """
        self._valeur_total = self._duree_mois * (self._mensualite)
        return round(self._valeur_total, 2)

    def calcul_par_mois(self):
        restant_a_payer = self._valeur_initial
        charge_mensuel = self._mensualite
        mois=[]
        for i in range(self._duree_mois):
            interet_du_mois = restant_a_payer*(self._taux_annuel/12)
            mois.append(
                (i, round(restant_a_payer,2), round(charge_mensuel,2), round(interet_du_mois,2))
            ) 
            restant_a_payer -= charge_mensuel - interet_du_mois
        return mois

    def remboursement_en_avance(self, tableau_remboursement:list, changement_mensualite:dict):
        charge_mensuel = round(self._mensualite, 2)
        restant_a_payer = self._valeur_initial
        mois=[]
        mois_en_cours = 0
        interet_payer =0
        while charge_mensuel <= restant_a_payer:
            # on regarde si un changement a eu lieu au cours du mois
            rembousement_avance = tableau_remboursement.get(mois_en_cours, 0)
            restant_a_payer -= rembousement_avance
            charge_mensuel = changement_mensualite.get(mois_en_cours, charge_mensuel)

            # calcul des interet 
            interet_du_mois = round(restant_a_payer*(self._taux_annuel/12), 2)
            interet_payer += interet_du_mois
            # on rajoute dans le tableau la mensualité payer
            mois.append(
                (mois_en_cours, restant_a_payer, charge_mensuel + rembousement_avance, interet_du_mois)
            )
            # actualisation des données pour le mois suivant
            restant_a_payer -= round(charge_mensuel - interet_du_mois, 2)
            
            mois_en_cours+=1
        
        interet_du_mois = restant_a_payer*(self._taux_annuel/12)
        interet_payer += interet_du_mois
        
        mois.append((mois_en_cours, round(restant_a_payer,2), round(restant_a_payer,2), round(interet_du_mois,2)))
        return mois, interet_payer

    def calcul_dernier_mois(self):
        raise NotImplemented
    def _actualiser(self):
        self.calcul_mensualite()
        self.calcul_total()
        self.calcul_total_interet()

    def get_type_de_pret(self):
        return self._type_de_pret
    def get_taux_annuel(self):
        return self._taux_annuel
    def get_valeur_initial(self):
        return self._valeur_initial
    def get_duree_mois(self):
        return self._duree_mois
    def get_mois_ecoule(self):
        return self._mois_ecoule


    def set_type_de_pret(self, a):
        self._type_de_pret = a
        self._actualiser()
    def set_taux_annuel(self, a):
        self._taux_annuel = a
        self._actualiser()
    def set_valeur_initial(self, a):
        self._valeur_initial = a
        self._actualiser()
    def set_duree_mois(self, a):
        self._duree_mois = a
        self._actualiser()
    def set_mois_ecoule(self, a):
        self._mois_ecoule = a

    def del_error():
        raise ReferenceError

    type_de_pret = property(get_type_de_pret, set_type_de_pret, del_error)
    taux_annuel = property(get_taux_annuel, set_taux_annuel, del_error)
    valeur_initial = property(get_valeur_initial, set_valeur_initial, del_error)
    duree_mois = property(get_duree_mois, set_duree_mois, del_error)
    mois_ecoule = property(get_mois_ecoule, set_mois_ecoule, del_error)
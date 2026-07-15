
class Produit:
    """Classe representant un produit du stock"""

    def __init__(self, id_produit, nom, categorie, prix, quantite, fournisseur):
        self.__id_produit = id_produit
        self.__nom = nom
        self.__categorie = categorie
        self.__prix = prix
        self.__quantite = quantite
        self.__fournisseur = fournisseur

    # --- Getters ---
    def get_id_produit(self):
        return self.__id_produit

    def get_nom(self):
        return self.__nom

    def get_categorie(self):
        return self.__categorie

    def get_prix(self):
        return self.__prix

    def get_quantite(self):
        return self.__quantite

    def get_fournisseur(self):
        return self.__fournisseur

    # --- Setters ---
    def set_nom(self, nom):
        self.__nom = nom

    def set_categorie(self, categorie):
        self.__categorie = categorie

    def set_prix(self, prix):
        self.__prix = prix

    def set_quantite(self, quantite):
        self.__quantite = quantite

    def set_fournisseur(self, fournisseur):
        self.__fournisseur = fournisseur

    # Methode pour convertir l'objet en dictionnaire pour le CSV DictWriter
    def to_dict(self):
        return {
            "ID_Produit": self.__id_produit,
            "Nom": self.__nom,
            "Categorie": self.__categorie,
            "Prix": self.__prix,
            "Quantite": self.__quantite,
            "Fournisseur": self.__fournisseur
        }

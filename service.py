import csv
import os
from modele import Produit

class GestionStockCSV:
    """Classe gerant les operations CRUD sur le fichier CSV"""

    FICHIER_CSV = "stock.csv"
    EN_TETES = ["ID_Produit", "Nom", "Categorie", "Prix", "Quantite", "Fournisseur"]

    def __init__(self):
        # Creer le fichier s'il n'existe pas avec les en-tetes
        if not os.path.exists(self.FICHIER_CSV):
            with open(self.FICHIER_CSV, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.EN_TETES)
                writer.writeheader()

    def ajouter_produit(self, produit):
        """ Ajoute un produit au fichier CSV"""
        with open(self.FICHIER_CSV, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.EN_TETES)
            writer.writerow(produit.to_dict())

    def get_tous_les_produits(self):
        """Lit et retourne tous les produits sous forme de liste d'objets Produit"""
        produits = []
        with open(self.FICHIER_CSV, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                produit = Produit(
                    row["ID_Produit"], row["Nom"], row["Categorie"],
                    float(row["Prix"]), int(row["Quantite"]), row["Fournisseur"]
                )
                produits.append(produit)
        return produits

    def rechercher_produits(self, critere, valeur):
        """Recherche par nom, categorie ou fournisseur"""
        produits = self.get_tous_les_produits()
        resultat = []
        for p in produits:
            if critere == "Nom" and valeur.lower() in p.get_nom().lower():
                resultat.append(p)
            elif critere == "Categorie" and valeur.lower() in p.get_categorie().lower():
                resultat.append(p)
            elif critere == "Fournisseur" and valeur.lower() in p.get_fournisseur().lower():
                resultat.append(p)
        return resultat

    def supprimer_produit(self, id_produit):
        produits = self.get_tous_les_produits()
        produits_restants = []
        for produit in produits:
            if produit.get_id_produit() != id_produit:
                produits_restants.append(produit)

        with open(self.FICHIER_CSV, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.EN_TETES)
            writer.writeheader()
            for p in produits_restants:
                writer.writerow(p.to_dict())

    def modifier_produit(self, produit_modifie):
        produits = self.get_tous_les_produits()
        for i in range(len(produits)):
            if produits[i].get_id_produit() == produit_modifie.get_id_produit():
                produits[i] = produit_modifie
                break

        with open(self.FICHIER_CSV, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.EN_TETES)
            writer.writeheader()
            for p in produits:
                writer.writerow(p.to_dict())

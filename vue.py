# Copyright © DEV103 — Ahmed Karkach and Mohamed OUELD EL GHABA OFPPT

import tkinter as tk
from tkinter import ttk, messagebox
from service import GestionStockCSV
from modele import Produit

# Couleurs de l'application
BG_COLOR = "#F8F9FA"
PANEL_COLOR = "#FFFFFF"
PRIMARY_COLOR = "#1E293B"
ACCENT_COLOR = "#2563EB"
SUCCESS_COLOR = "#16A34A"
WARNING_COLOR = "#D97706"
DANGER_COLOR = "#DC2626"
TEXT_COLOR = "#1E293B"
LIGHT_GRAY = "#E2E8F0"

ACCENT_ACTIVE = "#1D4ED8"
SUCCESS_ACTIVE = "#15803D"
WARNING_ACTIVE = "#B45309"
DANGER_ACTIVE = "#B91C1C"
PRIMARY_ACTIVE = "#0F172A"
NEUTRAL_ACTIVE = "#CBD5E1"

# Polices utilisées dans l'application
FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_SUBTITLE = ("Segoe UI", 11, "bold")
FONT_LABEL = ("Segoe UI", 10)
FONT_ENTRY = ("Segoe UI", 10)
FONT_BUTTON = ("Segoe UI", 10, "bold")
FONT_TREE = ("Segoe UI", 10)


class ApplicationTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Stock - Projet POO Tkinter")
        self.root.geometry("1000x650")
        self.root.minsize(750, 520)
        self.root.configure(bg=BG_COLOR)

        self.configurer_style()

        self.gestionnaire = GestionStockCSV()

        self.frame_login = tk.Frame(self.root, bg=BG_COLOR)
        self.frame_login.pack(expand=True)
        self.creer_widgets_login()
        self.entry_user.focus_set()

    def configurer_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background=PANEL_COLOR,
                        foreground=TEXT_COLOR,
                        rowheight=30,
                        fieldbackground=PANEL_COLOR,
                        font=FONT_TREE,
                        borderwidth=0)

        style.configure("Treeview.Heading",
                        background=PRIMARY_COLOR,
                        foreground="white",
                        font=FONT_SUBTITLE,
                        borderwidth=0,
                        padding=5)


        style.map("Treeview",
                  background=[("selected", ACCENT_COLOR)],
                  foreground=[("selected", "white")])

        style.configure("Accent.TButton", background=ACCENT_COLOR, foreground="white",
                        font=FONT_BUTTON, borderwidth=0, padding=(10, 6))
        style.map("Accent.TButton", background=[("active", ACCENT_ACTIVE), ("pressed", ACCENT_ACTIVE)])

        style.configure("Success.TButton", background=SUCCESS_COLOR, foreground="white",
                        font=FONT_BUTTON, borderwidth=0, padding=(10, 6))
        style.map("Success.TButton", background=[("active", SUCCESS_ACTIVE), ("pressed", SUCCESS_ACTIVE)])

        style.configure("Warning.TButton", background=WARNING_COLOR, foreground="white",
                        font=FONT_BUTTON, borderwidth=0, padding=(10, 6))
        style.map("Warning.TButton", background=[("active", WARNING_ACTIVE), ("pressed", WARNING_ACTIVE)])

        style.configure("Danger.TButton", background=DANGER_COLOR, foreground="white",
                        font=FONT_BUTTON, borderwidth=0, padding=(10, 6))
        style.map("Danger.TButton", background=[("active", DANGER_ACTIVE), ("pressed", DANGER_ACTIVE)])

        style.configure("Neutral.TButton", background=LIGHT_GRAY, foreground=TEXT_COLOR,
                        font=FONT_BUTTON, borderwidth=0, padding=(10, 6))
        style.map("Neutral.TButton", background=[("active", NEUTRAL_ACTIVE), ("pressed", NEUTRAL_ACTIVE)])

        style.configure("Primary.TButton", background=PRIMARY_COLOR, foreground="white",
                        font=FONT_BUTTON, borderwidth=0, padding=(10, 6))
        style.map("Primary.TButton", background=[("active", PRIMARY_ACTIVE), ("pressed", PRIMARY_ACTIVE)])

    # Page de connexion
    def creer_widgets_login(self):
        carte_login = tk.Frame(self.frame_login, bg=PRIMARY_COLOR, padx=2, pady=2)
        carte_login.pack(expand=True)

        carte_interieure = tk.Frame(carte_login, bg=PANEL_COLOR, padx=40, pady=30)
        carte_interieure.pack()

        tk.Label(carte_interieure, text="🔒 Connexion Sécurisée", font=FONT_TITLE, bg=PANEL_COLOR, fg=PRIMARY_COLOR).grid(row=0, column=0, columnspan=2, pady=(0, 25))

        tk.Label(carte_interieure, text="Nom d'utilisateur :", font=FONT_LABEL, bg=PANEL_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, sticky="w", pady=5)
        self.entry_user = tk.Entry(carte_interieure, font=FONT_ENTRY, relief="flat", bg=BG_COLOR, highlightthickness=1, highlightcolor=ACCENT_COLOR)
        self.entry_user.grid(row=2, column=0, pady=(0, 15), ipady=5)

        tk.Label(carte_interieure, text="Mot de passe :", font=FONT_LABEL, bg=PANEL_COLOR, fg=TEXT_COLOR).grid(row=3, column=0, sticky="w", pady=5)
        self.entry_mdp = tk.Entry(carte_interieure, show="*", font=FONT_ENTRY, relief="flat", bg=BG_COLOR, highlightthickness=1, highlightcolor=ACCENT_COLOR)
        self.entry_mdp.grid(row=4, column=0, pady=(0, 25), ipady=5)

        btn_connexion = ttk.Button(carte_interieure, text="Se connecter", command=self.verifier_connexion,
                                   style="Accent.TButton", cursor="hand2")
        btn_connexion.grid(row=5, column=0)
        self.entry_user.bind("<Return>", lambda _event: self.verifier_connexion())
        self.entry_mdp.bind("<Return>", lambda _event: self.verifier_connexion())

    def verifier_connexion(self):
        user = self.entry_user.get()
        mdp = self.entry_mdp.get()

        if user == "admin" and mdp == "admin123":
            self.frame_login.destroy()
            self.creer_interface_principale()
        else:
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect !")
            self.entry_mdp.delete(0, tk.END)
            self.entry_mdp.focus_set()

    # Page principale
    def creer_interface_principale(self):
        self.frame_principal = tk.Frame(self.root, bg=BG_COLOR)
        self.frame_principal.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        self.frame_principal.columnconfigure(0, weight=0)
        self.frame_principal.columnconfigure(1, weight=1)
        self.frame_principal.rowconfigure(1, weight=1)

        # Titre de l'application
        header = tk.Frame(self.frame_principal, bg=BG_COLOR)
        header.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        tk.Label(header, text="📦 Gestion des Produits", font=("Segoe UI", 20, "bold"), bg=BG_COLOR, fg=PRIMARY_COLOR).pack(side=tk.LEFT)

        # Formulaire pour saisir un produit
        cadre_form = tk.Frame(self.frame_principal, bg=PRIMARY_COLOR, padx=1, pady=1) # Ombre
        cadre_form.grid(row=1, column=0, sticky="ns", padx=(0, 15))

        self.frame_form = tk.Frame(cadre_form, bg=PANEL_COLOR, padx=20, pady=20)
        self.frame_form.pack()

        tk.Label(self.frame_form, text="Formulaire", font=FONT_SUBTITLE, bg=PANEL_COLOR, fg=PRIMARY_COLOR).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 15))

        labels = ["ID_Produit :", "Nom :", "Catégorie :", "Prix :", "Quantité :", "Fournisseur :"]
        categories = [
            "Alimentation", "Boissons", "Électronique", "Informatique",
            "Vêtements", "Maison", "Beauté", "Papeterie", "Autre"
        ]
        self.entries = {}

        for i in range(len(labels)):
            text = labels[i]
            tk.Label(self.frame_form, text=text, font=FONT_LABEL, bg=PANEL_COLOR, fg=TEXT_COLOR).grid(row=i+1, column=0, sticky="w", pady=4)
            if text == "Catégorie :":
                entry = ttk.Combobox(self.frame_form, values=categories, font=FONT_ENTRY,
                                     width=23, state="normal")
            else:
                entry = tk.Entry(self.frame_form, font=FONT_ENTRY, width=25, relief="flat",
                                 bg=BG_COLOR, highlightthickness=1, highlightcolor=ACCENT_COLOR)
            entry.grid(row=i+1, column=1, pady=4, ipady=3, padx=(10, 0))
            self.entries[text] = entry

        self.entries["ID_Produit :"].config(state="readonly", highlightthickness=0, bg=LIGHT_GRAY)


        frame_btn = tk.Frame(self.frame_form, bg=PANEL_COLOR)
        frame_btn.grid(row=8, column=0, columnspan=2, pady=(20, 0))

        ttk.Button(frame_btn, text="➕ Ajouter", command=self.ajouter,
                   style="Success.TButton", cursor="hand2", width=22).pack(pady=3)
        ttk.Button(frame_btn, text="✏️ Modifier", command=self.modifier,
                   style="Warning.TButton", cursor="hand2", width=22).pack(pady=3)
        ttk.Button(frame_btn, text="🗑️ Supprimer", command=self.supprimer,
                   style="Danger.TButton", cursor="hand2", width=22).pack(pady=3)
        ttk.Button(frame_btn, text="🧹 Effacer les champs", command=self.effacer_champs,
                   style="Neutral.TButton", cursor="hand2", width=22).pack(pady=3)


        # Zone de recherche et tableau
        frame_droit = tk.Frame(self.frame_principal, bg=BG_COLOR)
        frame_droit.grid(row=1, column=1, sticky="nsew")
        frame_droit.columnconfigure(0, weight=1)
        frame_droit.rowconfigure(1, weight=1)

        # Recherche d'un produit
        cadre_search = tk.Frame(frame_droit, bg=PRIMARY_COLOR, padx=1, pady=1)
        cadre_search.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        frame_search = tk.Frame(cadre_search, bg=PANEL_COLOR, padx=10, pady=10)
        frame_search.pack(fill=tk.X)
        frame_search.columnconfigure(2, weight=1)

        tk.Label(frame_search, text="🔍", font=("Segoe UI", 12), bg=PANEL_COLOR).grid(row=0, column=0, sticky="w")
        self.var_recherche = tk.StringVar(value="Nom")
        ttk.Combobox(frame_search, textvariable=self.var_recherche,
                     values=["Nom", "Categorie", "Fournisseur"], width=12,
                     state="readonly", font=FONT_ENTRY).grid(row=0, column=1, padx=(5, 10))

        self.entry_recherche = tk.Entry(frame_search, font=FONT_ENTRY, width=20, relief="flat", bg=BG_COLOR, highlightthickness=1, highlightcolor=ACCENT_COLOR)
        self.entry_recherche.grid(row=0, column=2, sticky="ew", padx=5, ipady=3)
        self.entry_recherche.bind("<Return>", lambda _event: self.rechercher())

        ttk.Button(frame_search, text="Rechercher", command=self.rechercher,
                   style="Primary.TButton", cursor="hand2").grid(row=0, column=3, padx=5)
        ttk.Button(frame_search, text="Tout afficher", command=self.afficher_tout,
                   style="Accent.TButton", cursor="hand2").grid(row=0, column=4, padx=(5, 0))

        # Tableau des produits
        cadre_tree = tk.Frame(frame_droit, bg=PRIMARY_COLOR, padx=1, pady=1)
        cadre_tree.grid(row=1, column=0, sticky="nsew")

        frame_tree = tk.Frame(cadre_tree, bg=PANEL_COLOR)
        frame_tree.pack(fill=tk.BOTH, expand=True)

        colonnes = ("ID_Produit", "Nom", "Categorie", "Prix", "Quantite", "Fournisseur")
        self.tree = ttk.Treeview(frame_tree, columns=colonnes, show="headings", height=15)

        for col in colonnes:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center", minwidth=80)

        scrollbar = ttk.Scrollbar(frame_tree, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=5)

        self.tree.bind('<ButtonRelease-1>', self.selectionner_ligne)

        # Copyright en bas de la fenêtre
        tk.Label(
            self.frame_principal,
            text="© DEV103 — Ahmed Karkach and Mohamed OUELD EL GHABA OFPPT ©",
            font=("Segoe UI", 9),
            bg=BG_COLOR,
            fg="#64748B",
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(12, 0))

        self.afficher_tout()


    def ajouter(self):
        id_prod = self.entries["ID_Produit :"].get()
        if id_prod == "":
            messagebox.showwarning("Attention", "Veuillez saisir un ID.")
            return
        try:
            if any(p.get_id_produit() == id_prod for p in self.gestionnaire.get_tous_les_produits()):
                messagebox.showerror("Erreur", "Cet ID de produit existe déjà.")
                return
            produit = Produit(id_prod, self.entries["Nom :"].get(), self.entries["Catégorie :"].get(),
                              float(self.entries["Prix :"].get()), int(self.entries["Quantité :"].get()), self.entries["Fournisseur :"].get())
            self.gestionnaire.ajouter_produit(produit)
            self.effacer_champs()
            messagebox.showinfo("Succès", "Produit ajouté avec succès !")
        except ValueError:
            messagebox.showerror("Erreur", "Prix = nombre décimal\nQuantité = nombre entier.")

    def modifier(self):
        id_prod = self.entries["ID_Produit :"].get()
        if id_prod == "":
            messagebox.showwarning("Attention", "Sélectionnez un produit à modifier.")
            return
        try:
            produit = Produit(id_prod, self.entries["Nom :"].get(), self.entries["Catégorie :"].get(),
                              float(self.entries["Prix :"].get()), int(self.entries["Quantité :"].get()), self.entries["Fournisseur :"].get())
            self.gestionnaire.modifier_produit(produit)
            self.effacer_champs()
            messagebox.showinfo("Succès", "Produit modifié avec succès !")
        except ValueError:
            messagebox.showerror("Erreur", "Prix = nombre décimal\nQuantité = nombre entier.")

    def supprimer(self):
        id_prod = self.entries["ID_Produit :"].get()
        if id_prod:
            if messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer ce produit ?"):
                self.gestionnaire.supprimer_produit(id_prod)
                self.effacer_champs()
        else:
            messagebox.showwarning("Attention", "Sélectionnez un produit à supprimer.")

    def rechercher(self):
        critere = self.var_recherche.get()
        valeur = self.entry_recherche.get()
        if not valeur:
            self.afficher_tout()
            return
        resultat = self.gestionnaire.rechercher_produits(critere, valeur)
        self.mettre_a_jour_treeview(resultat)

    def afficher_tout(self):
        produits = self.gestionnaire.get_tous_les_produits()
        self.mettre_a_jour_treeview(produits)
        self.entries["ID_Produit :"].config(state="normal")
        self.entries["ID_Produit :"].delete(0, tk.END)
        self.entries["ID_Produit :"].insert(0, f"PROD-{len(produits)+1:03d}")
        self.entries["ID_Produit :"].config(state="readonly")

    def effacer_champs(self):
        for entry in self.entries.values():
            if isinstance(entry, ttk.Combobox):
                entry.config(state="normal")
            else:
                entry.config(state="normal", bg=BG_COLOR, highlightcolor=ACCENT_COLOR)
            entry.delete(0, tk.END)
        self.entries["ID_Produit :"].config(state="readonly", highlightthickness=0, bg=LIGHT_GRAY)
        self.afficher_tout()

    def selectionner_ligne(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return
        item = self.tree.item(selected_item[0])
        record = item['values']

        self.entries["ID_Produit :"].config(state="normal")
        self.entries["ID_Produit :"].delete(0, tk.END)
        self.entries["ID_Produit :"].insert(0, str(record[0]))
        self.entries["ID_Produit :"].config(state="readonly")

        champs_a_remplir = ["Nom :", "Catégorie :", "Prix :", "Quantité :", "Fournisseur :"]
        for i in range(len(champs_a_remplir)):
            champ = champs_a_remplir[i]
            self.entries[champ].delete(0, tk.END)
            self.entries[champ].insert(0, str(record[i+1]))

    def mettre_a_jour_treeview(self, liste_produits):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for produit in liste_produits:
            self.tree.insert("", tk.END, values=(
                produit.get_id_produit(), produit.get_nom(), produit.get_categorie(),
                produit.get_prix(), produit.get_quantite(), produit.get_fournisseur()
            ))

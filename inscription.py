import tkinter as tk
from tkinter import messagebox

class Inscription:
    def __init__(self, master, on_close_callback=None):
        self.master = master
        self.on_close_callback = on_close_callback

        self.master.title("Page d'Inscription")
        self.master.configure(bg='#0A3D62')  # Appliquer la couleur de fond bleu nocturne


        # Créer un cadre pour contenir les widgets d'inscription
        frame = tk.Frame(master, bg='#0A3D62')
        frame.pack(expand=True, padx=100, pady=100)

        # Champ Prénom
        tk.Label(frame, text="Prénom :", bg='#0A3D62', fg='white').grid(row=0, column=0, pady=(10, 0))
        self.prenom_inscription = tk.Entry(frame, width=30, bg='#0A3D62', fg='white', borderwidth=0)
        self.prenom_inscription.grid(row=0, column=1, pady=(10, 0))

        # Champ Nom
        tk.Label(frame, text="Nom :", bg='#0A3D62', fg='white').grid(row=1, column=0, pady=(10, 0))
        self.nom_inscription = tk.Entry(frame, width=30, bg='#0A3D62', fg='white', borderwidth=0)
        self.nom_inscription.grid(row=1, column=1, pady=(10,0))

        # Champ Adresse mail
        tk.Label(frame, text="Adresse mail :", bg='#0A3D62', fg='white').grid(row=2, column=0, pady=(10, 0))
        self.mail_inscription = tk.Entry(frame, width=30, bg='#0A3D62', fg='white', borderwidth=0)
        self.mail_inscription.grid(row=2, column=1, pady=(10, 0))

        # Champ Mot de passe
        tk.Label(frame, text="Mot de passe :", bg='#0A3D62', fg='white').grid(row=3, column=0, pady=(10, 0))
        self.mot_de_passe_inscription = tk.Entry(frame, width=30, show="*", bg='#0A3D62', fg='white', borderwidth=0)
        self.mot_de_passe_inscription.grid(row=3, column=1, pady=(10, 0))

        # Bouton d'inscription
        tk.Button(frame, width=30, text="S'inscrire", command=self.soumettre_inscription, bg='#0A3D62', fg='white').grid(row=4, column=0, columnspan=2, pady=(10, 0))

    def soumettre_inscription(self):
        prenom = self.prenom_inscription.get()
        nom = self.nom_inscription.get()
        email = self.mail_inscription.get()
        password = self.mot_de_passe_inscription.get()
        messagebox.showinfo("Inscription réussie", f"Bienvenue, {prenom} {nom}!")

    def on_close(self):
        if self.on_close_callback:
            self.on_close_callback()
        self.master.destroy()

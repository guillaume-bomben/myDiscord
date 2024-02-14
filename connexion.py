import tkinter as tk
from tkinter import messagebox

class Connexion:
    def __init__(self, master, switch_function):
        self.master = master
        self.master.title("Page de Connexion")
        self.master.configure(bg='#0A3D62')  # Appliquer la couleur de fond bleu nocturne


        # Créer un cadre pour contenir les widgets de connexion
        frame = tk.Frame(master, bg='#0A3D62')
        frame.pack(expand=True)

        # Champ adresse mail dans le cadre
        tk.Label(frame, text="Adresse mail :", bg='#0A3D62', fg='white').grid(row=0, column=0)
        self.adresse_mail_connexion = tk.Entry(frame, width=30)
        self.adresse_mail_connexion.grid(row=0, column=1)

        # Champ mot de passe dans le cadre
        tk.Label(frame, text="Mot de passe :", bg='#0A3D62', fg='white').grid(row=1, column=0)
        self.mot_de_passe_connexion = tk.Entry(frame, show="*", width=30)
        self.mot_de_passe_connexion.grid(row=1, column=1)

        # Boutons dans le cadre
        tk.Button(frame, text="Connexion", command=self.soumettre_connexion, width=30, bg='#0A3D62', fg='white').grid(row=2, column=0, sticky=tk.W)
        tk.Button(frame, text="S'inscrire", command=lambda: switch_function(master), bg='#0A3D62', fg='white', width=30,).grid(row=2, column=1, sticky=tk.E)

    def soumettre_connexion(self):
        email = self.adresse_mail_connexion.get()
        password = self.mot_de_passe_connexion.get()
        messagebox.showinfo("Connexion réussie", f"Vous êtes connecté avec l'adresse {email}!")
    
    def cacher(self):
        self.master.withdraw()  # Cache la fenêtre

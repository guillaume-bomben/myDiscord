import tkinter as tk
from tkinter import messagebox

class Connexion:
    def __init__(self, master, switch_function):
        self.master = master
        self.master.title("Page de Connexion")
        self.master.configure(bg='#0A3D62')  # Couleur de fond bleu nocturne

        frame = tk.Frame(master, bg='#0A3D62')
        frame.pack(expand=True, padx=100, pady=100)  # Ajuster l'espacement

        # Configure les widgets
        tk.Label(frame, text="Adresse mail :", bg='#0A3D62', fg='white').grid(row=0, column=0, pady=(10, 0))
        self.adresse_mail_connexion = tk.Entry(frame, width=30, bg='#0A3D62', fg='white', borderwidth=0)
        self.adresse_mail_connexion.grid(row=0, column=1, pady=(10, 0))

        tk.Label(frame, text="Mot de passe :", bg='#0A3D62', fg='white').grid(row=1, column=0, pady=(10, 0))
        self.mot_de_passe_connexion = tk.Entry(frame, show="*", width=30, bg='#0A3D62', fg='white', borderwidth=0)
        self.mot_de_passe_connexion.grid(row=1, column=1, pady=(10, 0))

        tk.Button(frame, text="Connexion", command=self.soumettre_connexion, bg='#0A3D62', fg='white', width=20).grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        tk.Button(frame, text="S'inscrire", command=lambda: switch_function(master), bg='#0A3D62', fg='white', width=20).grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

    def soumettre_connexion(self):
        email = self.adresse_mail_connexion.get()
        password = self.mot_de_passe_connexion.get()
        messagebox.showinfo("Connexion réussie", f"Vous êtes connecté avec l'adresse {email}!")
    
    def cacher(self):
        self.master.withdraw()  # Cache la fenêtre

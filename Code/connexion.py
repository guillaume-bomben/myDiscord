import sys
import tkinter as tk
from tkinter import messagebox
from Data.User import User

class Connexion:
    def __init__(self):
        self.user_list = User()
        self.master = tk.Tk()
        self.master.title("Page de Connexion")
        self.master.configure(bg='#0A3D62')
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.chat = False
        self.inscription = False

        self.setup_widgets()
        self.master.mainloop()

    def setup_widgets(self):
        frame = tk.Frame(self.master, bg='#0A3D62')
        frame.pack(expand=True, padx=100, pady=100)

        tk.Label(frame, text="Adresse mail :", bg='#0A3D62', fg='white').grid(row=0, column=0, pady=10)
        self.adresse_mail_connexion = tk.Entry(frame, width=30, bg='white', fg='black', borderwidth=0)
        self.adresse_mail_connexion.grid(row=0, column=1, pady=10)

        tk.Label(frame, text="Mot de passe :", bg='#0A3D62', fg='white').grid(row=1, column=0, pady=10)
        self.mot_de_passe_connexion = tk.Entry(frame, show="*", width=30, bg='white', fg='black', borderwidth=0)
        self.mot_de_passe_connexion.grid(row=1, column=1, pady=10)

        tk.Button(frame, text="Connexion", command=self.soumettre_connexion, width=20, bg='white', fg='black').grid(row=2, column=0, pady=10, sticky=tk.W)
        tk.Button(frame, text="S'inscrire", command=self.inscription_page, width=20, bg='white', fg='black').grid(row=2, column=1, pady=10, sticky=tk.E)

    def soumettre_connexion(self):
        email = self.adresse_mail_connexion.get()
        password = self.mot_de_passe_connexion.get()
        id = self.user_list.get_id_by_email_and_mdp(email, password)
        if id == []:
            messagebox.showerror("Erreur", "Adresse mail ou mot de passe incorrect")
            return
        else:
            self.id = id[0][0]
            self.master.destroy()
            self.chat = True


    def inscription_page(self):
        self.master.destroy()
        self.inscription = True
        
    def on_close(self):
        self.master.destroy()
        sys.exit(0)
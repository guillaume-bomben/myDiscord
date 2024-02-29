import sys
from Data.User import User
from Data.chan_user import chan_user
from Data.chanel import chanel
import tkinter as tk
from tkinter import messagebox

class Inscription:
    def __init__(self):
        self.user_list = User()
        self.chan_user = chan_user()
        self.chan = chanel()
        self.master = tk.Tk()
        self.master.title("Page d'Inscription")
        self.master.configure(bg='#0A3D62')
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

        
        self.connexion = False

        self.setup_widgets()
        
        self.master.mainloop()

    def setup_widgets(self):
        frame = tk.Frame(self.master, bg='#0A3D62')
        frame.pack(expand=True, padx=100, pady=100)

        labels_texts = ["Prénom :", "Nom :", "Adresse mail :", "Mot de passe :"]
        self.entries = []
        for i, text in enumerate(labels_texts):
            tk.Label(frame, text=text, bg='#0A3D62', fg='white').grid(row=i, column=0, pady=10)
            if i == 3:
                entry = tk.Entry(frame, width=30, bg='white', fg='black', borderwidth=0, show="*")
            else:
                entry = tk.Entry(frame, width=30, bg='white', fg='black', borderwidth=0)
            entry.grid(row=i, column=1, pady=10)
            self.entries.append(entry)

        tk.Button(frame, text="S'inscrire", command=self.soumettre_inscription, width=20, bg='white', fg='black').grid(row=4, column=0, columnspan=2, pady=10)

    def soumettre_inscription(self):
        prenom = self.entries[0].get()
        nom = self.entries[1].get()
        email = self.entries[2].get()
        password = self.entries[3].get()
        if self.entries[0].get() == "" or self.entries[1].get() == "" or self.entries[2].get() == "" or self.entries[3].get() == "":
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
            return
        else:
            self.user_list.create(nom, prenom, email, password)
            for chan in self.chan.data_list:
                self.chan_user.create(chan[0],self.user_list.get_id_by_email(email)[0][0],2)
            self.master.destroy()
            self.connexion = True
            
    def on_close(self):
        self.master.destroy()
        sys.exit(0)
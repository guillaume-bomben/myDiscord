from Data.User import User
import tkinter as tk
from tkinter import messagebox

class Inscription:
    def __init__(self, master, on_close_callback=None):
        self.user_list = User('localhost','root','1234','myDiscord')
        self.master = master
        self.on_close_callback = on_close_callback  # Store callback
        self.master.title("Page d'Inscription")
        self.master.configure(bg='#0A3D62')

        self.setup_widgets()

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

    def on_close(self):
        if self.on_close_callback:
            self.on_close_callback()
        self.master.destroy()

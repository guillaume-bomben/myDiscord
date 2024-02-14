import tkinter as tk
from tkinter import messagebox

class Inscription:
    def __init__(self, master, on_close_callback=None):
        self.master = master
        self.master.title("Page d'Inscription")
        self.master.configure(bg='#0A3D62')  # Couleur de fond bleu nocturne

        frame = tk.Frame(master, bg='#0A3D62')
        frame.pack(expand=True, padx=100, pady=100)

        # Configuration des widgets
        tk.Label(frame, text="Prénom :", bg='#0A3D62', fg='white').grid(row=0, column=0, pady=10)
        self.prenom_inscription = tk.Entry(frame, width=30, bg='white', fg='black', borderwidth=0)
        self.prenom_inscription.grid(row=0, column=1, pady=10)

        tk.Label(frame, text="Nom :", bg='#0A3D62', fg='white').grid(row=1, column=0, pady=10)
        self.nom_inscription = tk.Entry(frame, width=30, bg='white', fg='black', borderwidth=0)
        self.nom_inscription.grid(row=1, column=1, pady=10)

        tk.Label(frame, text="Adresse mail :", bg='#0A3D62', fg='white').grid(row=2, column=0, pady=10)
        self.mail_inscription = tk.Entry(frame, width=30, bg='white', fg='black', borderwidth=0)
        self.mail_inscription.grid(row=2, column=1, pady=10)

        tk.Label(frame, text="Mot de passe :", bg='#0A3D62', fg='white').grid(row=3, column=0, pady=10)
        self.mot_de_passe_inscription = tk.Entry(frame, show="*", width=30, bg='white', fg='black', borderwidth=0)
        self.mot_de_passe_inscription.grid(row=3, column=1, pady=10)

        tk.Button(frame, text="S'inscrire", command=self.soumettre_inscription, width=20, bg='white', fg='black').grid(row=4, column=0, columnspan=2, pady=10)

    def soumettre_inscription(self):
        prenom = self.entries[0].get()
        nom = self.entries[1].get()
        email = self.entries[2].get()
        password = self.entries[3].get()
        # Ici, vous pourriez inclure une logique pour enregistrer ces informations, par exemple dans une base de données
        messagebox.showinfo("Inscription réussie", f"Bienvenue, {prenom} {nom}!")

    def on_close(self):
        if self.on_close_callback:
            self.on_close_callback()
        self.master.destroy()

# Code pour tester la classe Inscription directement
if __name__ == "__main__":
    root = tk.Tk()
    app = Inscription(root)
    root.mainloop()

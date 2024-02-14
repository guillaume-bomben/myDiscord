import tkinter as tk
from connexion import Connexion
from inscription import Inscription

def main():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    app = Connexion(root, afficher_inscription)
    root.mainloop()

def afficher_inscription(master):
    master.withdraw()  # Cache la fenêtre de connexion
    inscription_window = tk.Toplevel()  # Utilisez Toplevel au lieu de Tk pour la fenêtre d'inscription
    inscription_window.attributes('-fullscreen', True)
    app_inscription = Inscription(inscription_window, lambda: master.destroy())  # Passer une fonction pour fermer root

if __name__ == "__main__":
    main()

import tkinter as tk
from connexion import Connexion
from inscription import Inscription

def main():
    root = tk.Tk()
    Connexion(root, afficher_inscription)  # Simplified initialization
    root.mainloop()

def afficher_inscription(master):
    master.withdraw()  # Hide the login window
    inscription_window = tk.Toplevel(master)  # Ensures correct parent-child relationship
    Inscription(inscription_window, lambda: master.destroy())  # Simplified lambda function

if __name__ == "__main__":
    main()

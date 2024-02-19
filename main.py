import tkinter as tk
from connexion import Connexion
from inscription import Inscription

def main():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    Connexion(root, afficher_inscription)  # Simplified initialization
    root.mainloop()

def afficher_inscription(master):
    master.withdraw()  # Hide the login window
    inscription_window = tk.Toplevel(master)  # Ensures correct parent-child relationship
    inscription_window.attributes('-fullscreen', True)
    Inscription(inscription_window, lambda: master.destroy())  # Simplified lambda function

if __name__ == "__main__":
    main()

from Data.chanel import chanel
from Data.message import message
from Data.User import User
import tkinter
import time

class chanels:
    def __init__(self):
        self.windows = tkinter.Tk()
        self.windows.title('Discord chat')
        
        self.curent_chanel = 1
        self.curent_user = 1
        
        self.user_list = User('localhost','root','1234','myDiscord')
        self.chan = chanel('localhost','root','1234','myDiscord')
        self.mess = message('localhost','root','1234','myDiscord')
        
        # Créer un cadre pour contenir les messages
        self.messages_frame = tkinter.Frame(self.windows)
        self.messages_frame.pack()
        # Créer une zone de texte pour afficher les messages
        self.messages_text = tkinter.Text(self.messages_frame, width=50, height=20)
        self.messages_text.pack()
        # Créer une barre de défilement verticale pour la zone de texte
        self.scrollbar = tkinter.Scrollbar(self.messages_frame, command=self.messages_text.yview)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        # Définir la zone de texte pour qu'elle utilise la barre de défilement
        self.messages_text.config(yscrollcommand=self.scrollbar.set)
        # Créer une zone de saisie pour envoyer des messages
        self.entry_frame = tkinter.Frame(self.windows)
        self.entry_frame.pack()
        self.entry_text = tkinter.Entry(self.entry_frame, width=50)
        self.entry_text.pack()
        
        # Bouton d'envoi
        self.send_button = tkinter.Button(self.entry_frame, text="Envoyer", command=self.send_message)
        self.send_button.pack()
        
        self.chat()
        
        self.windows.mainloop()


    def chat(self):
        # Insérer chaque message dans la zone de texte
        for message in self.mess.get_message_by_id_chanel(self.curent_chanel):
            self.messages_text.insert(tkinter.END, f"{self.user_list.get_nom_and_prenom_by_id(self.curent_user)}: {message}\n")


    def send_message(self):
        message_content = self.entry_text.get()
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        # Enregistrer le message dans la base de données
        self.mess.create(message_content,date,self.curent_chanel,self.curent_user)

        # Afficher le message dans la zone de texte
        self.messages_text.insert(tkinter.END, f"{self.user_list.get_nom_and_prenom_by_id(self.curent_user)}: {message_content}\n")

        # Vider la zone de saisie
        self.entry_text.delete(0, tkinter.END)
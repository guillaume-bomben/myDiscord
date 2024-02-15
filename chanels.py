from Data.chanel import chanel
from Data.message import message
import tkinter

class chanels:
    def __init__(self):
        self.windows = tkinter.Tk()
        self.windows.title('Discord chat')
        
        self.curent_chanel = 1
        
        self.chan = chanel('localhost','root','1234','myDiscord')
        self.mess = message('localhost','root','1234','myDiscord')
        
        self.chat()
        
        self.windows.mainloop()
    
    def chat(self):
        #messages = self.mess.get_message_by_id_chanel(self.curent_chanel)
        
        # Créer un cadre pour contenir les messages
        messages_frame = tkinter.Frame(self.windows)
        messages_frame.pack()

        # Créer une zone de texte pour afficher les messages
        messages_text = tkinter.Text(messages_frame, width=50, height=20)
        messages_text.pack()

        # Créer une barre de défilement verticale pour la zone de texte
        scrollbar = tkinter.Scrollbar(messages_frame, command=messages_text.yview)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Définir la zone de texte pour qu'elle utilise la barre de défilement
        messages_text.config(yscrollcommand=scrollbar.set)
        
        # Insérer chaque message dans la zone de texte
        for message in self.mess.data_list:
            messages_text.insert(tkinter.END, f"{message.id_user}: {message.message}\n")
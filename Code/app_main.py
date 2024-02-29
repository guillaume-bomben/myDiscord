from Code.connexion import Connexion
from Code.inscription import Inscription
from Code.chat import chat

class app_main:
    def __init__(self):
        self.Connect_page = Connexion()
        
        self.event()
        
    
    def event(self):
        while True:
            if self.Connect_page.chat:
                self.chat_page = chat(self.Connect_page.id)
                self.Connect_page.chat = False
            if self.Connect_page.inscription:
                self.inscription_page = Inscription()
                self.Connect_page.inscription = False
            if self.chat_page.connexion == False:
                self.Connect_page = Connexion()
                self.chat_page.connexion = True
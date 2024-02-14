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
        self.mess.get_message_by_id_chanel(self.curent_chanel)
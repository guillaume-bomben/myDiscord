from Data.chanel import chanel
from Data.message import message
from Data.User import User
import tkinter
import time

class chanels:
    def __init__(self,user_id):
        self.windows = tkinter.Tk()
        self.windows.title('Discord chat')
        
        self.curent_chanel = 1
        self.curent_user = user_id
        
        self.user_list = User('localhost','root','1234','myDiscord')
        self.chan = chanel('localhost','root','1234','myDiscord')
        self.mess = message('localhost','root','1234','myDiscord')
        
        self.affiche_chat()
        self.affiche_chanels()
        
        tkinter.Button(self.windows, text="Add Chanel", command=self.add_chanel).pack()
        
        self.windows.mainloop()


    def affiche_chat(self):
        #create a frame to contain the messages
        self.messages_frame = tkinter.Frame(self.windows)
        self.messages_frame.pack()
        #create a text box to display the messages
        self.messages_text = tkinter.Text(self.messages_frame, width=150, height=50)
        self.messages_text.pack()
        #create a scrollbar for the text box
        self.scrollbar = tkinter.Scrollbar(self.messages_frame, command=self.messages_text.yview)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        # set text widget to use vertical scrollbar
        self.messages_text.config(yscrollcommand=self.scrollbar.set)
        #create a frame to contain the entry and the button
        self.entry_frame = tkinter.Frame(self.windows)
        self.entry_frame.pack()
        self.entry_text = tkinter.Entry(self.entry_frame, width=50)
        self.entry_text.pack()
        # send button
        self.send_button = tkinter.Button(self.entry_frame, text="Envoyer", command=self.send_message)
        self.send_button.pack()
        
        self.add_message_in_chat()


    def add_message_in_chat(self):
        # insert the messages into the text box
        for message in self.mess.get_message_by_id_chanel(self.curent_chanel):
            id = self.mess.get_id_user_by_message(message[0])
            date = self.mess.get_date_by_message(message[0])
            user_name = self.user_list.get_nom_and_prenom_by_id(id[0][0])
            self.messages_text.insert(tkinter.END, f"{user_name[0][0]} {user_name[0][1]} ({date[0][0]}): {message[0]}\n")


    def send_message(self):
        message_content = self.entry_text.get()
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        # save the message in the database
        self.mess.create(message_content,date,self.curent_chanel,self.curent_user)
        # show the message in the text box
        self.messages_text.insert(tkinter.END, f"{self.user_list.get_nom_and_prenom_by_id(self.curent_user)}: {message_content}\n")
        # clear the entry
        self.entry_text.delete(0, tkinter.END)


    def change_chanel(self,chanel_id):
        self.curent_chanel = chanel_id
        self.messages_text.delete(1.0, tkinter.END)
        self.add_message_in_chat()
        
    
    def affiche_chanels(self):
        self.chanels_frame = tkinter.Frame(self.windows)
        self.chanels_frame.pack()
        for chanel in self.chan.data_list:
            self.chanel_button = tkinter.Button(self.chanels_frame, text=chanel[1], command=lambda chanel_id=chanel[0]: self.change_chanel(chanel_id))
            self.chanel_button.pack()
    
    
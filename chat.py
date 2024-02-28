import os
import sys
import pygame
from Data.chanel import chanel
from Data.message import message
from Data.User import User
from Data.chan_user import chan_user
from admin_page import admin_page
import tkinter
import time
import pyaudio
import wave
import emoji

class chat:
    def __init__(self,user_id):
        self.windows = tkinter.Tk()
        self.windows.title('Discord chat')
        self.windows.protocol("WM_DELETE_WINDOW", self.on_close)
        self.connexion = True
        
        self.curent_chanel = 1
        self.curent_user = user_id
        self.audio_buttons = {}
        
        self.user_list = User()
        self.chan = chanel()
        self.mess = message()
        self.chan_user = chan_user()
        
        self.affiche_chat()
        self.affiche_chanels()
        self.run_function_periodically()
        
        tkinter.Button(self.windows, text="Add Chanel", command=self.add_chanel).grid(row=1, column=0, sticky="nsew")
        
        self.windows.mainloop()

    def affiche_chat(self):
        #create a frame to contain the messages
        self.messages_frame = tkinter.Frame(self.windows)
        self.messages_frame.grid(row=0, column=1, sticky="nsew")
        
        #create a text box to display the messages
        self.messages_text = tkinter.Text(self.messages_frame, height=20, width=150)
        self.messages_text.grid(row=0, column=0, sticky="nsew")
        
        #create a scrollbar for the text box
        self.scrollbar = tkinter.Scrollbar(self.messages_frame, command=self.messages_text.yview)
        self.scrollbar.grid(row=0, column=2, sticky="nsew")
        self.messages_text.config(yscrollcommand=self.scrollbar.set)
        
        #create a frame to contain the entry and the button
        self.entry_frame = tkinter.Frame(self.windows)
        self.entry_frame.grid(row=1, column=1, sticky="nsew")
        self.entry_text = tkinter.Entry(self.entry_frame, width=50)
        self.entry_text.grid(row=0, column=0, sticky="nsew")
        # send button
        self.send_button = tkinter.Button(self.entry_frame, text="Envoyer", command=self.send_message)
        self.send_button.grid(row=0, column=1, sticky="ew")
        
        self.voce_button = tkinter.Button(self.entry_frame, text="Enregistrer", command= lambda :self.enregistrer_message('test.wav', 5))
        self.voce_button.grid(row=0, column=2, sticky="nsew")
        
        self.audio_buttons = tkinter.Button(self.entry_frame, text="Audio list", command=self.audio_list_window)
        self.audio_buttons.grid(row=0, column=3, sticky="nsew")
        
        self.emoji_button = tkinter.Button(self.entry_frame, text="Liste des emojis", command=self.list_emojis)
        self.emoji_button.grid(row=0, column=4, sticky="nsew")
        
        self.disconnect_button = tkinter.Button(self.entry_frame, text="Disconnect", command=self.disconnected)
        self.disconnect_button.grid(row=0, column=5, sticky="nsew")
        
        if self.chan_user.get_id_role_by_id_user_and_id_chanel(self.curent_user,self.curent_chanel)[0][0] == 1:
            self.admin_button = tkinter.Button(self.entry_frame, text="Admin", command=lambda: admin_page(self.windows,self.curent_chanel))
            self.admin_button.grid(row=0, column=6, sticky="nsew")
        
        self.add_message_in_chat() 

    def add_message_in_chat(self):
        audio_index = 1
        for message in self.mess.get_message_by_id_chanel(self.curent_chanel):
            id = self.mess.get_id_user_by_message(message[0])
            date = self.mess.get_date_by_message(message[0])
            type = self.mess.get_type_by_message(message[0])
            user_name = self.user_list.get_nom_and_prenom_by_id(id[0][0])
            if type[0][0] == 'audio':
                #if the message is an audio message, display a special icon
                self.messages_text.insert(tkinter.END, f"({date[0][0]}) {user_name[0][0]} {user_name[0][1]}: [🔊 Audio {audio_index}]\n")
                audio_index += 1
            else:
                message_content = emoji.emojize(message[0].decode('utf-8'))
                self.messages_text.insert(tkinter.END, f"({date[0][0]}) {user_name[0][0]} {user_name[0][1]}: {message_content}\n")

    def lire_audio(self, message_id):
        audio_blob = self.mess.get_message_by_id(message_id[0][0])
        if audio_blob != []:
            audio_file = f"temp_audio_{message_id}.wav"
            with open(audio_file, 'wb') as f:
                f.write(audio_blob[0][0])  
            pygame.mixer.init()
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)  
            pygame.mixer.quit()
            os.remove(audio_file)
        else:
            print("Erreur: Données audio non disponibles.")

    def send_message(self):
        message_content = self.entry_text.get()
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        self.mess.create(message_content,date,self.curent_chanel,self.curent_user,'text') # save the message in the database
        # show the message in the text box
        self.messages_text.insert(tkinter.END, f"{self.user_list.get_nom_and_prenom_by_id(self.curent_user)} {date}: {message_content}\n")
        self.entry_text.delete(0, tkinter.END) # clear the entry

    def change_chanel(self,chanel_id):
        self.curent_chanel = chanel_id
        self.messages_text.delete(1.0, tkinter.END)
        self.affiche_chat()

    def affiche_chanels(self):
        self.chanels_frame = tkinter.Frame(self.windows,width=100)
        self.chanels_frame.grid(row=0, column=0, sticky="nsew")
        for chanel in self.chan.data_list:
            self.chanel_button = tkinter.Button(self.chanels_frame, text=chanel[1], command=lambda chanel_id=chanel[0]: self.change_chanel(chanel_id))
            self.chanel_button.grid(row=chanel[0], column=0, sticky="nsew")

    def add_chanel(self):
        add_page = tkinter.Toplevel(self.windows)
        add_page.title('Add chanel')
        add_page.geometry('300x100')
        add_page.configure(bg='#0A3D62')
        
        nom_chanel = tkinter.Entry(add_page, width=30, bg='white', fg='black', borderwidth=0)
        nom_chanel.grid(row=0, column=0, padx=10, pady=10)
        
        button = tkinter.Button(add_page, text="Add", command=lambda: self.create_chanel(nom_chanel.get()))
        button.grid(row=1, column=0, padx=10, pady=10)

    def create_chanel(self,nom):
        self.chan.create(nom)
        self.chan.read()
        self.affiche_chanels()
        id_chan = self.chan.get_id_by_nom(nom)
        self.chan_user.create(id_chan[0][0],self.curent_user,1)
        for user in self.user_list.data_list:
            if user[0] != self.curent_user:
                self.chan_user.create(id_chan[0][0],user[0],2)

    def enregistrer_message(self,filename, duration):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = duration
        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        frames = []
        print("Enregistrement en cours...")
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        
        print("Enregistrement terminé.")
        
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        wf = wave.open(filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        
        with open(filename, "rb") as f:
            message_blob = f.read()
            date = time.strftime("%Y-%m-%d %H:%M:%S")
            self.mess.create(message_blob,date,self.curent_chanel,self.curent_user)

    def audio_list_window(self):
        audio_list = tkinter.Toplevel(self.windows)
        audio_list.title('Audio list')
        audio_list.geometry('300x100')
        audio_list.configure(bg='#0A3D62')
        
        audio_list_frame = tkinter.Frame(audio_list,width=100)
        audio_list_frame.grid(row=0, column=0, sticky="nsew")
        audio_index = 1
        for message in self.mess.get_message_by_id_chanel(self.curent_chanel):
            type = self.mess.get_type_by_message(message[0])
            if type[0][0] == 'audio':
                audio_button = tkinter.Button(audio_list_frame, text=f"Audio {audio_index}", command=lambda message_id=self.mess.get_id_by_message(message[0]): self.lire_audio(message_id))
                audio_button.grid(row=audio_index, column=0, sticky="nsew")
                audio_index += 1
        audio_list.mainloop()

    def list_emojis(self):
        list_emojis = tkinter.Toplevel(self.windows)
        list_emojis.title('Liste des emojis')
        list_emojis.geometry('300x100')
        list_emojis.configure(bg='#0A3D62')
        
        list_emojis_frame = tkinter.Frame(list_emojis,width=100)
        list_emojis_frame.grid(row=0, column=0, sticky="nsew")
        for id,emoji in enumerate(["😁","😘","😕","🤬","🤢","😈"]):
            emoji_button = tkinter.Button(list_emojis_frame, text=emoji, command=lambda emoji_id=id: self.add_emoji(emoji_id))
            emoji_button.grid(row=id%4, column=id//4, sticky="nsew")

    def add_emoji(self,emoji_id):
        self.entry_text.insert(tkinter.END, ["😁","😘","😕","🤬","🤢","😈"][emoji_id])

    def run_function_periodically(self):
        self.messages_text.delete(1.0, tkinter.END)
        self.affiche_chat()
        self.windows.after(10000, self.run_function_periodically)

    def disconnected(self):
        self.windows.destroy()
        self.connexion = False

    def on_close(self):
        self.windows.destroy()
        sys.exit(0)
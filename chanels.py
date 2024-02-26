import os
import pygame
from Data.chanel import chanel
from Data.message import message
from Data.User import User
import tkinter
import time
import pyaudio
import wave

class chanels:
    def __init__(self,user_id):
        self.windows = tkinter.Tk()
        self.windows.title('Discord chat')
        
        self.curent_chanel = 1
        self.curent_user = user_id
        
        self.user_list = User()
        self.chan = chanel()
        self.mess = message()
        
        self.affiche_chat()
        self.affiche_chanels()
        
        tkinter.Button(self.windows, text="Add Chanel", command=self.add_chanel).grid(row=1, column=0, sticky="nsew")
        
        self.windows.mainloop()


    def affiche_chat(self):
        #create a frame to contain the messages
        self.messages_frame = tkinter.Frame(self.windows)
        self.messages_frame.grid(row=0, column=1, sticky="nsew")
        #create a text box to display the messages
        self.messages_text = tkinter.Text(self.messages_frame, width=150, height=25)
        self.messages_text.grid(row=0, column=0, sticky="nsew")
        #create a scrollbar for the text box
        self.scrollbar = tkinter.Scrollbar(self.messages_frame, command=self.messages_text.yview)
        self.scrollbar.grid(row=0, column=1, sticky="nsew")
        # set text widget to use vertical scrollbar
        self.messages_text.config(yscrollcommand=self.scrollbar.set)
        #create a frame to contain the entry and the button
        self.entry_frame = tkinter.Frame(self.windows)
        self.entry_frame.grid(row=1, column=1, sticky="nsew")
        self.entry_text = tkinter.Entry(self.entry_frame, width=50)
        self.entry_text.grid(row=0, column=0, sticky="nsew")
        # send button
        self.send_button = tkinter.Button(self.entry_frame, text="Envoyer", command=self.send_message)
        self.send_button.grid(row=0, column=1, sticky="nsew")
        
        self.voce_button = tkinter.Button(self.entry_frame, text="Enregistrer", command= lambda :self.enregistrer_message('test.wav', 5))
        self.voce_button.grid(row=0, column=2, sticky="nsew")
        
        self.add_message_in_chat() 


    def add_message_in_chat(self):
        # insert the messages into the text box
        for message in self.mess.get_message_by_id_chanel(self.curent_chanel):
            id = self.mess.get_id_user_by_message(message[0])
            date = self.mess.get_date_by_message(message[0])
            type = self.mess.get_type_by_message(message[0])
            user_name = self.user_list.get_nom_and_prenom_by_id(id[0][0])
            if type[0][0] == 'audio':
                #if the message is an audio message, display a special icon
                self.messages_text.insert(tkinter.END, f"{user_name[0][0]} {user_name[0][1]} ({date[0][0]}): [🔊 Audio]\n")
                play_button = tkinter.Button(self.messages_frame, text="Lire", command=lambda message_id=self.mess.get_id_by_message(message[0]): self.lire_audio(message_id))
                play_button.grid(row=0, column=1, sticky="nsew")
            else:
                #else, display the text normally
                self.messages_text.insert(tkinter.END, f"{user_name[0][0]} {user_name[0][1]} ({date[0][0]}): {message[0]}\n")


    def lire_audio(self, message_id):
        audio_blob = self.mess.get_message_by_id(message_id[0][0])
        if audio_blob != []:
        # Si les données binaires de l'audio sont récupérées avec succès
            audio_file = f"temp_audio_{message_id}.wav"  # Nom du fichier temporaire pour enregistrer l'audio
            with open(audio_file, 'wb') as f:
                f.write(audio_blob[0][0])  # Écriture des données binaires de l'audio dans le fichier temporaire

            # Initialisation de Pygame pour la lecture audio
            pygame.mixer.init()
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

            # Attendre la fin de la lecture
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)  # Attendez 10 millisecondes pour éviter de surcharger le processeur

            # Arrêter Pygame après la lecture
            pygame.mixer.quit()

            # Supprimer le fichier temporaire après la lecture
            os.remove(audio_file)
        else:
            print("Erreur: Données audio non disponibles.")


    def send_message(self):
        message_content = self.entry_text.get()
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        # save the message in the database
        self.mess.create(message_content,date,self.curent_chanel,self.curent_user,'text')
        # show the message in the text box
        self.messages_text.insert(tkinter.END, f"{self.user_list.get_nom_and_prenom_by_id(self.curent_user)} {date}: {message_content}\n")
        # clear the entry
        self.entry_text.delete(0, tkinter.END)


    def change_chanel(self,chanel_id):
        self.curent_chanel = chanel_id
        self.messages_text.delete(1.0, tkinter.END)
        self.add_message_in_chat()
        
    
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
        self.add_chanel.destroy()


    #fonction for recording the voice message
    def enregistrer_message(self,filename, duration):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = duration  # time of recording in seconds
        
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
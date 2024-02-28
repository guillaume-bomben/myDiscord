import tkinter
from tkinter import ttk
from Data.role import role
from Data.User import User
from Data.chan_user import chan_user

class admin_page:
    def __init__(self,master,idchan):
        self.windows = tkinter.Toplevel(master)
        self.windows.title('Gestion des Roles')
        
        self.idchan = idchan
        self.user_list_selection = []
        self.role_list_selection = []
        
        self.role_list = role()
        for roles in self.role_list.data_list:
            self.role_list_selection.append(roles[1])
        self.user_list = User()
        for user in self.user_list.data_list:
            self.user_list_selection.append(user[1] + " " + user[2])
        
        self.chan_user_info = chan_user()
        self.widget()
        
        self.windows.mainloop()
    
    def widget(self):
        self.role_frame = tkinter.Frame(self.windows)
        self.role_frame.grid(row=0, column=0, sticky="nsew")
        
        self.list_user_box = ttk.Combobox(self.role_frame,values=self.user_list_selection, height=20, width=50)
        self.list_user_box.bind("<<ComboboxSelected>>", self.on_select_user)
        self.list_user_box.grid(row=0, column=0, sticky="nsew")
        
        self.list_role_box = ttk.Combobox(self.role_frame,values=self.role_list_selection ,height=20, width=50)
        self.list_role_box.grid(row=0, column=2, sticky="nsew")
        
        self.validate_button = tkinter.Button(self.role_frame, text="Valider", command=self.validate)
        self.validate_button.grid(row=1, column=0, sticky="nsew")
        
        
        self.add_role_entry = tkinter.Entry(self.role_frame, width=50)
        self.add_role_entry.grid(row=2, column=0, sticky="nsew")
        
        self.add_role_button = tkinter.Button(self.role_frame, text="Ajouter un role", command=self.add_role)
        self.add_role_button.grid(row=2, column=2, sticky="nsew")
    
    def validate(self):
        if self.list_user_box.get() != "" and self.list_role_box.get() != "":
            id_user = self.user_list.get_id_by_nom(self.list_user_box.get().split(" ")[0])
            id_role = self.role_list.get_id_by_nom(self.list_role_box.get())
            self.chan_user_info.update_id_role_by_id_user_and_id_chanel(id_user[0][0],self.idchan,id_role[0][0])
            print("Role updated")
    
    def on_select_user(self,event):
        selected_option = self.list_user_box.get()
        id_user = self.user_list.get_id_by_nom(selected_option.split(" ")[0])
        id_role = self.chan_user_info.get_id_role_by_id_user_and_id_chanel(id_user[0][0],self.idchan)
        role_name = self.role_list.get_nom_by_id(id_role[0][0])
        self.list_role_box.set(role_name[0][0])
    
    def add_role(self):
        self.role_list.create(self.add_role_entry.get())
        self.role_list_selection.append(self.add_role_entry.get())
        self.list_role_box['values'] = self.role_list_selection
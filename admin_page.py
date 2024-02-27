import tkinter
from Data.role import role
from Data.User import User

class admin_page:
    def __init__(self,master):
        self.windows = tkinter.Toplevel(master)
        self.windows.title('Gestion des Roles')
        
        self.role_list = role()
        self.user_list = User()
        
        self.windows.mainloop()
    
    def widget(self):
        self.role_frame = tkinter.Frame(self.windows)
        self.role_frame.grid(row=0, column=0, sticky="nsew")
        
        self.list_user = tkinter.Listbox(self.role_frame, height=20, width=50)
        self.list_user.grid(row=0, column=0, sticky="nsew")
        
        self.list_role = tkinter.Listbox(self.role_frame, height=20, width=50)
        self.list_role.grid(row=0, column=2, sticky="nsew")
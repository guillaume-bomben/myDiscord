from DB import DB

class serv_user(DB):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.data_liste = []
    
    def create(self,id_serveur,id_user,id_role):
        query = "INSERT INTO serv_user (id_serveur,id_user,id_role) VALUES (%s,%s,%s)"
        param = (id_serveur,id_user,id_role)
        self.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM serv_user"
        self.data_list = []
        for line in self.fetch(query):
            self.data_list.append(line)
    
    def delete(self,id):
        query = "DELETE FROM serv_user WHERE id = %s"
        param = (id,)
        self.executeQuery(query,param)
    
    def update_id_serveur(self,id,id_serveur):
        query = "UPDATE serv_user SET id_serveur = %s WHERE id = %s"
        param = (id_serveur,id)
        self.executeQuery(query,param)
    
    def update_id_user(self,id,id_user):
        query = "UPDATE serv_user SET id_user = %s WHERE id = %s"
        param = (id_user,id)
        self.executeQuery(query,param)
    
    def update_id_role(self,id,id_role):
        query = "UPDATE serv_user SET id_role = %s WHERE id = %s"
        param = (id_role,id)
        self.executeQuery(query,param)
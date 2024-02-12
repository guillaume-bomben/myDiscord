from DB import DB

class channel(DB):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.data_liste = []
    
    def create(self,nom,id_serveur):
        query = "INSERT INTO channel (nom,id_serveur) VALUES (%s,%s)"
        param = (nom,id_serveur)
        self.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM channel"
        self.data_list = []
        for line in self.fetch(query):
            self.data_list.append(line)
    
    def delete(self,id):
        query = "DELETE FROM channel WHERE id = %s"
        param = (id,)
        self.executeQuery(query,param)
    
    def update_nom(self,id,nom):
        query = "UPDATE channel SET nom = %s WHERE id = %s"
        param = (nom,id)
        self.executeQuery(query,param)
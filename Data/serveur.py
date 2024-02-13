from DB import DB

class serveur(DB):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.data_liste = []
    
    def create(self,nom):
        query = "INSERT INTO serveur (nom) VALUES (%s)"
        param = (nom,)
        self.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM serveur"
        self.data_list = []
        for line in self.fetch(query):
            self.data_list.append(line)
    
    def delete(self,id):
        query = "DELETE FROM serveur WHERE id = %s"
        param = (id,)
        self.executeQuery(query,param)
    
    def update_nom(self,id,nom):
        query = "UPDATE serveur SET nom = %s WHERE id = %s"
        param = (nom,id)
        self.executeQuery(query,param)
    
    def get_id_by_nom(self,nom):
        query = "SELECT id FROM serveur WHERE nom = %s"
        param = (nom,)
        return self.fetch(query,param)

    def get_nom_by_id(self,id):
        query = "SELECT nom FROM serveur WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)
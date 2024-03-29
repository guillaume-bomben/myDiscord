from Code.Data.DB import DB

class role(DB):
    def __init__(self):
        super().__init__()
        self.data_liste = []
        self.read()
    
    def create(self,nom):
        query = "INSERT INTO role (nom) VALUES (%s)"
        param = (nom,)
        self.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM role"
        self.data_list = []
        for line in self.fetch(query):
            self.data_list.append(line)
    
    def delete(self,id):
        query = "DELETE FROM role WHERE id = %s"
        param = (id,)
        self.executeQuery(query,param)
    
    def update_nom(self,id,nom):
        query = "UPDATE role SET nom = %s WHERE id = %s"
        param = (nom,id)
        self.executeQuery(query,param)
    
    def get_id_by_nom(self,nom):
        query = "SELECT id FROM role WHERE nom = %s"
        param = (nom,)
        return self.fetch(query,param)
    
    def get_nom_by_id(self,id):
        query = "SELECT nom FROM role WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)
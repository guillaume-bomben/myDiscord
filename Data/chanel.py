from Data.DB import DB

class chanel(DB):
    def __init__(self):
        super().__init__()
        self.data_liste = []
        self.read()
    
    def create(self,nom):
        query = "INSERT INTO chanel (nom) VALUES (%s)"
        param = (nom,)
        self.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM chanel"
        self.data_list = []
        for line in self.fetch(query):
            self.data_list.append(line)
    
    def delete(self,id):
        query = "DELETE FROM chanel WHERE id = %s"
        param = (id,)
        self.executeQuery(query,param)
    
    def update_nom(self,id,nom):
        query = "UPDATE chanel SET nom = %s WHERE id = %s"
        param = (nom,id)
        self.executeQuery(query,param)
    
    def get_id_by_nom(self,nom):
        query = "SELECT id FROM chanel WHERE nom = %s"
        param = (nom,)
        return self.fetch(query,param)

    def get_nom_by_id(self,id):
        query = "SELECT nom FROM chanel WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)
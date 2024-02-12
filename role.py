from DB import DB

class role(DB):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.data_liste = []
    
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
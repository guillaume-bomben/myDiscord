from DB import DB

class User(DB):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.data_list = []
        
    def create(self,nom,prenom,email,mdp):
        query = "INSERT INTO user (nom,prenom,email,mdp) VALUES (%s,%s,%s,%s)"
        param = (nom,prenom,email,mdp)
        self.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM user"
        self.data_list = []
        for line in self.fetch(query):
            self.data_list.append(line)
    
    def delete(self,id):
        query = "DELETE FROM user WHERE id = %s"
        param = (id,)
        self.executeQuery(query,param)
    
    def update_nom(self,id,nom):
        query = "UPDATE user SET nom = %s WHERE id = %s"
        param = (nom,id)
        self.executeQuery(query,param)
    
    def update_prenom(self,id,prenom):
        query = "UPDATE user SET prenom = %s WHERE id = %s"
        param = (prenom,id)
        self.executeQuery(query,param)
    
    def update_email(self,id,email):
        query = "UPDATE user SET email = %s WHERE id = %s"
        param = (email,id)
        self.executeQuery(query,param)

    def update_mdp(self,id,mdp):
        query = "UPDATE user SET mdp = %s WHERE id = %s"
        param = (mdp,id)
        self.executeQuery(query,param)
    
    def get_id_by_email(self,email):
        query = "SELECT id FROM user WHERE email = %s"
        param = (email,)
        return self.fetch(query,param)

    def get_id_by_id(self,id):
        query = "SELECT id FROM user WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)

    def get_id_by_nom(self,nom):
        query = "SELECT id FROM user WHERE nom = %s"
        param = (nom,)
        return self.fetch(query,param)
    
    def get_id_by_prenom(self,prenom):
        query = "SELECT id FROM user WHERE prenom = %s"
        param = (prenom,)
        return self.fetch(query,param)
    
    
from Code.Data.DB import DB

class chan_user(DB):
    def __init__(self):
        super().__init__()
        self.data_liste = []
        self.read()
    
    def create(self,id_chanel,id_user,id_role,nb_mess):
        query = "INSERT INTO chan_user (id_chanel,id_user,id_role,nb_mess) VALUES (%s,%s,%s,%s)"
        param = (id_chanel,id_user,id_role,nb_mess)
        self.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM chan_user"
        self.data_list = []
        for line in self.fetch(query):
            self.data_list.append(line)
    
    def delete(self,id):
        query = "DELETE FROM chan_user WHERE id = %s"
        param = (id,)
        self.executeQuery(query,param)
    
    def update_id_chanel(self,id,id_chanel):
        query = "UPDATE chan_user SET id_chanel = %s WHERE id = %s"
        param = (id_chanel,id)
        self.executeQuery(query,param)
    
    def update_id_user(self,id,id_user):
        query = "UPDATE chan_user SET id_user = %s WHERE id = %s"
        param = (id_user,id)
        self.executeQuery(query,param)
    
    def update_id_role(self,id,id_role):
        query = "UPDATE _user SET id_role = %s WHERE id = %s"
        param = (id_role,id)
        self.executeQuery(query,param)
        
    def update_nb_mess(self,nb_mess,id_user,id_chanel):
        query = "UPDATE chan_user SET nb_mess = %s WHERE id_user = %s AND id_chanel = %s"
        param = (nb_mess,id_user,id_chanel)
        self.executeQuery(query,param)
    
    def update_id_role_by_id_user_and_id_chanel(self,id_user,id_chanel,id_role):
        query = "UPDATE chan_user SET id_role = %s WHERE id_user = %s AND id_chanel = %s"
        param = (id_role,id_user,id_chanel)
        self.executeQuery(query,param)
        
    def get_id_role_by_id_user_and_id_chanel(self,id_user,id_chanel):
        query = "SELECT id_role FROM chan_user WHERE id_user = %s AND id_chanel = %s"
        param = (id_user,id_chanel)
        return self.fetch(query,param)

    def get_nb_mess_by_id_user_and_id_chanel(self,id_user,id_chanel):
        query = "SELECT nb_mess FROM chan_user WHERE id_user = %s AND id_chanel = %s"
        param = (id_user,id_chanel)
        return self.fetch(query,param)
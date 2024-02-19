from Data.DB import DB

class message(DB):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.data_liste = []
        self.read()
    
    def create(self,message,date,id_chanel,id_user):
        query = "INSERT INTO message (message,date,id_chanel,id_user) VALUES (%s,%s,%s,%s)"
        param = (message,date,id_chanel,id_user)
        self.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM message"
        self.data_list = []
        for line in self.fetch(query):
            self.data_list.append(line)
    
    def delete(self,id):
        query = "DELETE FROM message WHERE id = %s"
        param = (id,)
        self.executeQuery(query,param)
    
    def update_message(self,id,message):
        query = "UPDATE message SET message = %s WHERE id = %s"
        param = (message,id)
        self.executeQuery(query,param)
    
    def update_date(self,id,date):
        query = "UPDATE message SET date = %s WHERE id = %s"
        param = (date,id)
        self.executeQuery(query,param)
    
    def update_id_chanel(self,id,id_chanel):
        query = "UPDATE message SET id_chanel = %s WHERE id = %s"
        param = (id_chanel,id)
        self.executeQuery(query,param)
    
    def update_id_user(self,id,id_user):
        query = "UPDATE message SET id_user = %s WHERE id = %s"
        param = (id_user,id)
        self.executeQuery(query,param)
    
    def get_message_by_id(self,id):
        query = "SELECT message FROM message WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)
    
    def get_message_by_id_chanel(self,id_chanel):
        query = "SELECT message FROM message WHERE id_chanel = %s"
        param = (id_chanel,)
        return self.fetch(query,param)
    
    def get_date_by_id(self,id):
        query = "SELECT date FROM message WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)
    
    def get_id_chanel_by_id(self,id):
        query = "SELECT id_chanel FROM message WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)
    
    def get_id_user_by_id(self,id):
        query = "SELECT id_user FROM message WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)
    
    def get_id_by_message(self,message):
        query = "SELECT id FROM message WHERE message = %s"
        param = (message,)
        return self.fetch(query,param)
    
    def get_id_by_date(self,date):
        query = "SELECT id FROM message WHERE date = %s"
        param = (date,)
        return self.fetch(query,param)
    
    def get_id_user_by_message(self,message):
        query = "SELECT id_user FROM message WHERE message = %s"
        param = (message,)
        return self.fetch(query,param)
    
    def get_date_by_message(self,message):
        query = "SELECT date FROM message WHERE message = %s"
        param = (message,)
        return self.fetch(query,param)
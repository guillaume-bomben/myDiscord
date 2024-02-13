from DB import DB

class message(DB):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.data_liste = []
    
    def create(self,message,date,id_channel,id_user):
        query = "INSERT INTO message (message,date,id_channel,id_user) VALUES (%s,%s,%s,%s)"
        param = (message,date,id_channel,id_user)
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
    
    def update_id_channel(self,id,id_channel):
        query = "UPDATE message SET id_channel = %s WHERE id = %s"
        param = (id_channel,id)
        self.executeQuery(query,param)
    
    def update_id_user(self,id,id_user):
        query = "UPDATE message SET id_user = %s WHERE id = %s"
        param = (id_user,id)
        self.executeQuery(query,param)
    
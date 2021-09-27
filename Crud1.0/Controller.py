from Conecction import ConnectionDB

class ControllerCrud:
    def ListUser(self):
        cur = ConnectionDB().CursorCrud()
        sql = "SELECT * FROM userData"
        cur.execute(sql)
        return [row for row in cur]
    
    def InsertUser(self,id,name,lastname,password):
        con = ConnectionDB()
        query = "INSERT INTO userData(id,name,lastname,password) VALUES(?,?,?,?)"
        data = (id,name,lastname,password)
        con.CommitCrud(query,data)
        
    def UpdateUser(self,id,name,lastname,password):
        con = ConnectionDB()
        query = "UPDATE userData SET  name=?, lastname=?, password=? WHERE id = ?"
        data = (name,lastname,password,id)
        con.CommitCrud(query,data)
    
    def DeleteUser(self,id):
        con = ConnectionDB()
        query = "DELETE FROM userData WHERE id= ?"
        data = (id)
        con.CommitCrud(query,data)
        
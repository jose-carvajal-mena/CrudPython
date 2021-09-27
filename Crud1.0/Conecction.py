import pyodbc

class ConnectionDB:
  
    def __init__(self):
        self.connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            'Server=DESKTOP-0EF6RBK\SQLEXPRESS;'
                            'Database=CrudPython;'
                            'UID=sa;'
                            'PWD=123456')
        
    def CursorCrud(self):
        return self.connection.cursor()
    
    def CommitCrud(self,query,data):
        self.CursorCrud().execute(query,data)
        self.connection.commit()
        self.CursorCrud().close()




from Controller import ControllerCrud

Main = ControllerCrud()

Main.InsertUser(1,"Manuel","Guerrero","java.8")
Main.UpdateUser(1,"Manuel","Guerrero","java.9")
#Main.DeleteUser(1)
print(Main.ListUser())


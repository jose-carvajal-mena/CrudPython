from Controller import ControllerCrud


if __name__ == "__main__":
    Main = ControllerCrud()
    Main.InsertUser(1,"Manuel","Guerrero","java.8")
    Main.UpdateUser(1,"Manuel","Guerrero","java.6")
    #Main.DeleteUser(1)
    print(Main.ListUser())


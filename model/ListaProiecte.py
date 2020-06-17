import mysql.connector
from model.sqlDB import *

class ListaProiecte:
    def __init__(self):
        self.id_proiect, self.nr_bloc = self.getProjectsFromDB()
        self.list_of_projects = [(str(self.id_proiect[i]), str(self.nr_bloc[i])) for i in range(len(self.nr_bloc))]

    def getProjectsFromDB(self):
        try:
            mydb = mysql.connector.connect(
                host=host,
                user=user,
                passwd=passwd,
                database=database
            )
            c = mydb.cursor()

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL table {}".format(error))

        finally:
            if (mydb.is_connected()):
                c.execute("SELECT id_proiect, nr_bloc FROM `proiect` WHERE id_proiect ORDER BY id_proiect")
                myresult = c.fetchall()
                id_proiect = []
                nr_bloc = []
                for i in range(len(myresult)):
                    id_proiect.append(myresult[i][0])
                    nr_bloc.append(myresult[i][1])

                c.close()
                mydb.close()

                return id_proiect, nr_bloc

    def getListOfProjects(self):
        return self.list_of_projects
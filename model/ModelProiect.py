import mysql.connector
from model.sqlDB import *
from model.FactoriPeAn import FactoriPeAn

class ModelProiect:
    def __init__(self, id_proiect, nr_bloc):
        self.id_proiect = id_proiect
        self.nr_bloc = nr_bloc
        # sql cod --> pentru a primi datele legate de proiect
        self.id_timp = 1
        self.factori = FactoriPeAn(self.id_proiect, self.id_timp)
        if self.id_proiect == 0:
            return
        self.getDataProiect()


    def getDataProiect(self):
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
                c.execute("SELECT id_edificiu FROM `proiect` WHERE `id_proiect` = {}".format(self.id_proiect))
                myresult = c.fetchall()
                self.tip_edificiu = myresult[0][0]

                c.execute("SELECT id_locatie FROM `proiect` WHERE id_proiect = {}".format(self.id_proiect))
                myresult = c.fetchall()
                self.id_locatie = myresult[0][0]

                c.execute("SELECT oras, sector, strada FROM `locatie` WHERE id_locatie = {}".format(self.id_locatie))
                myresult = c.fetchall()
                self.oras, self.sector, self.strada = myresult[0]

                c.close()
                mydb.close()

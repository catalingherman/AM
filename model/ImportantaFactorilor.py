import mysql.connector
from model.sqlDB import *

class ImportantaFactorilor:
    def __init__(self):
        self.getDataImportanta()

    def getDataImportanta(self):
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
                c.execute("SELECT valoare FROM `importanta` order by id_importanta")
                myresult = c.fetchall()
                self.importantaFactorului1 = myresult[0][0]
                self.importantaFactorului2 = myresult[1][0]
                self.importantaFactorului3 = myresult[2][0]
                self.importantaFactorului4 = myresult[3][0]
                self.importantaFactorului5 = myresult[4][0]
                self.importantaFactorului6 = myresult[5][0]
                self.importantaFactorului7 = myresult[6][0]
                self.importantaFactorului8 = myresult[7][0]
                self.importantaFactorului9 = myresult[8][0]
                self.importantaFactorului10 = myresult[9][0]
                self.importantaFactorului11 = myresult[10][0]
                self.importantaFactorului12 = myresult[11][0]
                self.importantaFactorului13 = myresult[12][0]

                c.close()
                mydb.close()
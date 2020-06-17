import mysql.connector
import random
from model.sqlDB import *

class FactoriPeAn:
    def __init__(self,id_proiect, id_timp):
        self.id_proiect = id_proiect
        self.id_timp = id_timp
        # sql cod pentru a primi factorii pentru anul respectiv
        self.valoarea_pozitiei_geografice = 0
        self.starea_terenului_amplasarii = 0
        self.poluarea_mediului = 0
        self.zgomotul_inconjurator = 0
        self.calitatea_materialului_constructiei = 0
        self.grosimea_peretilor = 0
        self.calitatea_acoperisului = 0
        self.calitatea_peretilor = 0
        self.securitatea_la_incendiu = 0
        self.nivelul_de_ruinare = 0
        self.calitatea_geamurilor = 0
        self.rezistenta_mecanica = 0
        self.stabilitatea_blocului = 0
        if self.id_proiect == 0:
            return
        self.getDataFactori()


    def getDataFactori(self):
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
                c.execute("SELECT valoare FROM `criterii` WHERE id_proiect = {} and id_timp = {} order by id_factor".format(\
                          self.id_proiect, self.id_timp))
                myresult = c.fetchall()
                if len(myresult) == 13:
                    self.valoarea_pozitiei_geografice = myresult[0][0]
                    self.starea_terenului_amplasarii = myresult[1][0]
                    self.poluarea_mediului = myresult[2][0]
                    self.zgomotul_inconjurator = myresult[3][0]
                    self.calitatea_materialului_constructiei = myresult[4][0]
                    self.grosimea_peretilor = myresult[5][0]
                    self.calitatea_acoperisului = myresult[6][0]
                    self.calitatea_peretilor = myresult[7][0]
                    self.securitatea_la_incendiu = myresult[8][0]
                    self.nivelul_de_ruinare = myresult[9][0]
                    self.calitatea_geamurilor = myresult[10][0]
                    self.rezistenta_mecanica = myresult[11][0]
                    self.stabilitatea_blocului = myresult[12][0]

                c.close()
                mydb.close()

    def randomize(self):
        self.valoarea_pozitiei_geografice = self.getRand()
        self.starea_terenului_amplasarii = self.getRand()
        self.poluarea_mediului = self.getRand()
        self.zgomotul_inconjurator = self.getRand()
        self.calitatea_materialului_constructiei = self.getRand()
        self.grosimea_peretilor = self.getRand()
        self.calitatea_acoperisului = self.getRand()
        self.calitatea_peretilor = self.getRand()
        self.securitatea_la_incendiu = self.getRand()
        self.nivelul_de_ruinare = self.getRand()
        self.calitatea_geamurilor = self.getRand()
        self.rezistenta_mecanica = self.getRand()
        self.stabilitatea_blocului = self.getRand()

    def getRand(self):
        delta = random.random()
        if delta < 0.2:
            delta += 0.2
        delta *= 100
        delta = "{:06.4f}".format(delta)
        return delta
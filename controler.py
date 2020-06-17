
import sys

from model.FactoriPeAn import FactoriPeAn
from model.ImportantaFactorilor import ImportantaFactorilor
from model.ModelProiect import ModelProiect
from view.UiMainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from view.UIDialog import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from model.ListaProiecte import ListaProiecte
from view.UIDialog import Ui_Dialog


class MainProject:
    def __init__(self, ui):
        self.ui = ui
        self.id_proiect = 0
        self.importanta = ImportantaFactorilor()
        self.modelProiect = ModelProiect(self.id_proiect, 0)

    def openProjectClick(self):
        listaProiecte = ListaProiecte()
        listOfProjects = listaProiecte.getListOfProjects()
        DialogOpenProject_init = DialogOpenProject(listOfProjects, self)
        DialogOpenProject_init.show()
        DialogOpenProject_init.exec_()

    #exit with ok from openProjectDialog
    def projectIsSelected(self, project):
        # despartirea id-ului de nr_bloc
        self.id_proiect, nr_bloc = project.split()
        self.modelProiect = ModelProiect(self.id_proiect, nr_bloc)
        self.ui.lineEdit.setText(self.modelProiect.nr_bloc)
        self.ui.comboBox.setCurrentIndex(self.modelProiect.tip_edificiu - 1)
        self.ui.comboBox_3.setCurrentText(self.modelProiect.oras)
        self.ui.comboBox_4.setCurrentText(self.modelProiect.sector)
        self.ui.lineEdit_5.setText(self.modelProiect.strada)
        self.ui.comboBox_2.setCurrentIndex(0)

        self.ui.afisareFactori(self.modelProiect.factori, self.importanta)


    def timeActivator(self):
        self.ui.comboBox_2.currentIndexChanged.connect(self.detectChange)

    def detectChange(self):
        if(self.id_proiect != 0):
            id_timp = self.ui.comboBox_2.currentIndex() + 1
            self.modelProiect.factori = FactoriPeAn(self.id_proiect, id_timp)
            self.ui.afisareFactori(self.modelProiect.factori, self.importanta)

    def selectNewProject(self):
        self.ui.setAllToDefault()
        self.id_proiect = 0
        self.modelProiect = ModelProiect(0, 0)

    def randomize(self):
        self.modelProiect.factori.randomize()
        self.ui.afisareFactori(self.modelProiect.factori, self.importanta)

# openProjectDialog
class DialogOpenProject(QDialog, Ui_Dialog):
    def __init__(self, listOfProjects, mainwindow):
        QDialog.__init__(self)
        self.setupUi(self, listOfProjects)
        self.mainwindow = mainwindow
        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(self.reject_data)

    def accept_data(self):
        self.mainwindow.projectIsSelected(self.listWidget.currentItem().text())
        self.close()

    def reject_data(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    project = MainProject(ui)
    ui.setupUi(MainWindow, project)
    MainWindow.show()
    project.timeActivator()
    sys.exit(app.exec_())

import psutil
import platform
from datetime import datetime
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QToolBar, QAction, QStatusBar, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cpuinfo
import GPUtil



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setGeometry(500, 500, 700, 400) 
        self.setWindowTitle("Best program")
        osI = "OS: " + platform.system() + " " + platform.version()
        cpuT = psutil.cpu_count()
        cpuC = psutil.cpu_count(logical=False)
        cpuN = cpuinfo.get_cpu_info()["brand_raw"]
        cpuI = "Cpu information:\n" + cpuN
        cpuF = cpuinfo.get_cpu_info()["hz_advertised_friendly"]
        self.osL = QLabel(osI, self)
        self.osL.adjustSize()
        self.osL.move(250,25)
        self.osL.setAlignment(Qt.AlignVCenter) 
        self.cpuI = QLabel(cpuI, self)
        self.cpuI.adjustSize()
        self.cpuI.move(25,25)
        self.cpuI.setAlignment(Qt.AlignLeft) 
        self.cpuL = QLabel("Cores: " + str(cpuC) + "\nThreads: " + str(cpuT) + "\nFrequency: " + str(cpuF), self) 
        self.cpuL.move(25, 55) 
        self.cpuL.setStyleSheet("border: 2px solid black;") 
        self.cpuL.setAlignment(Qt.AlignLeft) 
        self.cpuL.adjustSize()
        self.osL.setStyleSheet("border: 1px solid black;") 
        
        print(osI)
        
        toolbar = QToolBar("toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Refresh", self)
        button_action.setStatusTip("buttonTip")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

        self.show()



    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
	
app.exec_()
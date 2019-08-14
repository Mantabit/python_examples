import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QObject
from mainwindow import Ui_MainWindow

#Hint: when running from an iPython console, no initialization of a QApplication object is necessary
app = QApplication(sys.argv)

#create a main window object and initialize its user-interface
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

#define signal handlers and connect them with signals
def on_mainbutton_click(self):
    ui.mainButton.setText("Clicked")
#connect a signal and a slot
ui.mainButton.clicked.connect(on_mainbutton_click)
    
#display the window
window.show()

#start the event loop (not necessary if running from iPython console)
app.exec_()
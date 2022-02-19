from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import mainWindow_geometry
import popup_geometry

class ExampleApp(QtWidgets.QMainWindow, mainWindow_geometry.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
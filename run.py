

from PyQt5 import QtCore, QtGui, QtWidgets
from source.Master import Ui_Form 
from source.codes import code101

def ts():
	code101.test



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.pushButton.clicked.connect(ts)
    Form.show()
    sys.exit(app.exec_())
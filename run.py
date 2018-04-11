from PyQt5 import QtCore, QtGui, QtWidgets
from source.Master import Ui_Form 
from source.code1 import code101



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    btn_scan=code101(ui)
    ui.pushButton.clicked.connect(btn_scan.start)
    Form.show()
    sys.exit(app.exec_())

    
			















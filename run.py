from PyQt5 import QtCore, QtGui, QtWidgets
from source.Master import Ui_Form 
from source.code1 import *


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    btn_scan=code101(ui)
    ui.pushButton.clicked.connect(btn_scan.start)
    btn_add_ip=code102(ui)
    ui.pushButton_2.clicked.connect(btn_add_ip.start)
    btn_remove_ip=code103(ui)
    ui.pushButton_3.clicked.connect(btn_remove_ip.start)
    Form.show()
    sys.exit(app.exec_())
	

    
			















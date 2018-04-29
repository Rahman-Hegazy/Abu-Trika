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
    ui.btn_scan.clicked.connect(btn_scan.start)
    btn_add_ip=code102(ui)
    ui.btn_to_auth.clicked.connect(btn_add_ip.start)
    btn_remove_ip=code103(ui)
    ui.btn_no_auth.clicked.connect(btn_remove_ip.start)
    # btn_auth=code104(ui)
    # ui.btn_auth.clicked.connect(btn_auth.start)
    btn_shutdown=code105(ui)
    ui.btn_shutdown.clicked.connect(btn_shutdown.start)
    btn_restart=code106(ui)
    ui.btn_restart.clicked.connect(btn_restart.start)
    Form.show()
    sys.exit(app.exec_())
	

    
			















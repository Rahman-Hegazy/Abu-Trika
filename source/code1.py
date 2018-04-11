from PyQt5 import QtCore, QtGui, QtWidgets
from . import code2
import threading, time, socket



class code101(QtCore.QThread):
	"""docstring for codeclass"""
	def __init__(self,obj):
		QtCore.QThread.__init__(self)
		self.obj=obj
		
	def __del__(self):
			self.wait()	


	def run(self):
		subnet=self.obj.comboBox.currentText()
		network=self.obj.line_network.text()				

		try:
			socket.inet_aton(network)
		except Exception as e:
			
		else:
			pass
		finally:
			pass


		self.obj.listWidget.addItem(network)

from PyQt5 import QtCore, QtGui, QtWidgets
from . import code2
import threading, time, socket



class code101(QtCore.QThread):
	"""docstring for codeclass"""
	def __init__(self,obj):
		QtCore.QThread.__init__(self)
		self.obj=obj

	signal1=QtCore.pyqtSignal()
	signal2=QtCore.pyqtSignal()


	def __del__(self):
			self.wait()	


	def run(self):
		
		network=self.obj.line_network.text()
		subnet=self.obj.comboBox.currentText()
		self.obj.listWidget.clear()
		self.obj.listWidget.addItem('working....')
		self.signal1.connect(self.disable)
		self.signal1.emit()
		

		try:
			
			socket.inet_aton(network)
			# print(network+'/'+subnet)
			res=code2.code202.scan(network+'/'+subnet)
			


			if len(res)==0:
				self.obj.listWidget.addItem('make sure ip is right')

			

			else :
				self.obj.listWidget.clear()

			
				for r in res:
					self.obj.listWidget.addItem(r)
			


			self.signal2.connect(self.enable)
			self.signal2.emit()
 
		except :
				self.obj.listWidget.clear()
				self.obj.listWidget.addItem("دخل اي بي عدل يابن المرة ")
				self.signal2.connect(self.enable)
				self.signal2.emit()


	def disable(self):
			self.obj.pushButton.setEnabled(False)
			self.obj.comboBox.setEnabled(False)
			self.obj.line_network.setEnabled(False)


	def enable(self):
			self.obj.pushButton.setEnabled(True)		
			self.obj.comboBox.setEnabled(False)
			self.obj.line_network.setEnabled(False)

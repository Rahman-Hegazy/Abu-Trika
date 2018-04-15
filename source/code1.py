from PyQt5 import QtCore, QtGui, QtWidgets
from . import code2




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
		self.obj.listWidget_2.clear()
		self.obj.listWidget.addItem('working....Plz don\'t close')
		self.signal1.connect(self.disable)
		self.signal1.emit()
		

		try:
			
			if not(code2.code202.ipChk(network)):
				raise Exception('invalid ip')
			

			# print(network+'/'+subnet)
			res=code2.code202.scan(network+'/'+subnet)
			


			if len(res)==0:
				self.obj.listWidget.addItem('make sure ip is right')

			

			else :
				self.obj.listWidget.clear()
				self.obj.listWidget_2.clear()
				self.obj.listWidget.addItems(res)	
				self.obj.listWidget_2.addItems(res)	
			


			self.signal2.connect(self.enable)
			self.signal2.emit()
 
		except :
				self.obj.listWidget.clear()
				self.obj.listWidget.addItem("دخل اي بي عدل يابن المرة ")
				self.signal2.connect(self.enable)
				self.signal2.emit()

	# def run(self):
	# 	print(code2.code202.ipChk('192.168.1.1'))
	


	def disable(self):
			self.obj.pushButton.setEnabled(False)
			self.obj.comboBox.setEnabled(False)
			self.obj.line_network.setEnabled(False)


	def enable(self):
			self.obj.pushButton.setEnabled(True)		
			self.obj.comboBox.setEnabled(True)
			self.obj.line_network.setEnabled(True)







# class code102(QtCore.QThread):

# 	def __init__(self, obj):
# 		QtCore.QThread.__init__(self)
# 		self.obj=obj
	
# 	def __del__(self):
# 		self.wait()


# 	def run(self):
# 		 pass




class code102(QtCore.QThread):

	def __init__(self, obj):
		QtCore.QThread.__init__(self)
		self.obj=obj
	
	def __del__(self):
		self.wait()


	def run(self):
		items=self.obj.listWidget_2.selectedItems()
		if not items : return
		for item in items:	
			 self.obj.listWidget_2.takeItem(self.obj.listWidget_2.row(item))
			 self.obj.listWidget_3.addItem(item.text())



class code103(QtCore.QThread):

	def __init__(self, obj):
		QtCore.QThread.__init__(self)
		self.obj=obj
	
	def __del__(self):
		self.wait()


	def run(self):
		items=self.obj.listWidget_3.selectedItems()
		if not items : return
		for item in items:	
			 self.obj.listWidget_3.takeItem(self.obj.listWidget_3.row(item))
			 self.obj.listWidget_2.addItem(item.text())


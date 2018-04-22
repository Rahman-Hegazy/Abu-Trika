# author RahmanHegazy7

from PyQt5 import QtCore, QtGui, QtWidgets
from . import code2



# scan thread
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
		subnet=self.obj.combo_netmask.currentText()
		self.obj.list_ip.clear()
		self.obj.list_ip_2.clear()
		self.obj.list_ip.addItem('working....Plz don\'t close')
		self.signal1.connect(self.disable)
		self.signal1.emit()
		

		try:
			
			if not(code2.code202.ipChk(network)):
				raise Exception('invalid ip')
			

			# print(network+'/'+subnet)
			res=code2.code202.scan(network+'/'+subnet)
			


			if len(res)==0:
				self.obj.list_ip.addItem('make sure ip is right')

			

			else :
				self.obj.list_ip.clear()
				self.obj.list_ip_2.clear()
				self.obj.list_ip.addItems(res)	
				self.obj.list_ip_2.addItems(res)	
			


			self.signal2.connect(self.enable)
			self.signal2.emit()
 
		except :
				self.obj.list_ip.clear()
				self.obj.list_ip.addItem("please enter a valid ip")
				self.signal2.connect(self.enable)
				self.signal2.emit()

	# def run(self):
	# 	print(code2.code202.ipChk('192.168.1.1'))
	


	def disable(self):
			self.obj.btn_scan.setEnabled(False)
			self.obj.combo_netmask.setEnabled(False)
			self.obj.line_network.setEnabled(False)


	def enable(self):
			self.obj.btn_scan.setEnabled(True)		
			self.obj.combo_netmask.setEnabled(True)
			self.obj.line_network.setEnabled(True)







# class code102(QtCore.QThread):

# 	def __init__(self, obj):
# 		QtCore.QThread.__init__(self)
# 		self.obj=obj
	
# 	def __del__(self):
# 		self.wait()


# 	def run(self):
# 		 pass



# >> thread
class code102(QtCore.QThread):

	def __init__(self, obj):
		QtCore.QThread.__init__(self)
		self.obj=obj
	
	def __del__(self):
		self.wait()


	def run(self):
		items=self.obj.list_ip_2.selectedItems()
		if not items : return
		for item in items:	
			 self.obj.list_ip_2.takeItem(self.obj.list_ip_2.row(item))
			 self.obj.list_ip_3.addItem(item.text())


# << thread
class code103(QtCore.QThread):

	def __init__(self, obj):
		QtCore.QThread.__init__(self)
		self.obj=obj
	
	def __del__(self):
		self.wait()


	def run(self):
		items=self.obj.list_ip_3.selectedItems()
		if not items : return
		for item in items:	
			 self.obj.list_ip_3.takeItem(self.obj.list_ip_3.row(item))
			 self.obj.list_ip_2.addItem(item.text())


#auth thread
# class code104(QtCore.QThread):

# 	def __init__(self, obj):
# 		QtCore.QThread.__init__(self)
# 		self.obj=obj
	
# 	def __del__(self):
# 		self.wait()


# 	def run(self):
# 		if self.obj.line_user.text(): 
# 			if self.obj.line_pass.text()==self.obj.line_pass_again.text():
# 				user=self.obj.line_user.text()
# 				password=self.obj.line_pass.text()
				
# 				for x in range(self.obj.list_ip_3.count()):
# 					if code2.code202.auth(user,passwords,self.obj.list_ip_3.row(x).text())
# 						self.obj.list_success.addItem('failed to auth'+': '+list_ip_3.row(x).text())
# 					else:
# 						self.obj.list_success.addItem('success: '+list_ip_3.row(x).text())


# 			else:
# 				self.obj.list_success.clear()
# 				self.obj.list_success.addItem("passwords don't match")

# 		else:
# 			self.obj.list_success.clear()
# 			self.obj.list_success.addItem('please provide ur user name ')		





#shutdown thread
class code105(QtCore.QThread):

	def __init__(self, obj):
		QtCore.QThread.__init__(self)
		self.obj=obj
	
	def __del__(self):
		self.wait()


	def run(self):
	if user=self.obj.line_user_controls.text():
	 	
		if self.obj.line_pass_again_controls.text()==line_pass_controls.text():
			password=self.obj.list_pass_controls.text()
			code2.code202.shutdown(user,password)
		else:
			self.obj.list_success_controls.addItem('passwords don\'t match')

	else:
		self.obj.list_success_controls.addItem('user name must be provided')
					


#restart thread
class code106(QtCore.QThread):

	def __init__(self, obj):
		QtCore.QThread.__init__(self)
		self.obj=obj
	
	def __del__(self):
		self.wait()


	def run(self):
		if user=self.obj.line_user_controls.text():
	 	
			if self.obj.line_pass_again_controls.text()==self.obj.line_pass_controls.text():
				password=self.obj.list_pass_controls.text()
				code2.code202.restart(user,password)

			else:
				self.obj.list_success_controls.addItem('passwords don\'t match')

		else:
			self.obj.list_success_controls.addItem('user name must be provided')
	

			
import nmap,sys,os,pexpect

class code202(object):
	"""docstring for code2"""
	def __init__(self, arg):
		super(code2, self).__init__()
		self.arg = arg
		
		#scan hosts 
	def scan(ip):
		nm = nmap.PortScanner()
		nm.scan(hosts=ip, arguments='-n -sP -PE  -PA21,23,80,3389') #PR
		return nm.all_hosts()

		# hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
		# for host, status in hosts_list:
		# 	print('{0}:{1}'.format(host, status))		

		#check ip validity
	def ipChk(ip_str):
	    if len(ip_str.split()) == 1:
	        ipList = ip_str.split('.')
	        if len(ipList) == 4:
	            for i, item in enumerate(ipList):
	                try:
	                    ipList[i] = int(item)
	                except:
	                    return False
	                if not isinstance(ipList[i], int):
	                    return False
	            if max(ipList) < 256:
	                return True
	            else:
	                return False
	        else:
	            return False
	    else:
	        return False


	#authenticate machines 

	# def auth(user,password,ip):
	# 	#here goes the code of authentication         
	# 	str_ssh = '/usr/bin/ssh-copy-id  %s@%s' %(user,ip)
	# 	child = pexpect.spawn( str_ssh )
	# 	try:
	# 		index = child.expect(['continue connecting \(yes/no\)','\'s password:',pexpect.EOF],timeout=20)
	# 		print(index)
	# 		if index == 0:
	# 			child.sendline('yes')
	# 			# print(child.after,child.before)
	# 		if index == 1:
	# 			child.sendline(password)
	# 			child.expect('password:')
	# 			child.sendline(password)
	# 			# print child.after,child.before
	# 			return 0
	# 		if index == 2:
	# 			# print '[ failed ]'
	# 			# print child.after,child.before
	# 			child.close()
	# 			return 1
	# 	except pexpect.TIMEOUT:
	# 		# print child.after,child.before
	# 		child.close()
	# 		return 1
	# 	else:
	# 		print('failed')
	# 		return 1 

		#shutdown machines
	def shutdown(user,password,ip):

		try:
			ssh_str='ssh -o StrictHostKeyChecking=no '+user+'@'+ip+' systemctl poweroff'
			child=pexpect.spawn(ssh_str)
			child.expect_exact(':')
			child.sendline(password)
			child.expect(pexpect.EOF,timeout=None)
			return 0 			
		except Exception as e:
			return 1


		#restart machines 
	def restart(user,password,ip):
		try:
			ssh_str='ssh -o StrictHostKeyChecking=no '+user+'@'+ip+' systemctl reboot'
			child=pexpect.spawn(ssh_str)
			child.expect_exact(':')
			child.sendline(password)
			child.expect(pexpect.EOF,timeout=None)
			return 0 			
		except Exception as e:
			return 1





		#backup 
	def backup(user,ip,destination,source):
		pass
		

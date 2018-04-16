import nmap

class code202(object):
	"""docstring for code2"""
	def __init__(self, arg):
		super(code2, self).__init__()
		self.arg = arg
		

	def scan(ip):
		nm = nmap.PortScanner()
		nm.scan(hosts=ip, arguments='-n -sP -PE  -PA21,23,80,3389') #PR
		return nm.all_hosts()

		# hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
		# for host, status in hosts_list:
		# 	print('{0}:{1}'.format(host, status))		


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


	
	def auth(user,password,ip):
		#here goes the code of authentication         
		
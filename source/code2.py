import nmap

class code202(object):
	"""docstring for code2"""
	def __init__(self, arg):
		super(code2, self).__init__()
		self.arg = arg
		

	def scan(ip):
		nm = nmap.PortScanner()
		nm.scan(hosts=ip, arguments='-n -sP -PE -PR -PA21,23,80,3389')
		return nm.all_hosts()

		# hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
		# for host, status in hosts_list:
		# 	print('{0}:{1}'.format(host, status))		
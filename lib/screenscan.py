
try:
	import re
	import datetime
	import subprocess
	from lib.core.core import Core
	from lib.screen.webscan import WebScan
	from lib.core.threadpool import Worker,ThreadPool	
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class ScreenScan(WebScan):

	def __init__(self, args, output_dir):

		self.__args = args
		self.__open_ports_reg = { "http":"80/open/tcp//", "https":"443/open/tcp//" }

		WebScan.__init__(self, args, output_dir)	


	def _run(self):
		
		cmd = "{0} {1}".format(Core.commands_path["nmap"], self._nmap_options)
		proc = subprocess.Popen([cmd], shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE,).communicate()
		
		result = self.__parse_nmap_scan()

		if result:	
			self.__take_screenshot(result)	


	def __parse_nmap_scan(self):
	
		result = {}

		self._result_file.seek(0)
		for line in self._result_file:
			for port, reg in self.__open_ports_reg.iteritems():
				if re.search(reg, line):
					ip = line.split()[1]
					try:
						result[ip] = "{0},{1}".format(result[ip], port)
					except KeyError:
						result[ip] = "{0}".format(port)
					except Exception, err:
						self._result_file.close()
						Core.print_erro(err)

		self._result_file.close()
		
		return result


	def __run_phantomjs(self, cmd):

		proc = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,).communicate()


	def __take_screenshot(self, ip_list):

		pool = ThreadPool(self.__args.thread)

		for ip, ports in ip_list.iteritems():
			for port in ports.split(","):
				url = "{0}://{1}".format(port, ip)
				output_file = "{0}{1}_{2}-{3}.png".format(self._output_dir, ip, port, datetime.datetime.now().strftime("%Y%m%d%H%M%S")) 	
				phantomjs_cmd = "{0} --ignore-ssl-errors=yes {1} {2} {3}".format(Core.commands_path["phantomjs"], self.__args.rasterize, url, output_file)

				pool.add_task(self.__run_phantomjs, phantomjs_cmd)

		pool.wait_completion()

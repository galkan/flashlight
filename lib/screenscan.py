
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

	def __init__(self, args):

		self.__urls = []
		self.__args = args

		WebScan.__init__(self, self.__args)	


	def _run(self, logger):
		
		cmd = "{0} {1}".format(Core._commands_path["nmap"], self._nmap_options)

		logger._logging("START: Nmap Screen Scan: {0}".format(cmd))
		cmd_list = shlex.split(cmd)
		proc = subprocess.Popen(cmd_list, stdout = subprocess.PIPE, stderr = subprocess.PIPE,).communicate()
		logger._logging("STOP: Nmap Screen Scan")

		self.__parse_nmap_scan(logger)


	def __parse_nmap_scan(self, logger):
	
		self._result_file.seek(0)

		for line in self._result_file:
			for port in self._scan_options.split(","):
				if re.search("{0}/open/tcp".format(port), line):
					ip = line.split()[1]
					if port != "443":
						self.__urls.append("http://{0}:{1}".format(ip,port))
					else:
						self.__urls.append("https://{0}:443".format(ip))

		self._result_file.close()

		if self.__urls:
			self.__take_screenshot(logger)	


	def __take_screenshot(self, logger):

		logger._logging("START: Screen Scan {0} threads".format(self.__args.thread))
		pool = ThreadPool(self.__args.thread)

		for url in self.__urls:
			output_file = "{0}{1}_{2}.png".format(self._output_dir, url.split("/")[2], datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
			phantomjs_cmd = "{0} --ignore-ssl-errors=true {1} {2} {3}".format(Core._commands_path["phantomjs"], self.__args.rasterize, url, output_file)
			
			logger._logging("Taking screenshot: {0}".format(url.split("/")[2]))
			pool.add_task(self.__run_phantomjs, phantomjs_cmd)

		pool.wait_completion()
		logger._logging("Finished Screenshot Scan. Results saved in {0} folder".format(self._output_dir))
					

	def __run_phantomjs(self, cmd):

		cmd_list = shlex.split(cmd)
		proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE,).communicate()


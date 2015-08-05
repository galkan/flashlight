
try:
	import re
	import datetime
	import tempfile
	import subprocess
	from lib.active.corescanner import CoreScanner
	from lib.core.config_parser import ConfigParser
	from lib.core.exceptions import FlashLightExceptions
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class PingScan(CoreScanner):

    	def __init__(self, destination, output_dir, nmap_optimize, scan_type):

		self.__host_up = "Host:\s([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s+\(\)\s+Status:\sUp"       

		self.__ip_file_to_scan = tempfile.NamedTemporaryFile(mode='w+t')
		self.__ip_file_to_scan.write("\n".join([ip_domain.strip() for ip_domain in destination.split(",")]))

		self.__output_file = "{0}{1}-{2}".format(output_dir, scan_type, datetime.datetime.now().strftime("%Y%m%d%H%M"))
        	CoreScanner.__init__(self, self.__ip_file_to_scan.name, self.__output_file, nmap_optimize, scan_type)



	def _run(self, result_file, logger):

		self.__ip_file_to_scan.seek(0)

		gnmap_file = "{0}.gnmap".format(self.__output_file)
		cmd = "{0} -oA {1}".format(self._proc_cmd, self.__output_file)

		logger._logging("START: Nmap Ping Scan")
		logger._logging("CMD - Ping Scan: {0}".format(cmd))

		proc = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE,).communicate()
		try:
			with open(gnmap_file, "r") as fd:
				result_file.write("\n".join([ re.search(self.__host_up, line).groups()[0] for line in fd  if re.search(self.__host_up, line) ]))
		except Exception, err:
			raise FlashLightExceptions(str(err))
		
		logger._logging("STOP: Nmap Ping Scan")


try:
	import datetime
	from lib.active.corescanner import CoreScanner
	from lib.core.config_parser import ConfigParser
	from lib.core.exceptions import FlashLightExceptions	
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class ScriptScan(CoreScanner):

    	def __init__(self, config_file, output_dir, ip_file_to_scan, nmap_optimize, scan_type):

		self._ip_file_to_scan = ip_file_to_scan
		try:
			self._scan_options = ConfigParser.get_scripts_options(config_file)
		except Exception, err:
			raise FlashLightExceptions(err)		

		output_file = "{0}{1}-{2}".format(output_dir, scan_type, datetime.datetime.now().strftime("%Y%m%d%H%M"))

		CoreScanner.__init__(self, self._ip_file_to_scan.name, output_file, nmap_optimize, scan_type)


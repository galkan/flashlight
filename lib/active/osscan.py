
try:
	from lib.core.config_parser import ConfigParser
	from lib.active.corescanner import CoreScanner
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class OsScan(CoreScanner):

    	def __init__(self,  output_dir, ip_file_to_scan, nmap_optimize, scan_type):

		self.ip_file_to_scan = ip_file_to_scan

		CoreScanner.__init__(self, self.ip_file_to_scan.name, output_dir, nmap_optimize, scan_type)



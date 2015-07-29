
try:
	from lib.core.config_parser import ConfigParser
	from lib.active.corescanner import CoreScanner
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class ScriptScan(CoreScanner):

    	def __init__(self, config_file, output_dir, ip_file_to_scan, nmap_optimize, scan_type):

		self.ip_file_to_scan = ip_file_to_scan
		self.scan_options = ConfigParser.get_scripts_options(config_file)

		CoreScanner.__init__(self, self.ip_file_to_scan.name, output_dir, nmap_optimize, scan_type)


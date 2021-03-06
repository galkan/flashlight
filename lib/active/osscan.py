
try:
	import datetime
	from lib.active.corescanner import CoreScanner
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class OsScan(CoreScanner):

    	def __init__(self,  output_dir, ip_file_to_scan, nmap_optimize, scan_type):

		self._ip_file_to_scan = ip_file_to_scan

		output_file = "{0}{1}-{2}".format(output_dir, scan_type, datetime.datetime.now().strftime("%Y%m%d%H%M"))

		CoreScanner.__init__(self, self._ip_file_to_scan.name, output_file, nmap_optimize, scan_type)



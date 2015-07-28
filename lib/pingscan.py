
try:
	import re
	import tempfile
	import subprocess
	from lib.corescanner import CoreScanner
	from lib.core.config_parser import ConfigParser
	from lib.core.exceptions import FlashLightExceptions
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class PingScan(CoreScanner):

    	def __init__(self, destination, output_dir, nmap_optimize, scan_type):

		self.host_up = "Host:\s([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s+\(\)\s+Status:\sUp"       

		self.ip_file_to_scan = tempfile.NamedTemporaryFile(mode='w+t')
		self.ip_file_to_scan.write("\n".join([ip_domain.strip() for ip_domain in destination.split(",")]))

        	CoreScanner.__init__(self, self.ip_file_to_scan.name, output_dir, nmap_optimize, scan_type)


	def run(self, result_file):

		self.ip_file_to_scan.seek(0)

		gnmap_file = "{0}.gnmap".format(self.output_file)
		cmd = "{0} -oA {1}".format(self.proc_cmd, self.output_file)

		print "PingScan: %s"% cmd

		proc = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE,).communicate()
		try:
			with open(gnmap_file, "r") as fd:
				result_file.write("\n".join([ re.search(self.host_up, line).groups()[0] for line in fd  if re.search(self.host_up, line) ]))
		except Exception, err:
			raise FlashLightExceptions(str(err))

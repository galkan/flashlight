
try:
	import os		
	import time
	import datetime
	import subprocess
	from lib.core.core import Core
except ImportError, err:
        import sys
        sys.stdout.write("%s\n" %err)
        sys.exit(1)


class CoreScanner(object):
	
	output_dir_control = False
	scan_type_options = { "PingScan":"-n -sn -T5", "PortScan":"-n -Pn -T5 --open", "OsScan":"-n -Pn -O -T5", "ScriptScan":"-n -Pn -T5" }

        def __init__(self, ip_file_to_scan, output_dir, nmap_optimize, scan_type):
	
		self.scan_type = scan_type
		self.ip_file = ip_file_to_scan
		self.output_dir = "{0}/nmap/".format(output_dir)

		if not CoreScanner.output_dir_control:
			try:
				os.makedirs(self.output_dir)
			except Exception, err:
				pass

			CoreScanner.output_dir_control = True

		if nmap_optimize:
			nmap_options = "{0} {1} -iL {2}".format(CoreScanner.scan_type_options[self.scan_type], Core.nmap_optimize, self.ip_file)
		else:
			nmap_options = "{0} -iL {1}".format(CoreScanner.scan_type_options[self.scan_type], self.ip_file)

		now = datetime.datetime.now()
		if output_dir[0] != "/":
			self.output_file = "{0}/{1}/nmap/{2}-{3}".format(os.getcwd(), output_dir, scan_type,now.strftime("%Y%m%d%H%M"))
		else:
			self.output_file = "{0}/nmap/{1}-{2}".format(output_dir, scan_type, now.strftime("%Y%m%d%H%M"))

		self.proc_cmd = "{0} {1}".format(Core.commands_path["nmap"], nmap_options)
	

	def run(self):

		self.ip_file_to_scan.seek(0)
		if self.scan_type in ( "PortScan", "ScriptScan"):
			cmd = "{0} {1} -oA {2}".format(self.proc_cmd, self.scan_options, self.output_file)
		else:
			cmd = "{0} -oA {1}".format(self.proc_cmd, self.output_file)

		print "%s : %s"% (self.scan_type, cmd)
		proc = subprocess.Popen([cmd], shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE,).communicate()

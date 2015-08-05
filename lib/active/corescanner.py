
try:
	import os		
	import time
	import datetime
	import subprocess
	from lib.core.core import Core,InitDirFile
except ImportError, err:
	from lib.core.core import Core
        Core.print_error(err)


class CoreScanner(object):
	
	__scan_type_options = { "PingScan":"-n -sn -T5", "PortScan":"-n -Pn -T5 --open", "OsScan":"-n -Pn -O -T5", "ScriptScan":"-n -Pn -T5" }

        def __init__(self, ip_file_to_scan, output_file, nmap_optimize, scan_type):
	
		self.__scan_type = scan_type
		self.__ip_file = ip_file_to_scan
		self.__output_file = output_file
	
		self.__nmap_options = "{0} {1} -iL {2}".format(CoreScanner.__scan_type_options[self.__scan_type], Core.nmap_optimize, self.__ip_file) if nmap_optimize else "{0} -iL {1}".format(CoreScanner.__scan_type_options[self.__scan_type], self.__ip_file)
			
		self._proc_cmd = "{0} {1}".format(Core._commands_path["nmap"], self.__nmap_options)


	def _run(self, logger):

		# it is inherited from portscan,osscan,scriptscan class
		self._ip_file_to_scan.seek(0)

		cmd = "{0} {1} -oA {2}".format(self._proc_cmd, self._scan_options, self.__output_file) if self.__scan_type in ( "PortScan", "ScriptScan") else "{0} -oA {1}".format(self._proc_cmd, self.__output_file)
		
		logger._logging("Starting {0} scan".format(self.__scan_type))
		logger._logging("{0} : {1}".format(self.__scan_type, cmd))
		
		proc = subprocess.Popen([cmd], shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE,).communicate()

		logger._logging("Stopped {0} scan".format(self.__scan_type))

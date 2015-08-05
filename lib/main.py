
try:
	import os
	import sys
	import signal
	import argparse
	from lib.core.core import Core
	from lib.core.logger import Logger
	from lib.filterscan import FilterScan
	from lib.screenscan import ScreenScan
	from lib.activescan import ActiveScan
	from lib.passivescan import PassiveScan
	from lib.core.exceptions import FlashLightExceptions	
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class Main(object):
		
	def __init__(self):
		
		__service_name_list = ("active", "passive", "screen", "filter")

                usage = "Usage: use --help for further information"
		description = "Flashligth: Light your ways through Pentest"
                parser = argparse.ArgumentParser(description = description, usage = usage)

		parser.add_argument('-p', '--project', dest = 'project', action = 'store', help = 'Project Name', required = True)
                parser.add_argument('-s', '--scan_type', dest = 'scan_type', help = 'Scan Type', choices = __service_name_list, required = True)
		parser.add_argument('-d', '--destination', dest = 'destination', action = 'store', help = 'Target Ip/Host Name')		
		parser.add_argument('-c', '--config', dest = 'config_file', action = 'store', help = 'Configuration File', metavar = 'FILE', default='config/flashlight.yaml')
		parser.add_argument('-i', '--interface', dest = 'interface', action = 'store', help = 'Interface')
		parser.add_argument('-f', '--pcap_file', dest = 'pcap', action = 'store', help = 'Pcap File for Filtering')
		parser.add_argument('-r', '--rasterize', dest = 'rasterize', action = 'store', default = "/usr/local/bin/rasterize.js" , help = "Rasterize Js File For ScreenShot")
		parser.add_argument('-t', '--thread', dest = 'thread', action = 'store', help = 'Thread Number', default = 10, type = int)
		parser.add_argument('-o', '--output', dest = 'output', action = 'store', help = 'Output Directory', default = os.getcwd())
		parser.add_argument('-a', '--alive', dest = 'is_alive', action = 'store_true', help = 'Ping Scan to Investigate Which Ip Address Are Up Before Scanning', default = None)
		parser.add_argument('-l', '--log', dest = 'log_file', action = 'store', help = 'Log File', metavar = 'FILE', default = "flashlight.log")
		parser.add_argument('-k', '--passive_timeout', dest = 'passive_timeout', action = 'store', help = 'Passive Scan Timeout Value', default = 15, type = int)
		parser.add_argument('-m', '--mim', dest = 'mim', action = 'store_true', help = 'Capture the Traffic When Performing Man in The Middle', default = None)
		parser.add_argument('-n', '--nmap-optimize', dest = 'nmap_optimize', action = 'store_true', help = 'Use Some Sxtra Nmap Options To Optimize Scanning For Performance Tuning', default = None)
		parser.add_argument('-v', '--verbose', dest = 'verbose', action = 'store_true', help = 'Verbose Output', default = None)
		parser.add_argument('-V', '--version', action='version', version='%(prog)s 1.0')

		self._args = parser.parse_args()


		command_list = { __service_name_list[0] : {self._args.destination : "-d/--destination"} , __service_name_list[1] : {self._args.interface : "-i/--interface"}, __service_name_list[2] : {self._args.destination : "-d/--destination"}, __service_name_list[3] : {self._args.pcap : "-f/--pcap_file"} }

		for key, value in command_list[self._args.scan_type].iteritems():
			if key is None:
				parser.error("{0} argument is required".format(value))

		try:
			self.__services = { __service_name_list[0]:ActiveScan(self._args), __service_name_list[1]:PassiveScan(self._args), __service_name_list[2]:ScreenScan(self._args), __service_name_list[3]:FilterScan(self._args) }	
		except FlashLightExceptions, err:
			Core.print_error(err)

		self.__logger = Logger(self._args.log_file, self._args.verbose)



	def _run(self, scan_type):
	
		""" Run flashligth as a root"""

		if os.geteuid() != 0:
			Core.print_error("Run as ROOT")

		signal.signal(signal.SIGINT, self.signal_handler)

		self.__services[scan_type]._run(self.__logger)



	def signal_handler(self, signal, frame):

		""" Set Signal """

		Core.print_error("Bye")

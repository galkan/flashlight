
try:
	import os
	import sys
	import signal
	import argparse
<<<<<<< Updated upstream
	import subprocess
=======
>>>>>>> Stashed changes
	from lib.core.core import Core
	from lib.screenscan import ScreenScan
	from lib.activescan import ActiveScan
	from lib.passivescan import PassiveScan
<<<<<<< Updated upstream
	from lib.core.threadpool import Worker,ThreadPool				
=======
>>>>>>> Stashed changes
	from lib.core.exceptions import FlashLightExceptions	
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class Main(object):
		
	def __init__(self):
		
<<<<<<< Updated upstream
		self.__services = { "active":self.__active_scan, "passive":self.__passive_scan, "screen":self.__takescreen }	
=======
		__service_name_list = ("active","passive","screen","filter")
>>>>>>> Stashed changes

                usage = "Usage: use --help for further information"
		description = "Flashligth: Light your ways through Pentest"
                parser = argparse.ArgumentParser(description = description, usage = usage)

		parser.add_argument('-p', '--project', dest = 'project', action = 'store', help = 'Project Name', required = True)
<<<<<<< Updated upstream
                parser.add_argument('-s', '--scan_type', dest = 'scan_type', help = 'Scan Type', choices = self.__services.keys(), required = True)
=======
                parser.add_argument('-s', '--scan_type', dest = 'scan_type', help = 'Scan Type', choices = __service_name_list, required = True)
>>>>>>> Stashed changes
		parser.add_argument('-d', '--destination', dest = 'destination', action = 'store', help = 'Target Ip/Host Name')		
		parser.add_argument('-c', '--config', dest = 'config_file', action = 'store', help = 'Configuration File', metavar = 'FILE', default='config/flashlight.yaml')
		parser.add_argument('-i', '--interface', dest = 'interface', action = 'store', help = 'Interface')
		parser.add_argument('-f', '--pcap_file', dest = 'pcap', action = 'store', help = 'Pcap File for Filtering')
		parser.add_argument('-r', '--rasterize', dest = 'rasterize', action = 'store', default = "/usr/local/bin/rasterize.js" , help = "Rasterize Js File For ScreenShot")
		parser.add_argument('-t', '--thread', dest = 'thread', action = 'store', help = 'Thread Number', default = 10, type = int)
<<<<<<< Updated upstream
		parser.add_argument('-o', '--output', dest = 'output', action = 'store', help = 'Output Directory', default = None)
=======
		parser.add_argument('-o', '--output', dest = 'output', action = 'store', help = 'Output Directory', default = os.getcwd())
>>>>>>> Stashed changes
		parser.add_argument('-a', '--alive', dest = 'is_alive', action = 'store_true', help = 'Ping Scan to Investigate Which Ip Address Are Up Before Scanning', default = None)
		parser.add_argument('-l', '--log', dest = 'log_file', action = 'store', help = 'Log File', metavar = 'FILE', default = "flashligth.log")
		parser.add_argument('-k', '--passive_timeout', dest = 'passive_timeout', action = 'store', help = 'Passive Scan Timeout Value', default = 15, type = int)
		parser.add_argument('-m', '--mim', dest = 'mim', action = 'store_true', help = 'Capture the Traffic When Performing Man in The Middle', default = None)
		parser.add_argument('-n', '--nmap-optimize', dest = 'nmap_optimize', action = 'store_true', help = 'Use Some Sxtra Nmap Options To Optimize Scanning For Performance Tuning', default = None)
		parser.add_argument('-v', '--verbose', dest = 'verbose', action = 'store_true', help = 'Verbose Output', default = None)
		parser.add_argument('-V', '--version', action='version', version='%(prog)s 1.0')

		self._args = parser.parse_args()

<<<<<<< Updated upstream
		command_list = { "active" : {self._args.destination : "-d/--destination"} , "passive" : {self._args.interface : "-i/--interface"}, "screen" : {self._args.destination : "-d/--destination"}, "filter" : {self._args.pcap : "-f/--pcap_file"} }
=======
		command_list = { __service_name_list[0] : {self._args.destination : "-d/--destination"} , __service_name_list[1] : {self._args.interface : "-i/--interface"}, __service_name_list[2] : {self._args.destination : "-d/--destination"}, __service_name_list[3] : {self._args.pcap : "-f/--pcap_file"} }
>>>>>>> Stashed changes

		for key, value in command_list[self._args.scan_type].iteritems():
			if key is None:
				parser.error("{0} argument is required".format(value))
<<<<<<< Updated upstream

		if self._args.output is None:
			self.__output_dir = "output/{0}".format(self._args.project)
		else:
			self.__output_dir = "{0}/output/{1}".format(self._args.output, self._args.project)

		try:
			os.makedirs(self.__output_dir)
		except:
			pass



	def __active_scan(self):

		""" Run Nmap In Order To Do Port Scan Through Active Scan """
		
		active = ActiveScan(self._args, self.__output_dir)
		active._run()


	def __passive_scan(self):
	
		""" Capture Traffic in Passive Mode """

		passive = PassiveScan(self._args, self.__output_dir)
		passive._run()	


	def __takescreen(self):

		screen = ScreenScan(self._args, self.__output_dir)
		screen._run()
=======

		self.__services = { __service_name_list[0]:ActiveScan(self._args), __service_name_list[1]:PassiveScan(self._args), __service_name_list[2]:ScreenScan(self._args) }	

>>>>>>> Stashed changes


	def _run(self, scan_type):
	
<<<<<<< Updated upstream
		""" Run flashligth """
=======
		""" Run flashligth as a root"""
>>>>>>> Stashed changes

		if os.geteuid() != 0:
			Core.print_error("Run as ROOT")

		signal.signal(signal.SIGINT, self.signal_handler)
<<<<<<< Updated upstream
		self.__services[scan_type]()
=======

		self.__services[scan_type]._run()

>>>>>>> Stashed changes


	def signal_handler(self, signal, frame):

		""" Set Signal """

		Core.print_error("Bye")


try:
	import tempfile
	from lib.core.core import Core,InitDirFile
	from lib.core.config_parser import ConfigParser
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class WebScan(InitDirFile):

	def __init__(self, args):

		self._scan_options = ConfigParser.get_screen_ports(args.config_file)
		__core_options = "-n -Pn -T5 --open -p T:{0}".format(self._scan_options) if self._scan_options else "-n -Pn -T5 --open -p T:80,443"

		self._result_file = tempfile.NamedTemporaryFile(mode='w+t')
		InitDirFile.__init__(self, [Core.commands_path["phantomjs"], Core.commands_path["nmap"], args.rasterize], args, "screen")

		if args.destination:
			__destination =  " ".join([ip.strip() for ip in args.destination.split(",")])
			self._nmap_options = "{0} {1} -oG {2} {3}".format(__core_options, Core.nmap_optimize, self._result_file.name, __destination) if args.nmap_optimize else  "{0} -oG {1} {2}".format(__core_options, self._result_file.name, __destination)



try:
	import tempfile
	from lib.core.core import Core,InitDirFile
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class WebScan(InitDirFile):

	def __init__(self, args, output_dir):

		core_options = "-n -Pn -T5 --open -p T:80,443"
		self._result_file = tempfile.NamedTemporaryFile(mode='w+t')

		InitDirFile.__init__(self, [Core.commands_path["phantomjs"], Core.commands_path["nmap"], args.rasterize], output_dir, "screen")

		destination =  " ".join([ip.strip() for ip in args.destination.split(",")])
		self._nmap_options = "{0} {1} -oG {2} {3}".format(core_options, Core.nmap_optimize, self._result_file.name, destination) if args.nmap_optimize else  "{0} -oG {1} {2}".format(core_options, self._result_file.name, destination)


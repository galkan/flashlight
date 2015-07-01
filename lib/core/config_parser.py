
__VERSION__ = '0.1'
__AUTHOR__ = 'Galkan'
__DATE__ = '20.07.2014'

try:
        import sys
        from ConfigParser import SafeConfigParser
except ImportError,e:
        import sys
        sys.stdout.write("%s\n" %e)
        sys.exit(1)


class ConfigParser:
	result = {}
	
	@staticmethod
       	def parse(config_file):

		scan_proto = None
		scan_port = None
		scan_options = None
		script_options = None

		if not ConfigParser.result:
			try:
				parser = SafeConfigParser()
                		parser.read(config_file)
              		except Exception, err:
				print >> sys.stderr, err 
				sys.exit(1)

			for section_name in parser.sections():
				if section_name == "ports":
					for name, value in parser.items(section_name):
						if name == "tcp":
							scan_proto = "-sS "
							for port in value.split(","):
								if scan_port is None:
									scan_port = port.strip()
								else:
									scan_port = scan_port + "," + port.strip()
							scan_options = "-sS -p T:%s"% scan_port
							scan_port = None
						elif name == "udp":
							scan_proto = "-sU "
							for port in value.split(","):
								if scan_port is None:
									scan_port = port.strip()
								else:
									scan_port = scan_port + "," + port.strip()
							if scan_options is None:
								scan_options = "-sU -p U:%s"% scan_port
							else:
								scan_options = "-sU " + scan_options + ",U:" + scan_port	
					ConfigParser.result["scan"] = scan_options
				elif section_name == "script":
					for name, value in parser.items(section_name):
						for line in value.split(","):
							if script_options is None:
								script_options = line.strip()
							else:
								script_options = script_options + "," + line.strip()
						ConfigParser.result["script"] = script_options

		return ConfigParser.result



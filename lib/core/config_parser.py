
try:
	import yaml
	from lib.core.exceptions import FlashLightExceptions
except ImportError, err:
	from lib.core.core import Core
	Core.print_err(err)


class ConfigParser(object):

	result = {}
	scan_options = None
	default_ports = "80,443"
<<<<<<< HEAD
=======
	
>>>>>>> origin/master

	@staticmethod
        def parser(config_file):

		if not ConfigParser.result:
			try:
				with open(config_file, 'r') as stream:
    					cfg = yaml.load(stream)
			except IOError:
				raise FlashLightExceptions("{0} cannot be opened !!!".format(config_file))			
			except Exception, err:
				raise FlashLightExceptions(str(err))			        
 
			for section in cfg:
				ConfigParser.result[section] = ','.join([ value.strip() for value  in ''.join([value for value in cfg[section] ]).split(',') ])

                return ConfigParser.result        	



	@staticmethod
        def get_ports_options(config_file):

                if not ConfigParser.scan_options:
                        try:
                                cfg = ConfigParser.parser(config_file)
                        except Exception, err:
                                raise FlashLightExceptions("Error when parsing {0}: {1}".format(config_file, str(err)))

                        try:
                                tcp_ports = "-sS -p T:{0}".format(cfg["tcp_ports"])
                        except:
                                tcp_ports = None

                        try:
                                udp_ports = "U:{0} -sU".format(cfg["udp_ports"])
                        except: 
                                udp_ports = None
                                
                        if tcp_ports and udp_ports:
                                ConfigParser.scan_options = "{0},{1}".format(tcp_ports, udp_ports)
                        elif tcp_ports:
                                ConfigParser.scan_options = tcp_ports
                        elif udp_ports:
                                ConfigParser.scan_options = "-p {0}".format(udp_ports)

                return "-F"  if ConfigParser.scan_options is None else ConfigParser.scan_options

	

	@staticmethod
	def get_scripts_options(config_file):
		
		script_options = None

		try:
			ports_options = ConfigParser.get_ports_options(config_file)
		except Exception, err:
			raise FlashLightExceptions(str(err))	


		if ConfigParser.result["scripts"]:
                	try:
                        	script_options = "--script=default,{0}".format(ConfigParser.result["scripts"])
                	except:
                        	script_options = "--script=default" 
		else:
			try:
        	       		cfg = ConfigParser.parser(config_file)
			except Exception, err:
				raise FlashLightExceptions(str(err))
			
                	try:
                        	script_options = "--script=default,{0}".format(cfg["scripts"])
                	except:
                        	script_options = "--script=default" 
		

		return "{0} {1}".format(ports_options, script_options)



	@staticmethod
	def get_screen_ports(config_file):

		try:
			if ConfigParser.result["screen_ports"]:	
				return ConfigParser.result["screen_ports"]
			else:
				cfg = ConfigParser.parser(config_file)
		except FlashLightExceptions, err:
                       	raise FlashLightExceptions(str(err))
		except:
			return ConfigParser.default_ports
<<<<<<< HEAD

=======
>>>>>>> origin/master

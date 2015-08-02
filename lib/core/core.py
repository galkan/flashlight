
import os
import sys

class Core(object):

	commands_path = { "nmap" : "/usr/bin/nmap", "tshark" : "/usr/bin/tshark", "tcpdump" : "/usr/sbin/tcpdump", "arpspoof" : "/usr/sbin/arpspoof", "phantomjs" : "/usr/local/bin/phantomjs" }
	nmap_optimize = "-min-hostgroup 64 -min-parallelism 64 -host-timeout=300m -max-rtt-timeout=600ms -initial-rtt-timeout=300ms -min-rtt-timeout=300ms -max-retries=2 -min-rate=150"

	@staticmethod
	def print_error(message):
		""" Print error message given """

		print >> sys.stderr, str(message)
		sys.exit(1)



class FileExists(object):

	def __init__(self, file_list):

		for file_name in file_list:
			if not os.path.exists(file_name):
				Core.print_error("{0} Doesn't Exists On The System".format(file_name))



class InitDirFile(FileExists):

<<<<<<< Updated upstream
	def __init__(self, file_list, output_dir, scan_type):
	
		FileExists.__init__(self, file_list)
		
		if output_dir[0] != "/":
                        self._output_dir = "{0}/{1}/{2}/".format(os.getcwd(), output_dir, scan_type)
                else:   
                        self._output_dir = "{0}/{1}/".format(output_dir, scan_type)
=======
	def __init__(self, file_list, args, scan_type):
	
		FileExists.__init__(self, file_list)
		
		self._output_dir = "{0}/output/{1}/{2}/".format(args.output, args.project, scan_type) if args.output.startswith("/") else "{0}/{1}/{2}/{3}".format(os.getcwd(), args.output, args.project, scan_type)
>>>>>>> Stashed changes

                try:
                        os.makedirs(self._output_dir)
                except: 
                        pass

<<<<<<< Updated upstream
		
				
=======
>>>>>>> Stashed changes


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


	@staticmethod
	def is_file_exists(file_name):
                """ Check file whether exists or not """

                if not os.path.exists(Core.commands_path[file_name]):
                        Core.print_error("{0} Doesn't Exists on The System !!!".format(Core.commands_path[file_name]))


class FileExists(object):

	def __init__(self, file_list):
		for file_name in file_list:
			Core.is_file_exists(file_name)

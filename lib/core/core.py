
import sys

class Core(object):

	commands_path = { "nmap" : "/usr/bin/nmap", "tshark" : "/usr/bin/tshark", "tcpdump" : "/usr/sbin/tcpdump", "arpspoof" : "/usr/sbin/arpspoof", "phantomjs" : "/usr/local/bin/phantomjs" }
	nmap_optimize = "-min-hostgroup 64 -min-parallelism 64 -host-timeout=300m -max-rtt-timeout=600ms -initial-rtt-timeout=300ms -min-rtt-timeout=300ms -max-retries=2 -min-rate=150"

	@staticmethod
	def print_error(message):
		print >> sys.stderr, str(message)
		sys.exit(1)

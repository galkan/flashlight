
try:
	import os
	import socket
	import struct
	import datetime
	from lib.core.core import Core,InitDirFile
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class Passive(InitDirFile):

	def __init__(self, output_dir):

		InitDirFile.__init__(self, [Core.commands_path["tcpdump"], Core.commands_path["arpspoof"]], output_dir, "pcap")

		self.__proc_route = "/proc/net/route"
		self._output_file = "{0}{1}.pcap".format(self._output_dir, datetime.datetime.now().strftime("%Y%m%d%H%M"))
	
		self._default_gw = self.__get_default_gw()


	def __get_default_gw(self):

		try:
			with open(self.__proc_route) as fh:
        			for line in fh:
            				fields = line.strip().split()
					if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                				continue

            				return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
		except:
			return None

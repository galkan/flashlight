
try:
	import os
	import socket
	import struct
	import datetime
	from lib.core.core import FileExists
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class Passive(FileExists):

	def __init__(self, output_dir):

		FileExists.__init__(self, ["tcpdump", "arpspoof"])

		self.__proc_route = "/proc/net/route"
		self._output_file = self.__init_pcap_file(output_dir)
	
		self._default_gw = self.__get_default_gw()


	def __init_pcap_file(self, output_dir):

		if output_dir[0] != "/":
                        pcap_output_dir = "{0}/{1}/pcap".format(os.getcwd(), output_dir)
                else:   
                        pcap_output_dir = "{0}/pcap/".format(output_dir)

                try:
                        os.makedirs(pcap_output_dir)
                except: 
                        pass

                return "{0}/{1}.pcap".format(pcap_output_dir, datetime.datetime.now().strftime("%Y%m%d%H%M"))


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

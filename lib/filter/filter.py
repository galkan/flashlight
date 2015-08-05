
try:
	import os
	from lib.core.core import Core, InitDirFile
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class Filter(InitDirFile):

	def __init__(self, pcap_file, args, scan_type):

		InitDirFile.__init__(self, pcap_file, args, scan_type)
	
		self.__pcap_file =  pcap_file[0] if pcap_file[0].startswith("/") else "{0}/{1}".format(os.getcwd(), pcap_file[0])

		self._filter_commands = { "iplist" : "{0} -2 -R 'ip' -T fields  -e ip.src -r {1}".format(Core._commands_path["tshark"], self.__pcap_file),  "hostports" : "{0} -2 -R 'tcp' -T fields -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -r {1}".format(Core._commands_path["tshark"], self.__pcap_file),  "winhosts" : "{0} -2 -R 'browser.command == 0x01' -T fields -e ip.src -e browser.server -r {1}".format(Core._commands_path["tshark"], self.__pcap_file),  "windomains" : "{0} -2 -R 'browser.command == 0x0c' -T fields -e ip.src -e browser.server -r {1}".format(Core._commands_path["tshark"], self.__pcap_file), "top10hosts" : "{0} -2 -R 'ip' -T fields  -e ip.dst -r {1}".format(Core._commands_path["tshark"], self.__pcap_file), "top10conversations" : "{0} -2 -R tcp -T fields -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -E separator=';' -r {1}".format(Core._commands_path["tshark"], self.__pcap_file),  "top10dns" : "{0} -2 -T fields  -e dns.qry.name -E separator=';' -R ' dns and udp.port == 53' -r {1}".format(Core._commands_path["tshark"], self.__pcap_file),  "top10http" : "{0} -2 -R http.request -T fields -e http.host -r {1}".format(Core._commands_path["tshark"], self.__pcap_file) }

#!/usr/bin/python

__VERSION__ = '0.1'
__AUTHOR__ = 'Galkan'
__DATE__ = '06.08.2014'


""" it is derived from https://github.com/argp/nmapdb/blob/master/nmapdb.py """

try:
	import sys
	import xml.dom.minidom
	from xml.etree import ElementTree
except ImportError,e:
        import sys
        sys.stdout.write("%s\n" %e)
        sys.exit(1)


class XmlParser:
	
	def __init__(self, xml_file):
		
		self.xml_file = xml_file
		self.mac = {}
		self.mac_list = {}
		self.os = {}
		self.os_list = {}
		self.script_ret = {}
		self.script = {}
		self.script_list = []
		self.port_service_ret = {}
		self.port_service = {}
		self.port_service_list = []		


	def parser(self, opt):
		
		try:
                	root = xml.dom.minidom.parse(self.xml_file) 		
		except Exception, err:
			print >> sys.stderr, err
			sys.exit(1)

		for host in root.getElementsByTagName("host"):

			try:
                		address = host.getElementsByTagName("address")[0]
                		ip = address.getAttribute("addr")
                		protocol = address.getAttribute("addrtype")
            		except:
				pass

			try:
                		mac_address = host.getElementsByTagName("address")[1]
                		mac = mac_address.getAttribute("addr")
                		mac_vendor = mac_address.getAttribute("vendor")
            		except:
                		mac = ""
                		mac_vendor = ""

			mac_ret = mac + ":" + mac_vendor
			self.mac_list[ip] = mac_ret
			
			if opt == 1:
				try:
                			os = host.getElementsByTagName("os")[0]
                			os_match = os.getElementsByTagName("osmatch")[0]
                			os_name = os_match.getAttribute("name")
                			os_accuracy = os_match.getAttribute("accuracy")
                			os_class = os.getElementsByTagName("osclass")[0]
                			os_family = os_class.getAttribute("osfamily")
                			os_gen = os_class.getAttribute("osgen")
            			except:	
                			os_name = ""
                			os_accuracy = ""
                			os_family = ""
                			os_gen = ""
			
				os_ret = os_family + ":" + os_name + ":" + os_accuracy
				self.os_list[ip] = os_ret				

			elif opt == 2:
				try:
                			ports = host.getElementsByTagName("ports")[0]
                			ports = ports.getElementsByTagName("port")
            			except:
                			continue
			
				for port in ports:
					port_number = port.getAttribute("portid")
                			protocol = port.getAttribute("protocol")
                			state_el = port.getElementsByTagName("state")[0]
                			state = state_el.getAttribute("state")

					try:
                    				service = port.getElementsByTagName("service")[0]
                    				port_name = service.getAttribute("name")
                    				product_descr = service.getAttribute("product")
                    				product_ver = service.getAttribute("version")
                    				product_extra = service.getAttribute("extrainfo")
                			except:
                    				service = ""
                    				port_name = ""
                    				product_descr = ""
                    				product_ver = ""
                    				product_extra = ""


					port_service_ret = port_number + ":" + state + ":" + protocol + ":" + port_name + ":" + product_descr + ":" + product_ver + ":" + product_extra
					self.port_service_list.append(port_service_ret)
				
				self.port_service[ip] = self.port_service_list
				self.port_service_list = []			

			elif opt == 3:
				for hostscript in host.getElementsByTagName("hostscript"):
				 	for script in hostscript.getElementsByTagName("script"):
						script_id = script.getAttribute("id")
						script_output = script.getAttribute("output")
						
						script_ret_1 = script_id + ":" + script_output	
						self.script_list.append(script_ret_1)      				
				
				ports = host.getElementsByTagName("ports")[0].getElementsByTagName("port")	
				for port in ports:
					for script in port.getElementsByTagName("script"):
						script_id = script.getAttribute("id")
						script_output = script.getAttribute("output")
	
						script_ret_2 = script_id + ":" + script_output
						self.script_list.append(script_ret_2)		
				
				self.script[ip] =  self.script_list
				self.script_list = []	
																
		self.os["os"] = self.os_list
		self.mac["mac"] = self.mac_list
		self.script_ret["script"] = self.script
		self.port_service_ret["port_service"] = self.port_service

		return self.mac, self.os, self.port_service_ret, self.script_ret
		

##
### Main ...
##


if __name__ == "__main__":
	
	xml_parser = XmlParser(sys.argv[1])
	for key in xml_parser.parser(3).keys():
		print xml_parser.parser(3)[key]	

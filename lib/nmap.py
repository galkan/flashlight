
__VERSION__ = '0.1'
__AUTHOR__ = 'Galkan'
__DATE__ = '06.08.2014'


try:
	import re
	import os		
	import sys	
	import shutil	
	import datetime
	import tempfile
	import subprocess
	from xml_parser import XmlParser	
	from lib.core.threadpool import Worker,ThreadPool			
except ImportError,e:
        import sys
        sys.stdout.write("%s\n" %e)
        sys.exit(1)



class Nmap:
	

        def __init__(self, nmap_path, output_dir, thread_number):
	
		self.output_dir = output_dir + "/nmap/"
		self.thread_number = thread_number
		self.nmap = nmap_path
                self.open_port = re.compile("Host:\s([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s\(\)\s+Ports:\s+(.*)")
		self.host_up = re.compile("Host:\s([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s+\(\)\s+Status:\sUp")	

		if not os.path.isdir(self.output_dir):
			try:
				os.makedirs(self.output_dir)
			except Exception, err:
				print >> sys.sdterr, err
				sys.exit(1)


	def ping_scan(self, ip):

		""" Ping Scan """

		tmp = tempfile.NamedTemporaryFile(mode='w+t')
		tmp_file = tmp.name

		result = tempfile.NamedTemporaryFile(mode='w+t')
             	
		nmap_scan_option = "-n -sP %s -oG %s"% (ip, tmp_file)
                run_nmap = "%s %s"% (self.nmap, nmap_scan_option)
		
                proc = subprocess.Popen([run_nmap], shell=True, stdout = subprocess.PIPE,)
                stdout_value = str(proc.communicate())

		now = datetime.datetime.now()
		output_file = self.output_dir + "fener-" + "PingScan-" + now.strftime("%Y%m%d%H%M") 

		if not output_file[0] == "/":
			output_file = os.getcwd() + "/" + output_file

	        tmp.seek(0)
		try:		
			shutil.copy(tmp.name, output_file)
		except Exception, err:
			pass

                for line in tmp:
                        if re.search(self.host_up, line):
                                host = re.search(self.host_up, line).group(1)
				result.write(host + "\n")		

		tmp.close()

		result.seek(0)
		result_file_name = output_file + "_result"

		try:		
			shutil.copy(result.name, result_file_name)
		except Exception, err:
			pass

		return result
		

	def port_service_scan(self, ip_file, port_list):	

		""" Port Service Scan """

		now = datetime.datetime.now()
		output_file = self.output_dir + "fener-" + "PortService-Scan-" + now.strftime("%Y%m%d%H%M") 

		if not output_file[0] == "/":
			output_file = os.getcwd() + "/" + output_file
		
		ip_file.seek(0)	
		ip_file_name = ip_file.name

		nmap_scan_option = "-n -Pn -T4 -sV %s --open --host-timeout=10m --max-rtt-timeout=600ms --initial-rtt-timeout=300ms --min-rtt-timeout=300ms --max-retries=2 --min-rate=150 -iL %s -oA %s"% (port_list, ip_file_name, output_file)

                run_nmap = "%s %s"% (self.nmap, nmap_scan_option)
	
                proc = subprocess.Popen([run_nmap], shell=True, stdout=subprocess.PIPE,)
                stdout_value = str(proc.communicate())

		nmap_result_file = output_file + ".xml"
		

	
	def os_scan(self, ip_file):

		""" Operating System Scan """

		now = datetime.datetime.now()
		output_file = self.output_dir + "fener-" + "Os-Scan-" + now.strftime("%Y%m%d%H%M") 

		if not output_file[0] == "/":
			output_file = os.getcwd() + "/" + output_file
		
		ip_file.seek(0)	
		ip_file_name = ip_file.name

		nmap_scan_option = "-n -Pn -T4 -O -iL %s -oA %s 2>/dev/null"% (ip_file_name, output_file)
				
		run_nmap = "%s %s"% (self.nmap, nmap_scan_option)
		
		proc = subprocess.Popen([run_nmap], shell=True, stdout=subprocess.PIPE,)
                stdout_value = str(proc.communicate())
		
		nmap_result_file = output_file + ".xml"
		

	def script_scan(self, ip_file, script, ports):	

		""" Service Scan """

		now = datetime.datetime.now()
		output_file = self.output_dir + "fener-" + "Script-Scan-" + now.strftime("%Y%m%d%H%M") 
		
		if not output_file[0] == "/":
			output_file = os.getcwd() + "/" + output_file

		ip_file.seek(0)	
		ip_file_name = ip_file.name

		nmap_scan_option = "-n -Pn --script=default,%s %s --host-timeout=10m --max-rtt-timeout=600ms --initial-rtt-timeout=300ms --min-rtt-timeout=300ms --max-retries=2 --min-rate=150 -iL %s -oA %s"% (script, ports, ip_file_name, output_file)
				
		run_nmap = "%s %s"% (self.nmap, nmap_scan_option)

		proc = subprocess.Popen([run_nmap], shell=True, stdout=subprocess.PIPE,)
                stdout_value = str(proc.communicate())

		nmap_result_file = output_file + ".xml"	
		


try:
	import os
	import re
	import sys
	import time
	import socket
	import struct
	import signal
	import tempfile
	import datetime
	import argparse
	import subprocess
	from threading import Thread	
	from lib.osscan import OsScan
	from lib.core.core import Core
	from lib.pingscan import PingScan
	from lib.portscan import PortScan
	from lib.scriptscan import ScriptScan
	from lib.core.config_parser import ConfigParser	
	from lib.core.threadpool import Worker,ThreadPool				
	from lib.core.exceptions import FlashLightExceptions	
except ImportError, err:
        import sys
        sys.stdout.write("%s\n" %err)
        sys.exit(1)


class Main(object):
		
	def __init__(self):
		
		self.services = { "active":self.active_scan, "passive":self.passive_scan, "screen":self.take_screenshot, "filter":self.filter }	

                usage = "Usage: use --help for further information"
		description = "Flashligth: Light your ways through Pentest"
                parser = argparse.ArgumentParser(description = description, usage = usage)

		parser.add_argument('-p', '--project', dest = 'project', action = 'store', help = 'Project Name', required = True)
                parser.add_argument('-s', '--scan_type', dest = 'scan_type', help = 'Scan Type', choices = self.services.keys(), required = True)
		parser.add_argument('-d', '--destination', dest = 'destination', action = 'store', help = 'Target Ip/Host Name')		
		parser.add_argument('-c', '--config', dest = 'config_file', action = 'store', help = 'Configuration File', metavar = 'FILE', default='config/flashlight.yaml')
		parser.add_argument('-i', '--interface', dest = 'interface', action = 'store', help = 'Interface')
		parser.add_argument('-f', '--pcap_file', dest = 'pcap', action = 'store', help = 'Pcap File for Filtering')
		parser.add_argument('-r', '--rasterize', dest = 'rasterize', action = 'store', default = "/usr/local/bin/rasterize.js" , help = "Rasterize Js File For ScreenShot")
		parser.add_argument('-t', '--thread', dest = 'thread', action = 'store', help = 'Thread Number', default = 10, type = int)
		parser.add_argument('-o', '--output', dest = 'output', action = 'store', help = 'Output Directory', default = None)
		parser.add_argument('-a', '--alive', dest = 'alive', action = 'store_true', help = 'Ping Scan to Investigate Which Ip Address Are Up Before Scanning', default = None)
		parser.add_argument('-l', '--log', dest = 'log_file', action = 'store', help = 'Log File', metavar = 'FILE', default = "flashligth.log")
		parser.add_argument('-k', '--passive_timeout', dest = 'passive_timeout', action = 'store', help = 'Passive Scan Timeout Value', default = 15, type = int)
		parser.add_argument('-m', '--mim', dest = 'mim', action = 'store_true', help = 'Capture the Traffic When Performing Man in The Middle', default = None)
		parser.add_argument('-n', '--nmap-optimize', dest = 'nmap_optimize', action = 'store_true', help = 'Use Some Sxtra Nmap Options To Optimize Scanning For Performance Tuning', default = None)
		parser.add_argument('-v', '--verbose', dest = 'verbose', action = 'store_true', help = 'Verbose Output', default = None)
		parser.add_argument('-V', '--version', action='version', version='%(prog)s 1.0')
		
		self.args = parser.parse_args()

		command_list = { "active" : {self.args.destination : "-d/--destination"} , "passive" : {self.args.interface : "-i/--interface"}, "screen" : {self.args.destination : "-d/--destination"}, "filter" : {self.args.pcap : "-f/--pcap_file"} }

                for key, value in command_list[self.args.scan_type].iteritems():
                        if key is None:
                                parser.error("{0} argument is required".format(value))

		if self.args.output is None:
			self.output_dir = "output/{0}".format(self.args.project)
		else:
			self.output_dir = "{0}output/{1}".format(self.args.output, self.args.project)

		try:
			os.makedirs(self.output_dir)
		except:
			pass



	def is_file_exists(self, file_name):

		""" Check file whether exists or not """

		if not os.path.exists(Core.commands_path[file_name]):
                        Core.print_error("{0} Doesn't Exists on The System !!!".format(Core.commands_path[file_name]))


	def active_scan(self):

		""" Run Nmap In Order To Do Port Scan Through Active Scan """
		
		self.is_file_exists("nmap")

		ip_file_to_scan = tempfile.NamedTemporaryFile(mode='w+t')
		if self.args.alive:
			ping_scan = PingScan(self.args.destination, self.output_dir, self.args.nmap_optimize, "PingScan")
			ping_scan.run(ip_file_to_scan)
		else:
			ip_file_to_scan.write("\n".join([ip.strip() for ip in self.args.destination.split(",")]))

		port_scan = PortScan(self.args.config_file, self.output_dir, ip_file_to_scan, self.args.nmap_optimize, "PortScan")
		os_scan = OsScan(self.output_dir, ip_file_to_scan, self.args.nmap_optimize, "OsScan")
		script_scan = ScriptScan(self.args.config_file, self.output_dir, ip_file_to_scan, self.args.nmap_optimize, "ScriptScan")
	
		thread_list = []
		try:
			for counter, func in enumerate(( port_scan, os_scan, script_scan)):
				thread_number = "t_{0}".format(counter)
				thread_number = Thread(target = func.run, args = ())
				thread_number.start()
				thread_list.append(thread_number)

			for t in thread_list:
				t.join()
		except Exception, err:
			Core.print_error(str(err))


	def run_phantomjs(self, cmd_opt):

		""" Run Phantomjs """

		proc = subprocess.Popen([cmd_opt], shell=True, stdout=subprocess.PIPE,)
                stdout_value = str(proc.communicate())



	def take_screenshot(self):
		
		""" Take ScreenShot Using PhantomJS"""
		
		for rasterize_file in self.phantomjs_path, self.args.rasterize, self.nmap_path:
			if not os.path.exists(rasterize_file):
				print >> sys.stderr, "%s Doesn't Exists On The System !!!"% rasterize_file
				sys.exit(1)
			
		screen_output_dir = "{0}/screen/".format(self.output_dir)
		try:
			os.makedirs(screen_output_dir)
		except:
			pass

		now = datetime.datetime.now()
		screen_time = now.strftime("%Y%m%d%H%M") 
		
		if screen_output_dir[0] != "/":
			screen_output_dir = "{0}/{1}".format(os.getcwd(), screen_output_dir)

		http_reg = re.compile("80/open/tcp//")
        	https_reg = re.compile("443/open/tcp//")
   
		url_list = []	
		http_list = []
		https_list = []

		tmp = tempfile.NamedTemporaryFile(mode='w+t')
		tmp_file = tmp.name

		#nmap_scan_option = "-n -Pn -T4 -sT -p 80,443 --open --host-timeout=10m --max-rtt-timeout=600ms --initial-rtt-timeout=300ms --min-rtt-timeout=300ms --max-retries=2 --min-rate=150 %s -oG %s"% (self.args.target, tmp_file)
		#run_nmap = "%s %s"% (self.nmap_path, nmap_scan_option)
		
		proc = subprocess.Popen(["-n", "-Pn", "-T4", "-sT", "-p", "80,443" "--open", "--host-timeout=10m", "--max-rtt-timeout=600ms", "--initial-rtt-timeout=300ms", "--min-rtt-timeout=300ms", "--max-retries=2", "--min-rate=150", self.args.target, "-oG", tmp_file ], shell=False, stdout=subprocess.PIPE,)
                stdout_value = str(proc.communicate())
		
		for line in tmp:
			if re.search(http_reg, line):
				ip = line.split()[1]				
				http_list.append(ip)

			if re.search(https_reg, line):
				ip = line.split()[1]				
				https_list.append(ip)

		for host in http_list:
			url = "http://%s"% (host)
			url_list.append(url)

		for host in https_list:
			url = "https://%s"% (host)
			url_list.append(url)
			
		tmp.close()

		pool = ThreadPool(self.args.thread)
		for url in url_list:
			output_file = screen_output_dir + url.split(":")[0] + "-" + url.split("/")[2] + "_" + screen_time + ".png"	
			phantomjs_cmd = "%s --ignore-ssl-errors=yes %s %s %s"% (self.phantomjs_path, self.args.rasterize, url, output_file)		
			print phantomjs_cmd
			pool.add_task(self.run_phantomjs, phantomjs_cmd)			

		pool.wait_completion()
	


	def get_default_gw(self):

		try:
			with open("/proc/net/route") as fh:
        			for line in fh:
            				fields = line.strip().split()
					if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                				continue

            				return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
		except:
			return None



	def passive_scan(self):

		""" Run tcpdump to sniff network traffic """

		if self.args.verbose:	
			print "Passive Scan ..."

		if not os.path.exists(self.tcpdump_path):
                        print >> sys.stderr, "%s Doesn't Exists on the System !!!"% self.tcpdump_path
                        sys.exit(1)
		
		pcap_output_dir = "{0}/pcap/".format(self.output_dir)

		try:
			os.makedirs(pcap_output_dir)
		except:
			pass

		now = datetime.datetime.now()
		pcap_time = now.strftime("%Y%m%d%H%M") 
		
		if pcap_output_dir[0] != "/":
			pcap_output_dir = "{0}/{1}".format(os.getcwd(), pcap_output_dir)
	
		output_file = "{0}{1}.pcap".format(pcap_output_dir, pcap_time)

		if self.args.mim:
			if not os.path.exists(self.arpspoof_path):
                        	print >> sys.stderr, "%s Doesn't Exists on the System !!!"% self.arpspoof_path
                        	sys.exit(1)

			with open('/proc/sys/net/ipv4/ip_forward', 'w') as ipf:
        			ipf.write('1\n')

			default_gw = self.get_default_gw() 
			if default_gw:
				arpspoof_proc = subprocess.Popen([self.arpspoof_path, "-i", self.args.interface, default_gw], shell = False, stdout = subprocess.PIPE,)
	
		proc = subprocess.Popen([self.tcpdump_path, "-tttnn", "-i", self.args.interface, "-s", "0", "-w", output_file] , shell = False, stderr = subprocess.PIPE,)
	
		counter = 0
		time_wait = 2
		progress = 100/(self.args.passive_timeout/time_wait)	

		start_time = time.time()
		while ( (time.time() - start_time) <  self.args.passive_timeout ):			
			sys.stdout.write('\r')
			
			if ( progress < (100 - (progress*counter))):
    				sys.stdout.write("[%-20s] %d%%" % ('='*(counter*progress), progress*counter))
			else:
				sys.stdout.write("[%-20s] %d%%" % ('='*(counter*progress), 100))    			
				sys.stdout.write('\n\n')			
			
			sys.stdout.flush()
			counter = counter + 1
	
			time.sleep(time_wait)
    	
		proc.kill()
		
		if self.args.mim and default_gw:			
			arpspoof_proc.kill()


	
	def filter(self):
		
		""" Filter Pcap File using Tshark """

		output_dir = "{0}/".format(self.args.project)

		#for subdir, dirs, files in os.walk(pcap_dir):
		#	print subdir, dirs, files
	


	def run(self, scan_type):
	
		""" Run flashligth """

		if os.geteuid() != 0:
			print >> sys.stderr, "Run as Root\n"
			sys.exit(1)

		signal.signal(signal.SIGINT, self.signal_handler)
		
		self.services[scan_type]()



	def signal_handler(self, signal, frame):

		""" Set Signal """

		print('Bye ...')
         	sys.exit(37)	


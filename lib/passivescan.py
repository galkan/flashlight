
try:
	import sys
	import time
	import subprocess
	from lib.core.core import Core
	from lib.passive.passive import Passive
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class PassiveScan(Passive):

	def __init__(self, args, output_dir):

		Passive.__init__(self, output_dir)	

		self.__args = args
		self.__output_dir  = output_dir
                self.__proc_ip_forward = "/proc/sys/net/ipv4/ip_forward"


        def __show_progress(self):
        
                counter = 0
                time_wait = 2
                progress = 100/(self.__args.passive_timeout/time_wait)
                
                start_time = time.time()
                while ( (time.time() - start_time) <  self.__args.passive_timeout ):
                        sys.stdout.write('\r')
                        
                        if ( progress < (100 - (progress*counter))):
                                sys.stdout.write("[%-20s] %d%%" % ('='*(counter*progress), progress*counter))
                        else:   
                                sys.stdout.write("[%-20s] %d%%" % ('='*(counter*progress), 100))
                                sys.stdout.write('\n\n')
                                
                        sys.stdout.flush()
                        counter = counter + 1
                        
                        time.sleep(time_wait)
                        

	def __run_tcpdump(self):
        
                tcpdump_proc = subprocess.Popen([Core.commands_path["tcpdump"], "-tttnn", "-i", self.__args.interface, "-s", "0", "-w", self._output_file] , shell = False, stdout = subprocess.PIPE, stderr = subprocess.PIPE, )
                self.__show_progress()
                tcpdump_proc.kill()


        def __enable_forwarding(self):
        
                with open(self.__proc_ip_forward, 'w') as ip_forward:
                        ip_forward.write('1\n')


	def _run(self):
	
		arpspoof_proc = None
                if self.__args.mim:
			self.__enable_forwarding()
			
			if self._default_gw:
				print "ARPSPOOF"
				arpspoof_proc = subprocess.Popen([Core.commands_path["arpspoof"], "-i", self.__args.interface, self._default_gw], shell = False, stdout = subprocess.PIPE,)

		self.__run_tcpdump()
		if arpspoof_proc:
			arpspoof_proc.kill()
		

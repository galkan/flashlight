
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

	def __init__(self, args):

		self.__args = args
		Passive.__init__(self, self.__args)	

                self.__proc_ip_forward = "/proc/sys/net/ipv4/ip_forward"
		self.__cmd = "{0} -tttnn -i {1} -s 0 -w {2}".format(Core._commands_path["tcpdump"], self.__args.interface, self._output_file)       


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
 
                tcpdump_proc = subprocess.Popen([self.__cmd] , shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, )
                self.__show_progress()
                tcpdump_proc.kill()


        def __enable_forwarding(self):
        
                with open(self.__proc_ip_forward, 'w') as ip_forward:
                        ip_forward.write('1\n')


	def _run(self, logger):
	
		arpspoof_proc = None

                if self.__args.mim:
			logger._logging("Ip Forwarding Enabled")
			self.__enable_forwarding()

			if self._default_gw:
				logger._logging("Getting Default Gw {0}".format(self._default_gw))
				logger._logging("START: Arpspoofing")
				arpspoof_proc = subprocess.Popen([Core._commands_path["arpspoof"], "-i", self.__args.interface, self._default_gw], shell = False, stdout = subprocess.PIPE,)

		logger._logging("START: Tcpdump")
		self.__run_tcpdump()
		logger._logging("STOP: Tcpdump")

		if arpspoof_proc:
			logger._logging("STOP: Arpspoof")
			arpspoof_proc.kill()
		logger._logging("Finished Passive Scan. Results saved in {0} folder".format(self._output_dir))

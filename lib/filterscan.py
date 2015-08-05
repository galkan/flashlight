
try:
	import subprocess
	from lib.core.core import Core
	from lib.filter.filter import Filter
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class FilterScan(Filter):

	def __init__(self, args):
		
		Filter.__init__(self, [args.pcap], args, "filter")
		print self._output_dir


	def __run_cmd(self, cmd, file_name, result_set):
		
		output_file = "{0}{1}.txt".format(self._output_dir, file_name)
		result_file = open(output_file, "w")

		proc = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
		if isinstance(result_set, (list, tuple)):
			for line in iter(proc.stdout.readline, ''):
				if line not in result_set:
					result_set.append(line)
		else:
			for line in iter(proc.stdout.readline, ''):
				try:
				 	result_set[line.rstrip()] += 1
				except:
					result_set[line.rstrip()] = 1	
		
		if isinstance(result_set, (list, tuple)):
			if len(result_set) > 10:
				result_file.write("".join(result_set[1:10]))
			else:
				result_file.write("".join(result_set))
		else:
			for counter, value in enumerate(sorted(result_set, key=result_set.get, reverse=True)):
				if counter == 10:
					break
				else:
  					print result_set[value], value
				


	def _run(self, logger):
		
		for file_name, tshark_cmd in self._filter_commands.iteritems():
			result_set = None	

			if file_name.startswith("top10"):
				result_set = {}
			else:
				result_set = []
			
			self.__run_cmd(tshark_cmd,file_name, result_set)

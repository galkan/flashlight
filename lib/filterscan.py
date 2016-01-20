try:
	import os
	import subprocess
	import shlex
	from lib.core.core import Core
	from lib.filter.filter import Filter
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class FilterScan(Filter):

        def __init__(self, args):

                self.__args = args
                Filter.__init__(self, self.__args, "filter")


        def __run_cmd(self, cmd, file_name, result_set, logger):

                output_file = "{0}{1}_{2}.txt".format(self._output_dir, file_name, os.path.basename(self.__args.pcap))
                result_file = open(output_file, "w")

                logger._logging("Filter: {0} parsing".format(file_name))
                logger._logging("CMD - Filter: {0}".format(cmd))

                cmd_list = shlex.split(cmd)
                proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
                if isinstance(result_set, (list, tuple)):
                        [ result_set.append(line) for line in iter(proc.stdout.readline, '') if line not in result_set ]
                else:
                        for line in iter(proc.stdout.readline, ''):
                                try:
                                        result_set[line.rstrip()] += 1
                                except:
                                        result_set[line.rstrip()] = 1   

                if isinstance(result_set, (list, tuple)):
                        result_file.write("".join(result_set[1:10])) if len(result_set) > 10 else result_file.write("".join(result_set))
                else:
                        for counter, value in enumerate(sorted(result_set, key=result_set.get, reverse=True)):
                                if counter == 10:
                                        break
                                else:
                                        result_file.write("{0} {1}\n".format(result_set[value], value))


        def _run(self, logger):

                logger._logging("START: Filter pcap file")

                for file_name, tshark_cmd in self._filter_commands.iteritems():
                        result_set = {} if file_name.startswith("top10") else []
                        self.__run_cmd(tshark_cmd, file_name, result_set, logger)

                logger._logging("Finished Filtering. Results saved in {0} folder".format(self._output_dir))

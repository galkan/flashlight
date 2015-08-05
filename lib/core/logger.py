
import logging

class Logger(object):

	def __init__(self, logfile, verbose = False):

		logFormatter = logging.Formatter("FLASHLIGHT : %(asctime)s :  %(message)s", "%Y-%m-%d %H:%M:%S")
		self.__rootLogger = logging.getLogger()
		self.__rootLogger.setLevel(logging.DEBUG)

		fileHandler = logging.FileHandler(logfile)
		fileHandler.setFormatter(logFormatter)
		self.__rootLogger.addHandler(fileHandler)

		if verbose:
			consoleHandler = logging.StreamHandler()
			consoleHandler.setFormatter(logFormatter)
			self.__rootLogger.addHandler(consoleHandler)
		

	def _logging(self, message):

		self.__rootLogger.debug(message)		

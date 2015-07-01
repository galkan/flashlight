#!/usr/bin/env python

__VERSION__ = '0.1'
__AUTHOR__ = 'Galkan'
__DATE__ = '16.07.2014'


try:
	from lib.main import Main
except ImportError,e:
        import sys
        sys.stdout.write("%s\n" %e)
        sys.exit(1)

##
### Main, go Galkan go go go ...
##

if __name__ == "__main__":

	fener = Main()
	fener.run(fener.args.scan_type)


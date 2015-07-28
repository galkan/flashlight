#!/usr/bin/env python

try:
	from lib.main import Main
except ImportError, err:
        import sys
        sys.stdout.write("%s\n" %err)
        sys.exit(1)

##
### Main, go Galkan go go go ...
##

if __name__ == "__main__":

	flashlight = Main()
	flashlight.run(flashlight.args.scan_type)


import time
import sys

for i in range(20):
	print (str(i), end = '' )
	sys.stdout.flush()
	time.sleep(1)
	print ('\r')



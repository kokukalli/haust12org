import sys
import time

for i in reversed(range(0,20)):
	time.sleep(0.1)
	if(i == 19):
		print(str(i), end='', file=sys.stdout)
	else:
		print("\r0:{width}".format(str(i), width = w, fill = ' ', align = 'right'), end='', file=sys.stdout)
	sys.stdout.flush()
	w = len(str(i))

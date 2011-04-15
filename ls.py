import os

def ls_func(directory, depth):
	f = os.popen("ls -p " + directory)
	for i in f.readlines():
		j = i[0:-1]
		if j.endswith("/"):
			for i in range(0,depth):
				print " ",
			print j
			ls_func(directory + j, depth + 1)

def find_func():
	f = os.popen("find *.m")
	for i in f.readlines():
		print i

find_func()

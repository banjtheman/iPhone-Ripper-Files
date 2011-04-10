import os
import os.path
import shutil
from sys import argv
import fileinput

# copies the specified file into the ThreeViewNav folder
def copy_file(name):
  	shutil.copyfile('~/Documents/python/ThreeViewNav/' + name, name)
	return


argc = len(argv)

# terminates if used incorrectly
if (argc != 2):
	print 'usage: ocscript.py [filename]'
	exit()

# copy the .h and .m files into the project folder
copy_file('UIView+FullDescription.h')
copy_file('UIView+FullDescription

# follwing code adds in "popozow" whenever it finds "yoyoyo" in
# the file specified by argv[1]
flag = False

new_file_name = 'copy_'+argv[1]

new_file = open(new_file_name, 'w');

for line in fileinput.input():
	if flag:
		new_file.write('popozow\n')
		flag = False
	if line.startswith('yoyoyo'):
		flag = True
	new_file.write(line)
	
new_file.close()

# need to add #include "UIView+FullDescription.h" into every .m file we edit

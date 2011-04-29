#!/usr/bin/python

from sys import argv
import os
import fileinput
import re

# This script will prepare an Xcode project file for use with iPhone GUITAR.
# It does the following:
# 	1. Creates a copy of the specified folder, leaving everything in the original untouched.
#	2. Creates a Structures/ directory in this new folder
#	3. Adds in 8 required .h and .m files to the Classes/ folder
#	4. Edits the [Project Name]AppDelegate.m file to include some new lines
#
# The script assumes to find the 8 required .m and .h files in the current directory.
#
# Overwrites any folder in the same directory with the name [Project Name]_test



# edits the file, adding the 4 lines we need in the correct places.
def edit_app_delegate(filename):
	print "editing file..."

	# this function will create a new temporary file and copy all of the text
	# from the original. As it does this, it will insert the new lines where needed.
	# the original will then be deleted, and the copy file renamed.

	# create the new file
	new_file_name = filename + "_copy"
	new_file = open(new_file_name, "w");
	
	# flag to be used in the upcoming loop
	flag = False

	# write the first line we need, the new import statement
	new_file.write("#import \"ScriptRunner.h\"\n")

	# this is the loop that will search for the correct place to add
	# the other three lines. It will also go on after that and copy the remaining lines
	# unchanged into the new file.
	for line in fileinput.input(filename):
		# if we are in the correct function
		if flag:
			# just before the return statement, we will add the three
			# new lines
			if line.find("return") >= 0:
				new_file.write("[[[ScriptRunner alloc] init] autorelease];\n")

				# write the return statement
				new_file.write(line)

				# flip the flag back
				flag = False
			
			else:
				new_file.write(line)
		# if we find the function to add the lines to, trip the flag
		elif line.find("didFinishLaunchingWithOptions") >= 0:
			new_file.write(line)
			flag = True
		# otherwise just write the line
		else:
			new_file.write(line)
	
	# close the file
	new_file.close()
	
	# remove the original file
	os.popen("rm " + filename)
	
	# rename the new file
	os.popen("mv " + new_file_name + " " + filename)


# here the main function starts
start_dir=os.getcwd()

print start_dir

argc = len(argv)

# terminates if used incorrectly
if (argc != 2):
	print "usage: testscript.py [name of your project folder]"
	exit()

# check to see if the name passed in had a / at the end
if argv[1][-1] == "/":
	argv[1] = argv[1][0:-1]

app_name=re.split('[/*]',argv[1])
print app_name[-1]


# name of the new directory
new_directory = argv[1] + "_test"

# the name of the project directory, without the path
project_name = new_directory[new_directory.rfind("/") + 1:len(new_directory)]

# runs a find on the new directory name
f = os.popen("ls -p " + new_directory[0:new_directory.rfind("/")])
for i in f.readlines():
	# deletes the folder if it is found
	if i == project_name + "/\n":
		os.popen("rm -r " + new_directory)
		break


print "creating new project directory..."

#create the new directory
os.popen("cp -r " + argv[1] + " " + new_directory)

# making the structures folder
print "creating Structures folder..."
os.popen("mkdir " + new_directory + "/Structures")

print "copying required files to Classes folder..."

# now we need to copy all the necessary files from the current directory 
# to this new directory
os.popen("cp XPathQuery.h " + new_directory + "/Classes")
os.popen("cp XPathQuery.m " + new_directory + "/Classes")
os.popen("cp ScriptRunner.h " + new_directory + "/Classes")
os.popen("cp ScriptRunner.m " + new_directory + "/Classes")
os.popen("cp TouchSynthesis.h " + new_directory + "/Classes")
os.popen("cp TouchSynthesis.m " + new_directory + "/Classes")
os.popen("cp UIView+FullDescription.h " + new_directory + "/Classes")
os.popen("cp UIView+FullDescription.m " + new_directory + "/Classes")

print "finding AppDelegate.m ..."

# run a find on the AppDelegate.m file
f = os.popen("find " + new_directory + "/Classes/*AppDelegate.m")
for i in f.readlines():
	edit_app_delegate(i[0:-1])

print "done editing AppDelegate file"



print "Adding required files to xcode project"

print new_directory

dir2=new_directory+"/Classes"

print dir2
#doing the thor adding files to xcode project
os.chdir(new_directory)
os.system("ls")
os.system("thor xcs:add Classes/ScriptRunner.h Classes")
os.system("thor xcs:add Classes/ScriptRunner.m Classes")
os.system("thor xcs:add Classes/TouchSynthesis.h Classes")
os.system("thor xcs:add Classes/TouchSynthesis.m Classes")
os.system("thor xcs:add Classes/UIView+FullDescription.h Classes")
os.system("thor xcs:add Classes/UIView+FullDescription.m Classes")
os.system("thor xcs:add Classes/XPathQuery.h Classes")
os.system("thor xcs:add Classes/XPathQuery.m Classes")


print "getting library"
os.popen("cp /usr/lib/libxml2.dylib "+new_directory+ "/Classes")

#need user to manually link files
print "Time to open xcocde and drag the lib to the classes folder"

#press enter if libincluded
raw_input("Press enter when done")

os.system("xcodebuild -configuration Debug -target "+app_name[-1]+" -sdk iphonesimulator4.2 HEADER_SEARCH_PATHS=$SDKROOT/usr/include/libxml2")

os.chdir(start_dir)
os.system("ls")

os.system("../iphonesim/build/Release/iphonesim launch "+new_directory+"/build/Debug-iphonesimulator/"+app_name[-1]+".app")




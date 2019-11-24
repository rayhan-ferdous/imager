#!/usr/bin/env python
import os, os.path
thumb = ""

def logo():
	print "\t\t********************"
	print "\t\t****** imager ******"
	print "\t\t********************"
	print

def clear():
	os.system("clear")

def wait_for_enter():
	key = raw_input()

def show_partition():
	print "partition mapping...\n"
	os.system("sudo lsblk")
	print("============================================")

def entry():
	global thumb
	thumb = raw_input("USB device thumb ? (e.g. sdc, NOT sdc1) ")
	print thumb, " selected for operation ..."	

def make():
	global thumb
	cmd = "sudo dd if=os.iso of=/dev/" + str(thumb) + " bs=1M"
	print "Is the thumb entry correct (y/n)? "
	key = raw_input()

	if key == "y":
		os.system(cmd)
		#print cmd
	else:
		pass

###########################################################
clear()
logo()

print "copy your .iso image & imager.py both into the home directory if not already and run again. rename the disk image to 'os.iso'. then mount the USB device..."
print "press enter when done... [ENTER]"

wait_for_enter()
clear()
logo()

show_partition()
entry()

make()







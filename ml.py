# Micro Log
# 1.0
# A simple terminal work/time log focused on speed, usability and flexibility.
# Developed by: Edvard Busck-Nielsen 11.07.2018
# GNU GPL v. 3.0

import os
import os.path
import datetime

def open_log():
	#open
	today = input("Date for entry (format: year-day-month):")
	filename = today+'.txt'
	if os.path.isfile(filename):
		open_cmd = "nano "+filename
		os.system(open_cmd)
		show_out_cmd = "cat "+filename
		print ("\033[2m")
		os.system(show_out_cmd)
		print("\033[0m")
		print("*** DONE ***")
		tmp = input()
		main()
	else:
		with open(filename,"w+") as f:
				f.write(today)
		open_cmd = "nano "+filename
		os.system(open_cmd)
		show_out_cmd = "cat "+filename
		print ("\033[2m")
		os.system(show_out_cmd)
		print("\033[0m")
		print("*** DONE ***")
		tmp = input()
		main()

def today():
	#today
	today = datetime.datetime.now()
	today = str(today.year)+'-'+str(today.day)+'-'+str(today.month)
	if os.path.isfile(filename):
		open_cmd = "nano "+filename
		os.system(open_cmd)
		show_out_cmd = "cat "+filename
		print ("\033[2m")
		os.system(show_out_cmd)
		print("\033[0m")
		print("*** DONE ***")
		tmp = input()
		main()
	else:
		with open(filename,"w+") as f:
				f.write(today)
		open_cmd = "nano "+filename
		os.system(open_cmd)
		show_out_cmd = "cat "+filename
		print ("\033[2m")
		os.system(show_out_cmd)
		print("\033[0m")
		print("*** DONE ***")
		tmp = input()
		main()

def new():
	os.system('clear')
	title = "figlet -f mini New Entry"
	os.system(title)
	print ("\n")
	print ("\033[2m'x' to go back, ' ' to create a new one or 't' to start editing todays entry.\033[0m")
	action = input("-$: ")
	if action == "x" or action == "X":
		main()
	elif action == 't' or action == "T":
		#today
		today = datetime.datetime.now()
		today = str(today.year)+'-'+str(today.day)+'-'+str(today.month)
		filename = today+'.txt'
		if os.path.isfile(filename):
			open_cmd = "nano "+filename
			os.system(open_cmd)
			show_out_cmd = "cat "+filename
			print ("\033[2m")
			os.system(show_out_cmd)
			print("\033[0m")
			print("*** DONE ***")
			tmp = input()
			main()
		else:
			with open(filename,"w+") as f:
				f.write(today)
			open_cmd = "nano "+filename
			os.system(open_cmd)
			show_out_cmd = "cat "+filename
			print ("\033[2m")
			os.system(show_out_cmd)
			print("\033[0m")
			print("*** DONE ***")
			tmp = input()
			main()
	elif action == ' ':
		#new entry
		today = input("Date for entry (format: year-day-month):")
		filename = today+'.txt'
		if os.path.isfile(filename):
			open_cmd = "nano "+filename
			os.system(open_cmd)
			show_out_cmd = "cat "+filename
			print ("\033[2m")
			os.system(show_out_cmd)
			print("\033[0m")
			print("*** DONE ***")
			tmp = input()
			main()
		else:
			with open(filename,'w+') as f:
				f.write(today)
			open_cmd = "nano "+filename
			os.system(open_cmd)
			show_out_cmd = "cat "+filename
			print ("\033[2m")
			os.system(show_out_cmd)
			print("\033[0m")
			print("*** DONE ***")
			tmp = input()
			main()



def main():
	os.system('clear')
	title = "figlet M i c r o Log"
	os.system(title)
	print ("\n")
	print ("\033[2m'o' to open a entry, 'n' to create a new one or 't' to start editing todays entry.\033[0m")

	action = input("-$: ")

	if action == "o" or action == "O":
		#open
		open_log()
	elif action == "n" or action == "N":
		#new
		new()
	elif action == "t" or action == "T":
		#today
		today()

	else:
		print("\033[2mMicroNote doesn't recognize the command "+action)
		tmp = input()
		main()
main()

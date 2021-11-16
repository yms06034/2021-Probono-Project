import pyfiglet
print("pyfiglet import finish")
import time
print("time import finish")
import STTProcess as Pcs
print("STTProcess import finish")
import LED
print("LED import finish")
import os
print("os import finish")

def loading():
	os.system('clear')
	print("Ok! Let's go")
	time.sleep(3)
	print("\033[95m" + pyfiglet.figlet_format("Hi! I'm\n") + "\033[0m")
	print("\033[95m" + pyfiglet.figlet_format("phishing ppashung") + "\033[0m")
	time.sleep(3)
	os.system('clear')
	print(pyfiglet.figlet_format("What happen?"))
	flag = input("here(If you want help, you can write 'help'): ")
	if(flag == 'help'):
		print("If you want check voiceFile is voicephishing or is not voicepthishng you can write a number of file, and then write file path")
		print("If you want finish. you can write 'finish'")
		time.sleep(10)
		return 'h'
	elif(flag == 'finish'):
		return 'f'
	else:
		return flag
while(1):
	userIn = loading()
	if(userIn == 'h'): continue
	elif(userIn == 'f'):
		print("bye!")
		break
	num = int(userIn)
	if(num <= 0):
		print("error")
		break
	#elif(num == 3):
	#	textSet = Pcs.readFile(num)
	#	print("Listening...")
	#	time.sleep(30)
	#	print("ok")
	#	os.system('clear')
	#	signal = 0
	
	textSet = Pcs.readFile(num)
	print("Listening...")
	signal = Pcs.textPre(textSet)
	print("ok")
	os.system('clear')
	if(signal == 1):
		print("\033[31m" + pyfiglet.figlet_format("Warning!!!\n") + "\033[0m")
		led = LED.set(18)
		LED.ON(led)
		print("\033[41m" + pyfiglet.figlet_format("Warning!!!\n") + "\033[0m")
		LED.ON(led)
		print("\033[31m" + pyfiglet.figlet_format("Warning!!!\n") + "\033[0m")
		LED.ON(led)
		LED.finish()
	elif(signal == 0):
		print("\033[32m" + pyfiglet.figlet_format("It's okay") + "\033[0m")
		led = LED.set(17)
		LED.ON(led)
		print("\033[42m" + pyfiglet.figlet_format("It's okay") + "\033[0m")
		LED.ON(led)
		print("\033[32m" + pyfiglet.figlet_format("It's okay") + "\033[0m")
		LED.ON(led)
		LED.finish()
	time.sleep(10)

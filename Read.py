
#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import webbrowser
import subprocess
from guizero import App, Text, PushButton

reader = SimpleMFRC522()

def do_ok():
	app.destroy()
	subprocess.call("chromium-browser --no-sandbox https://drive.google.com/file/d/17HpiFLGdm9bHNpaX_8HXn1ktQDoxy1z-/view?usp=drivesdk", shell=True)
	#app.destroy()

def do_ok1():
        app.destroy()

def do_ok2():
        app.destroy()
        subprocess.call("chromium-browser --no-sandbox https://drive.google.com/file/d/17NH2PiW9RgloK_3mH33TAX9nGMHyZsRW/view", shell=True)

while True:
	try:
		id, text = reader.read()
		print(id)
		print(text)
		if(id==443620150705):
			#pygame.mixer.init()
			#pygame.mixer.music.load("Voice 001.m4a")
			#pygame.mixer.music.play()
			#while pygame.mixer.music.get_busy() == True:
   		 	#	continue
			app = App(title="Hello User", height=200, width=2000)
			benmes = Text(app, text="Bennett University", size=20, color='red')
			message = Text(app, text="You have reached the 2nd Floor. Take a Left and continue staight until the end of the corridor")
			button = PushButton(app, text="OK", command=do_ok1)
			app.display()
			#print("You have reached the 2nd Floor. Take a Left and continue staight until the end of the corridor")
                        #subprocess.call("chromium-browser --no-sandbox https://www.youtube.com", shell=True)
		elif(id == 720783888171):
		#if(id!=None):
			#print(id)
			#print(text)
			#webbrowser.open_new('https://www.youtube.com')
			app = App(title="Hello User", height=200, width=2000)
			benmes = Text(app, text="Bennett University", size=20, color='red')
			message = Text(app, text="On your left is the Mac Lab which Dr Vipul Mishra will now give you more information about, continue to your right later on")
			button = PushButton(app, text="OK", command=do_ok)
			app.display()
		elif(id==34028015263):
			app = App(title="Hello User", height=200, width=2000)
			benmes = Text(app, text="Bennett University", size=20, color='red')
			message = Text(app, text="On your right is the NVIDIA Lab open to senior students and regularly  used by PhD scholars to build on their imaginative Comp Sci ideas using the high spec computers available")
			button = PushButton(app, text="OK", command=do_ok2)
			app.display()
		elif(id==786294328611):
			app = App(title="Hello User", height=200, width=2000)
			benmes = Text(app, text="Bennett University", size=20, color='red')
			message = Text(app, text="Continue along the corridor to exit this small CSE Department section in the A-Block")
			button = PushButton(app, text="OK", command=do_ok1)
			app.display()
			#subprocess.call("chromium-browser --no-sandbox https://www.youtube.com", shell=True)
	finally:
		GPIO.cleanup()

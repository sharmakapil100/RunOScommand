import os
import pyttsx3 as tt
print("hello")
tt.speak("hello I am microsoft")
while True:
	tt.speak("enter your command")
	p = input()
	
	print(p)
	if ('hello' in p or 'hi' in p or 'hyy' in p) and ( 'i' in p or 'am' in p):
		tt.speak("hello I am here to help you ")
		tt.speak("please enter your command")
		
	elif ('run' in p or 'execute' in p or 'open' in p or 'text' in p) and ('editor' in p or 'notepad' in p):
		tt.speak("starting notepad")
		
		os.system("notepad")
		tt.speak("anything else you want to do")
	elif ('run' in p or 'execute' in p or 'open' in p) and ('firefox' in p or 'browser' in p):
		tt.speak("starting firefox")
		os.system("firefox")
		tt.speak("great!!, anything you want from me ")
	elif ('run' in p or 'execute' in p or 'open' in p) and ('song' in p or 'media' in p or 'player' in p):
		tt.speak("starting media player")
		os.system("wmplayer")
		
	elif ('run' in p or 'execute' in p or 'open' in p or 'play' in p) and ('song' in p or 'media' in p or 'player' in p):
		tt.speak("starting vlc mediaplayer")
		os.system("vlc")
		tt.speak("have you enjoy  your songs")
	if ('run' in p or 'want' in p) and ('paint' in p or 'painting' in p):
		tt.speak("wait for a second starting mspaint program for you")
		os.system("mspaint")
		tt.speak("how can i help you")
	else:
		tt.speak("have a nice day goodbye")
		#print("don't support")
		break;
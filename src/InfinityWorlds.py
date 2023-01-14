#!/usr/bin/env python3

#A free, and open source game that allows you to go through infinite possibilities, I present to you, 
#Infinity Worlds

#As always, free as well as open source!

import os
import time
import sys

#Used for the AI (Uses GPT-3))
import openai



#API KEY (IMPORTANT!):

openAiapikey = '' #Put your api key here




#Clearscreen function (Visual purposes):
def clearscreen():
	if(os.name == 'posix'):
		os.system('clear')
	else:
		os.system('cls')
		
def delay_print(s, t):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(t)
		
#Clear the screen on start
clearscreen()
delay_print("Welcome to the World of Infinite Possibilities...", .09)
time.sleep(2)
print("\n")
delay_print("What shall the next story be?", .09)
print("\n")


#Generate the text with the help of GPT-3.
def generate(text):
	openai.api_key = openAiapikey
	
	response = openai.Completion.create(
		model="text-davinci-003",
		prompt=text,
		temperature=0.7,
		max_tokens=256,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0
	)
	content = response.choices[0].text.split('.')
	return response.choices[0].text

#Main variables/lists:

#The MainMenu/MainACTIVITY of the game:

#Actual prompts (Not used now, may be used later if necessary)
#questions = "1) Adventure\n2) Survival\n3) Real\n4) I am...\n5) They are...\n6) He/She is..."
#Do the main loop here afterwards:
while True:
	#Clear the screen.
	time.sleep(1.5)
	clearscreen()
	questions = "\n\n1) Start\n2) Credits\n00) Exit"
	delay_print(questions, .05)
	MainMenu = int(input("\n>> "))

	if MainMenu == 1:
		clearscreen()
		#The contents:
		promptcontents = []
		#Print initial question:
		delay_print("\nWrite about who/what you want to be...\nExample: A knight, with super powers. Or, anything else you want.\n", .07)
		command = str(input(">> "))
		outputtext = generate("Write an adventurous two sentences about being" + command + " in second person point of view")
		delay_print(outputtext, .05)
		#Append what happened.
		promptcontents.append(outputtext + "\n")
		#While True, Continue the story:
		while True:
			promptcontentscurated = ' '.join(promptcontents)
			#What happens next in the story:
			whatnext = input("\nWhat happens next? >> ")
			if "QQT" in whatnext:
				delay_print("\nExiting the story due to an unexpected interrupt...", .07)
				break
			#Prompt to give to AI:
			continuationstory = generate("Continue what happens next based on the information of: " + promptcontentscurated + " " + whatnext + " in three sentences using second person point of view")
			#Append the new content so the algorithm knows what happened in the previous details added.
			promptcontents.append(" " + continuationstory + " ")
			#Print what happens next:
			print("\n")
			delay_print(whatnext + " " + continuationstory + "\n", .05)
	elif MainMenu == 2:
		print("This is a fun project I wanted to make. I always wanted to make one of these AI text adventures! This is a free game with infinite possibilities.\n\nCreated by PatzEdi and GPT-3 (HUGE credits to the chat GPT-3 team over at OpenAI!")
	elif MainMenu == 0:
		delay_print("\nYou are leaving the worlds...", .09)
		exit()
	else:
		while True:
			print("\nNot a valid option!")
			delay_print("\nGoing back...", .07)
			clearscreen()
			break
# InfinityWorlds
Welcome to InfinityWorlds, a configurable and customizable text-based adventure with infinite possibilities, made with the power of OpenAI and their powerful GPT language models.

![infinity-worlds-v2-logo](https://github.com/PatzEdi/InfinityWorlds/assets/116693779/a60485e1-2722-4cc7-93e4-1538a2f61576)


<p align="center">
	<img src="https://img.shields.io/badge/license-GPL%203.0-brightgreen"
		height="23">
	<img src="https://img.shields.io/badge/Creator-PatzEdi-brightgreen"
		height="23">
	<img src="https://img.shields.io/badge/Latest%20Version-V%202.0-brightgreen"
		height="23">
</p>

DISCLAIMER: As of now, you need an OpenAI key in order to run InfinityWorlds. I have been trying to think of a way to provide one API key for everyone. If you have any ideas of how I could do such a thing, feel free to create an issue. For now, you can get you API key at: https://openai.com/api/ 

Thank you OpenAI for providing the API to your GPT models :)

**AND, Huge thank you to [@Sembauke](https://github.com/Sembauke), [@DeadSue](https://github.com/DeadSue), [@ELTANTAWI](https://github.com/ELTANTAWI), [@mikudae](https://github.com/mikudae), and [@fablau](https://github.com/fablau), for starring InfinityWorlds.**

## **Written in python, made with OpenAI's GPT models and passion. Welcome to the Infinity Worlds.**

InfinityWorlds V2 introduces a fully configurable and customizable experience, with the ability to edit colors and styles, edit in-game strings, disabling/enabling certain features, and much more. You can refer to the [Usage](#Usage) section below, which explains how to use these new features.

____________________________________________________________________________
## **Instructions**
- Clone the repo:
```
git clone https://github.com/PatzEdi/InfinityWorlds
```
- Enter the projects directory, enter the src directory, execute the game:
```
cd InfinityWorlds
```
- Enter the src directory:
```
cd src
```
- Execute the game:
```
python3 InfinityWorlds.py
```
- Enjoy!

**If you want to automate running InfinityWorlds (For example, you open a terminal window and want to run it directly without having to manually enter the project files), you can follow these steps:**

1. Enter the root project files:

```
cd $HOME/InfinityWorlds/
```

2. Put the IW.sh shell script under your HOME directory:

```
mv IW.sh $HOME
```
3. Go back to the HOME directory:

```
cd $HOME
```

4. Make the IW.sh shell script executable:

```
chmod +x IW.sh
```
5. Now, when you are in your HOME directory, you can directly call InfinityWorlds by running:

```
./IW.sh
```
____________________________________________________________________________
## **Demo**

![Demo3 (1) copy](https://github.com/PatzEdi/InfinityWorlds/assets/116693779/1a42f04c-d831-4419-882d-164a544704f8)


## **Custom Theme Support (V2)**
Here are a few theme examples:

<img width="1440" alt="Screenshot 2023-07-11 at 12 22 40 PM" src="https://github.com/PatzEdi/InfinityWorlds/assets/116693779/14a72cdf-31cd-419a-a9b7-22c387c0b931">

<img width="1440" alt="Screenshot 2023-07-11 at 9 44 43 AM" src="https://github.com/PatzEdi/InfinityWorlds/assets/116693779/0f0d1b45-02b2-4a1b-b22e-3af5fdc23524">

<img width="1440" alt="Screenshot 2023-07-10 at 9 11 56 PM" src="https://github.com/PatzEdi/InfinityWorlds/assets/116693779/6ddcf994-7b66-40bb-a149-32362e144297">

 
____________________________________________________________________________
## **Features**
- An infinite amount of possibilities - yes, literally.
- Make any story you want
- Includes "flashbacks" meaning that the AI can make connections from previous parts of the story to the present. This means that it can memorize names, places, etc in the story and make connections with other parts of the story later on (Improved in version V2!).
- Easy to use.

Version V2 Introduces a plethora of New Features:

- Custom themes with the ability to choose custom colors and styles for in-game text.
- Ability to edit certain in-game strings. If you don't like some UI strings, you can change them.
- Ability to disable/enable: introduction, animations, activity recaps, and the in-game logo (logo is also introduced in V2).
- Ability to choose your own custom GPT model (default = gpt-3.5-turbo, as this model is sufficient for InfinityWorlds to work well, and is super cheap.
- A custom quit command, as well as a custom animation speed
- Ability to save your stories to a custom directory (If a directory is provided)
- Ability to create an unlimited amount of configurations through the .IWconfig.json file (more info on that below under the [Usage](#Usage) section of this guide)
- Want to make your imagination come true? Infinity Worlds is the right thing for you :)
- Fast and efficient, includes animations (which can be disabled). 
____________________________________________________________________________
## **Usage**

**InfinityWorlds V2 consists of a new config file named .IWconfig.json that is created under your $HOME directory. It is a hidden (.) file. In order to access it, enable hidden files in your file viewer.**

This configuration file contains all of the customizable elements that your can change to your liking. Let's get into how you can use this config file.

As soon as you clone InfinityWorlds and run InfinityWorlds.py, a configuration file will be created. On this first run, you should see an error saying "ERR: An Open AI API Key must be..." and so on.

Open the .IWconfig.json. If you can't find it in your home directory, make sure hidden files are enabled in you file manager.

As soon as you open you .IWconfig.json file, you will see something like this:

```
	{
		"IWSettings": [
			{
				"mainTemplate" : "withAnimations"
			}
		],	
		
		"withAnimations": [
			{
				"openAIAPIKey" : "",
				"gptModel" : "gpt-3.5-turbo",
				"skipIntro" : "False",
				"initialInstructions" : "\nWrite about who/what you want to be...\nExample: A knight, with super powers. Or, anything else you want.\n",
				"disableAnimations" : "False",
				"disableActivityRecaps" : "True",
				"animationSpeed" : ".05",
				"UITextColor" : "",
				"UITextStyle" : "",
				"StoryTextColor" : "",
				"StoryTextStyle" : "",
				"disableLogo" : "False",
				"LogoColor" : "",
				"continueFlag" : "What happens next?",
				"inputFlag" : "-->",
				"quitCommand" : "QQT",
				"storySavePath" : ""
			}
		],
		"withoutAnimations": [
			{
				"openAIAPIKey" : "",
				"gptModel" : "gpt-3.5-turbo",
				"skipIntro" : "True",
				"initialInstructions" : "\nWrite about who/what you want to be...\nExample: A knight, with super powers. Or, anything else you want.\n",
				"disableAnimations" : "True",
				"disableActivityRecaps" : "True",
				"animationSpeed" : ".05",
				"UITextColor" : "",
				"UITextStyle" : "",
				"StoryTextColor" : "",
				"StoryTextStyle" : "",
				"disableLogo" : "False",
				"LogoColor" : "",
				"continueFlag" : "What happens next?",
				"inputFlag" : "-->",
				"quitCommand" : "QQT",
				"storySavePath" : ""
			}
		],
		
		"exampleTheme1": [
			{
				"openAIAPIKey" : "",
				"gptModel" : "gpt-3.5-turbo",
				"skipIntro" : "False",
				"initialInstructions" : "\nWrite about who/what you want to be...\nExample: A knight, with super powers. Or, anything else you want.\n",
				"disableAnimations" : "False",
				"disableActivityRecaps" : "True",
				"animationSpeed" : ".05",
				"UITextColor" : "colors.textColor.pink",
				"UITextStyle" : "colors.style.bold",
				"StoryTextColor" : "colors.textColor.lightgreen",
				"StoryTextStyle" : "colors.style.underline",
				"disableLogo" : "False",
				"LogoColor" : "colors.textColor.cyan",
				"continueFlag" : "Continue:",
				"inputFlag" : "-->",
				"quitCommand" : "QQT",
				"storySavePath" : ""
			}
		]
	}
```

Starting from the top of the JSON configuration, you can see the IWSettings section. Here, under the mainTemplate, you can choose which configuration to choose. By default, the main configuration is "withAnimations", which is chosen as an example. Of course, you can replace the configuration. For example, you can put exampleTheme1 instead of withAnimations, and the example theme I created for you will be used upon running InfinityWorlds. 

**In other words, the IWSettings section is solely used by InfinityWorlds to choose the configuration you want to use on start**

Lets take a look at the exampleTheme1 configuration. 

At first, you will see the "openAIAPIKey" variable in the configuration. In between the two quotation marks, you can paste your OpenAI API key there. Once you do that, you can run InfinityWorlds with the exampleTheme1 configuration (by putting exampleTheme1 in the mainTemplate section under IWSettings), and InfinityWorlds will run with no problems. Do keep in mind, you must provide an API key for each configuration you use, as you may want to use a specific API key for some configurations (Of course, you can always use the same one)

After the API key, you will see the ability to change your GPT model. It is recommended that you use the default (gpt-3.5-turbo), as it is fast, works super well, and super cheap compared to other models. Of course, you can change it to your liking.

The skipIntro variable will skip the introduction of "Welcome to the..." etc. If you want to skip that part, set it to True.

The initialInstructions variable is what you will see upon entering the story. You can edit this to your liking.

disableAnimations will disable all animations. This includes disabling the consecutive printing of single characters of a string, and will rather print out a whole string instantly.

disableActivityRecaps is an option that if enabled will display the activity of your chosen action in the story right after your hit enter. It converts your action in second person as a recap of what you decided to do. Please keep in mind that enabling this option sends a request through the API, leading to possible cost increases.

animationSpeed is used to edit the speed of animations. When strings (assuming disableAnimations = False) are rendered, the lower the animations speed, the faster the rendering. The higher the animation speed, the slower the rendering.

UITextColor is a parameter that can be used to customize the UI text color. The UI includes all strings other than the story and the logo. If you want to use a color, you can refer to the [colors](src/colors.py) file to see all colors/styles. By default, the example theme as the color colors.textColor.pink, which is pink.

UITextStyle is used to add a style to your text. You can make a text bold, or underlined, etc. You can apply these styles as they are applied in the exampleTheme1 configuration, like so: colors.style.bold. The UI will have bolded text. Again, view [colors](src/colors.py) for a full list of styles/colors.

For StoryTextColor and StoryTextStyle, the usage is the same as the UITextColor and the UITextStyle, shown above.

disableLogo can be used to disable (remove) the in-game logo. If the logo is enabled, there will be a random logo chosen each time you run the Main Menu (Total of 8 logos as of now)

For LogoColor, you can define the color of the logo, and it has the same usage as the UITextColor and StoryTextColor variables.

ContinueFlag can be customized to your liking. As seen above, some of the configurations include "Continue:" and others contain "What happens next?". You can change this to your liking.

inputFlag can be customized to your liking as well. It is displayed when you (the user) need to input something in InfinityWorlds (such as an action of what to do next in the story)

quitCommand can customized as well. The quit command is a command that your run within the ContinueFlag input. Once you run it, you will exit the story.

Once you run the quitCommand, if you have defined a storySavePath, InfinityWorlds will ask whether or not you want to save the story to the specified path under the storySavePath parameter in the configuration. If no save path is given, you will not be prompted to save anything.


____________________________________________________________________________
## **Why?**
- I wanted to showcase how one can easily use the power of chat GPT made from OpenAI to make something special. 
- I loved the concept of other apps such as AI Dungeon. They were great. But then... it became worse overtime. So I decided to remake my version, from scratch! Was it worth it? Totally. Especially because I did this in order to figure out on my own how they actually did this through the process of doing it on my own, it is super interesting.
____________________________________________________________________________
## **How?**
- I "fed" the AI prompts that I created on my own. For example, I told it to write about the inputted sentences the user put in, continue the story, and most importantly, write it in second person POV.
- You may be asking, does this Infinity Worlds project actually memorize what is happening and what happened in the past of the story? Yes! It does! And I did this by creating a list and appending all of the information of the story into the list and then feeding the AI with that list plus the new information given by the user. It works perfectly, and it is a great way for the AI to look back on things such as names, places, and the story's history in general from any point in the story!
- OpenAI and their GPT AI Models are super impressive. They made this and other projects come to life, just like your imagination will when you play this!
____________________________________________________________________________
## **User notice**
- Unfortunately, I can not provide one api key for the script and for everyone as of now. I am trying to think of a way to provide one api key for everyone. For now you need to:
- Get your own API key from: https://openai.com/api/
- This project is a project I made for fun for myself, and now for others.
- **If you are on Windows, refer to [this article](https://replit.com/talk/learn/ANSI-Escape-Codes-in-Python/22803) to enable ANSI color coding in your terminal.**
- Logos may not render correctly if they can not fit. If they do not fit, zoom out.
- New features will most likely come soon :)
____________________________________________________________________________
## **Services used (Credits):**
- [OpenAI](https://openai.com/)
- [Shields.io](shields.io)
- [OS Module](https://docs.python.org/3/library/os.html)
- [Sys Module](https://docs.python.org/3/library/sys.html)
- [Time Module](https://docs.python.org/3/library/time.html)
- [Random Module](https://docs.python.org/3/library/random.html)
- [replit.com](https://replit.com/talk/learn/ANSI-Escape-Codes-in-Python/22803) This was really useful, big credits to replit.com!
- [GeeksForGeeks](https://www.geeksforgeeks.org/print-colors-python-terminal/#) This was also very useful, thank you GeeksForGeeks!
- [Logos](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) Thank you for the styles!
____________________________________________________________________________
## **Make sure to leave a star!**
- I hope you like project! If you did, leaving a star is more than enough and greatly appreciated!

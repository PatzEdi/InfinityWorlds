#Main configuration file loader for InfinityWorlds:

import os
import importlib
import pathlib
import json
import colors
from pathlib import Path


#Creates a config file if it does not exist already:
#Return the home directory:
def getHomeDirectory():
     return Path.home()

def createConfigFile():
     #Get the home directory:
     home = getHomeDirectory()
     #Create a hidden config file:
     if os.path.exists(os.path.join(home, ".IWconfig.json")) != True:
          f = open(os.path.join(home, ".IWconfig.json"), 'w')
          f.writelines(['{\n', '\t"IWSettings": [\n', '\t\t{\n', '\t\t\t"mainTemplate" : "withAnimations"\n', '\t\t}\n', '\t],\t\n', '\t\n', '\t"withAnimations": [\n', '\t\t{\n', '\t\t\t"openAIAPIKey" : "",\n', '\t\t\t"gptModel" : "gpt-3.5-turbo",\n', '\t\t\t"skipIntro" : "False",\n', '\t\t\t"initialInstructions" : "\\nWrite about who/what you want to be...\\nExample: A knight, with super powers. Or, anything else you want.\\n",\n', '\t\t\t"disableAnimations" : "False",\n', '\t\t\t"disableActivityRecaps" : "True",\n', '\t\t\t"animationSpeed" : ".05",\n', '\t\t\t"UITextColor" : "",\n', '\t\t\t"UITextStyle" : "",\n', '\t\t\t"StoryTextColor" : "",\n', '\t\t\t"StoryTextStyle" : "",\n', '\t\t\t"disableLogo" : "False",\n', '\t\t\t"LogoColor" : "",\n', '\t\t\t"continueFlag" : "What happens next?",\n', '\t\t\t"inputFlag" : "-->",\n', '\t\t\t"quitCommand" : "QQT",\n', '\t\t\t"storySavePath" : ""\n', '\t\t}\n', '\t],\n', '\t"withoutAnimations": [\n', '\t\t{\n', '\t\t\t"openAIAPIKey" : "",\n', '\t\t\t"gptModel" : "gpt-3.5-turbo",\n', '\t\t\t"skipIntro" : "True",\n', '\t\t\t"initialInstructions" : "\\nWrite about who/what you want to be...\\nExample: A knight, with super powers. Or, anything else you want.\\n",\n', '\t\t\t"disableAnimations" : "True",\n', '\t\t\t"disableActivityRecaps" : "True",\n', '\t\t\t"animationSpeed" : ".05",\n', '\t\t\t"UITextColor" : "",\n', '\t\t\t"UITextStyle" : "",\n', '\t\t\t"StoryTextColor" : "",\n', '\t\t\t"StoryTextStyle" : "",\n', '\t\t\t"disableLogo" : "False",\n', '\t\t\t"LogoColor" : "",\n', '\t\t\t"continueFlag" : "What happens next?",\n', '\t\t\t"inputFlag" : "-->",\n', '\t\t\t"quitCommand" : "QQT",\n', '\t\t\t"storySavePath" : ""\n', '\t\t}\n', '\t],\n', '\t\n', '\t"exampleTheme1": [\n', '\t\t{\n', '\t\t\t"openAIAPIKey" : "",\n', '\t\t\t"gptModel" : "gpt-3.5-turbo",\n', '\t\t\t"skipIntro" : "False",\n', '\t\t\t"initialInstructions" : "\\nWrite about who/what you want to be...\\nExample: A knight, with super powers. Or, anything else you want.\\n",\n', '\t\t\t"disableAnimations" : "False",\n', '\t\t\t"disableActivityRecaps" : "True",\n', '\t\t\t"animationSpeed" : ".05",\n', '\t\t\t"UITextColor" : "colors.textColor.pink",\n', '\t\t\t"UITextStyle" : "colors.style.bold",\n', '\t\t\t"StoryTextColor" : "colors.textColor.lightgreen",\n', '\t\t\t"StoryTextStyle" : "colors.style.underline",\n', '\t\t\t"disableLogo" : "False",\n', '\t\t\t"LogoColor" : "colors.textColor.cyan",\n', '\t\t\t"continueFlag" : "Continue:",\n', '\t\t\t"inputFlag" : "-->",\n', '\t\t\t"quitCommand" : "QQT",\n', '\t\t\t"storySavePath" : ""\n', '\t\t}\n', '\t]\n', '}'])
          f.close()
#Import the elements of the config file:
def importConfig(templateName, filePath, isSettings = False):
        
        with open(filePath) as json_file:
            
            
            #Try to load the JSON data:
            try:
                data = json.load(json_file)
            except:
                raise Exception("ERR: Unable to load JSON data - Is it formatted correctly?")
            
            #See if all items are included:
            #try:
            if isSettings == True:
                for i in data[templateName]:
                    mainTemplate = i['mainTemplate']
            else:
                for i in data[templateName]:
                    apikey = i['openAIAPIKey']
                    gptModel = i['gptModel']
                    skipIntro = i['skipIntro']
                    initialInstructions = i['initialInstructions']
                    disableAnimations = i['disableAnimations']
                    disableActivityRecaps = i['disableActivityRecaps']
                    animationSpeed = i['animationSpeed']
                    UITextColor = i['UITextColor']
                    UITextStyle = i['UITextStyle']
                    StoryTextColor = i['StoryTextColor']
                    StoryTextStyle = i['StoryTextStyle']
                    disableLogo = i['disableLogo']
                    LogoColor = i['LogoColor']
                    continueFlag = i['continueFlag']
                    inputFlag = i['inputFlag']
                    quitCommand = i['quitCommand']
                    storySavePath = i['storySavePath']
                    
            # except:
            #     raise Exception("ERR: Unable to load certain items - Are all items included?")
        if isSettings == True:
            return mainTemplate
        else:
            if skipIntro == "True":
                skipIntro = True
            else:
                skipIntro = False

            if disableAnimations == "True":
                disableAnimations = True
            else:
                disableAnimations = False
            
            if disableActivityRecaps == "True":
                disableActivityRecaps = True
            else:
                disableActivityRecaps = False

            if disableLogo == "True":
                disableLogo = True
            else:
                disableLogo = False

            if apikey == '':
                raise Exception("ERR: An Open AI API key must be provided in the config (.IWconfig.json) file")
            
            #If the colors are left blank in the config file, then make them white (standard)
            if UITextColor == '':
                UITextColor = "colors.textColor.white"
            if StoryTextColor == '':
                StoryTextColor = "colors.textColor.white"
            if LogoColor == '':
                LogoColor = "colors.style.reset"
            
            if UITextStyle == '':
                UITextStyle = "colors.style.reset"
            if StoryTextStyle == '':
                StoryTextStyle = "colors.style.reset"

            #Return the values:
            return apikey, gptModel, skipIntro, initialInstructions, disableAnimations, disableActivityRecaps, animationSpeed, UITextColor, UITextStyle, StoryTextColor, StoryTextStyle, disableLogo, LogoColor, continueFlag, inputFlag, quitCommand, storySavePath


#For colors:


def convertStringToCallableClass(string):
    # String representation of the class
    class_string = string

    # Split the string into its components
    class_parts = class_string.split('.')

    # Get the module and class names
    module_name = ".".join(class_parts[:-2])
    class_name = class_parts[-1]

    # Import the module dynamically
    module = importlib.import_module(module_name)

    # Get the class object from the module
    for part in class_parts[1:]:
        module = getattr(module, part)
    
    class_object = module

    # Now, you can use the class object as needed
    instance = class_object
    # Example usage
    return instance




#First step, create the config file:
# createConfigFile()

# # #Second step, read the contents of the config file:

# # #Template name will be imported from the argparser (as InfinityWorlds will become a CLI tool.)

# templateName = "withoutAnimations"
# openAIAPIKey, skipIntro, disableAnimations = importConfig(templateName, os.path.join(getHomeDirectory(), ".IWconfig.json"))

# print(skipIntro, disableAnimations)
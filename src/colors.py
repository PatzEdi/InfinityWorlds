
#List of colors:


 
class style:

    #Styles:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

class textColor:
    #Colors:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'
    
    #Here, you can create your own, custom colors:
    def rgb(r, g, b): return f"\u001b[38;2;{r};{g};{b}m"

    #Here is an example of a custom color:
    electricblue = rgb(64, 110, 247)

    white = rgb(255, 255, 255)
    
    #Some pastel colors :)
    pastelblue = rgb(143, 196, 156)
    pastelpink = rgb(196, 143, 161)
    pastelyellow = rgb(227, 227, 120)
    pastelorange = rgb(217, 158, 132)
    pastelgreen = rgb(139, 217, 149)
#Background highlights:
class backgroundColor:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'

    #Here, you can create your own, custom colors:
    def rgb(r, g, b): return f"\u001b[48;2;{r};{g};{b}m"
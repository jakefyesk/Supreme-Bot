from SBotAutomatic import *


### Formatting Tool ###
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print color.BOLD + color.RED + '''   _____                                         ____        __ 
  / ___/__  ______  ________  ____ ___  ___     / __ )____  / /_
  \__ \/ / / / __ \/ ___/ _ \/ __ `__ \/ _ \   / __  / __ \/ __/
 ___/ / /_/ / /_/ / /  /  __/ / / / / /  __/  / /_/ / /_/ / /_  
/____/\__,_/ .___/_/   \___/_/ /_/ /_/\___/  /_____/\____/\__/  
          /_/                                                   ''' + color.END
### Choice of Bot ###
BotChoice = raw_input('Which bot would you like to use? Automatic or Manual? (A/M): ').lower()
if BotChoice in ("a", "automatic"):
	print color.BOLD + color.GREEN + 'Using Automatic Bot' + color.END
	Automatic()
elif BotChoice in ("m", "manual"):
	print color.BOLD + color.GREEN + 'Using Manual Bot' + color.END
else:
	print color.BOLD + color.RED + 'INCORRECT CHOICE' + color.END
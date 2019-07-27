import os,time,sys
from colorama import init, Fore, Back, Style
init(autoreset=True)
# Initializing everything from TessaEZEngine (LOL UNFINAL NAME)
print(Fore.CYAN + "Currently loading all variables and functions.")

class Technical(object):
	def __init__(self):
		self.colors = {"black": Fore.BLACK, "red": Fore.RED, "green": Fore.GREEN, "yellow": Fore.YELLOW, "blue": Fore.BLUE, "magenta": Fore.MAGENTA, "cyan": Fore.CYAN, "white": Fore.WHITE}
		print(self.colors['cyan'] + "Technical(__init__) class initialized!")
		pass

tech = Technical()
GameSettings = {}
class Tessa(object):

	def __init__(self):
		self.health = 100
		self.characters = []
		self.ivars = {}
		print(Fore.CYAN + "Tessa(__init__) class initialized!")
		pass
	def DamageSelf(self,intdamage):
		self.health -= intdamage
		return
	def Say(self,character,message):
		if(character > len(self.characters)-1):
			print(Fore.RED + "missingno" + Fore.WHITE + ": " + message)
		else:
			print(self.characters[character].color + self.characters[character].name + Fore.WHITE + ": " + message)
	def GiveChoice(self, question):
		print(question + " [Y/N]: ", end='')
		v = input()
		if(v == "y" or v == "Y"):
			return True
		else:
			return False
	def RegisterChar(self,character):
		self.characters.append(character)
		return
	def SetIVar(self, var, con):
		self.ivars[var] = con
		return
	def GetIVar(self,var):
		return self.ivars.get(var)

class Character(object):
	def __init__(self, name, color):
		self.name = name
		self.color = color
		pass

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print(Fore.GREEN + "Loading characters from characters.txt")
tessa = Tessa()
# Character Registering
chars = open('characters.txt', 'r')
for l in chars:
	l = l.replace('\n', '')
	chardata = l.split(',')
	tessa.RegisterChar(Character(chardata[0], tech.colors[chardata[1]]))
	print("Character " + tech.colors[chardata[1]] + chardata[0] + Fore.RESET + " was registered.")
# Settings reading
gamesettings = open('settings.txt', 'r')
for l in gamesettings:
	l = l.replace('\n', '')
	gs = l.split(':')
	GameSettings[gs[0]] = gs[1]
	print(Fore.CYAN + gs[0] +Fore.RESET+' is '+Fore.CYAN+gs[1])
	print('GameSettings['+gs[0]+'] = '+GameSettings[gs[0]])
if(GameSettings['engine'] != "Tessa"):
	print(Fore.RED + "Engine violation. ("+GameSettings['engine']+" != Tessa)")
	exit(1)

def isDebug():
	return GameSettings['debug']

#OK
print(Fore.CYAN + ("Loading complete.\n"))
cls()
motd = open('motd.txt', 'r')
for l in motd:
	print(l.replace('\n',''))

time.sleep(2)
cls()
# Gameplay
gameplay = open('gameplay.txt', 'r')
ln = 0
inIfSkippage = False
for l in gameplay:
	if(tessa.health < 1):
		print(Fore.RED + "YOU ARE DEAD.")
		input("Press Enter to continue...")
		cls()
		print(Fore.CYAN + GameSettings['goodbye'])
		exit(0)
		continue
	ln += 1
	l = l.replace('\n', '')
	gv = l.split(':')
	if(inIfSkippage):
		if(gv[0] == "ifend"):
			inIfSkippage = False
		elif(gv[0] == "else"):
			inIfSkippage = False
		continue
	if(gv[0] == "print"):
		gv[1] = gv[1].replace('{!nl}', '\n')
		print(gv[1])
	elif(gv[0] == "say"):
		tessa.Say(int(gv[1]), gv[2])
	elif(gv[0] == "sleep"):
		time.sleep(float(gv[1]))
	elif(gv[0] == "question"):
		tessa.SetIVar(gv[1],tessa.GiveChoice(gv[2]))
	elif(gv[0] == "sayvar"):
		tessa.Say(int(gv[1]), gv[3].format(str(tessa.GetIVar(gv[2]))))
	elif(gv[0] == "askinput"):
		print(gv[2]+": ", end='')
		tessa.SetIVar(gv[1], str(input()))
	elif(gv[0] == "if"):
		if(tessa.GetIVar(gv[1]) != True):
			inIfSkippage = True
	elif(gv[0] == "ifend"):
		pass
	elif(gv[0] == "else"):
		inIfSkippage = True
		pass
	elif(gv[0] == "damage"):
		tessa.DamageSelf(int(gv[1]))
	else:
		if isDebug():
			print(Fore.CYAN + "[TESSA]: " + Fore.RED + "UNKNOWN TYPE OF ACTION. (GAMEPLAY.TXT/"+str(ln)+")")

cls()
print(Fore.CYAN + GameSettings['goodbye'])
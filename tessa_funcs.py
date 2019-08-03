import os,time,sys,requests,random,names,json,winsound,argparse,configparser
from colorama import init, Fore, Back, Style
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import simpledialog
from datetime import datetime
init(autoreset=True)
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--editor", action = "store_true", help="Activates editor mode.")
parser.add_argument("-d", "--debug", action = "store_true", help="Activates debug mode.")
args = parser.parse_args()
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
		self.inventory = []
		print(Fore.CYAN + "Tessa(__init__) class initialized!")
		pass
	def DamageSelf(self,intdamage):
		if(GameSettings['health'] != "1" and isDebug()):
			print(Fore.RED+"Damage was stopped. Health is disabled.")
			return
		winsound.Beep(100,10)
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
	def CleanupSaves(self):
		for f in os.listdir("saves"):
			os.unlink("saves/"+f)
	def AddInventory(self, item):
		self.inventory.append(item)
	def HasItem(self,item):
		if item in self.inventory:
			return True
		else:
			return False
	def TakeItem(self, item):
		self.inventory.remove(item)

class Character(object):
	def __init__(self, name, color):
		self.name = name
		self.color = color
		pass

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print(Fore.GREEN + "Loading characters from characters.txt")
tessa = Tessa()
print(Fore.CYAN + "Loading of primary functions and variables was finished.")
def rs():
    abababab = 0
def ex():
    print(Fore.RED + "Bye!")
    exit(0)

def askInput():
    print("")
if(args.editor):
    print(Fore.GREEN + "Entering editor mode...")
    m = Tk()
    m.title("Tessa: Visual Editor (v1.3.0/v1.0.0)")
    m.minsize(600,300)
    mb = Menu(m)
    ts = Menu(mb, tearoff=0)
    ts.add_command(label = "Reset gameplay",command=rs)
    ts.add_command(label = "Reset settings",command=rs)
    ts.add_command(label = "Reset characters",command=rs)
    ts.add_separator()
    ts.add_command(label = "Save",command=ex)
    ts.add_command(label = "Exit",command=ex)
    mb.add_cascade(label="Tessa", menu=ts)
    
    ins = Menu(mb, tearoff=0)
    mb.add_cascade(label="Insert", menu=ins)
    m.config(menu=mb)
    # GUI
    text = Text(m, state='normal')
    text.focus_set()
    text.pack(pady=0,padx=0)
    print(text.get(1.0, END))
    messagebox.showwarning("Tessa","This environment isn't completed at all. Use this at own risk.")
    mainloop()
    print(Fore.RED + "Bye!")
    exit(0)
# Character Registering
if not (os.path.isfile("motd.txt")):
    with open("motd.txt","w") as mt: mt.write("")
if not (os.path.isfile('settings.txt')):
    print(Fore.CYAN + "Settings is missing. Creating default.")
    with open('settings.txt', 'w') as st:
        st.write('gamename:Unknown Game\ngamever:1.0.0\ncreator:Unknown Creator\nhealth:0\ninventory:0')
if not (os.path.isfile('gameplay.txt')):
    print(Fore.CYAN + "Gameplay is missing. Creation impossible. Abandonning.")
    exit(-1)
if not (os.path.isfile('characters.txt')):
    print(Fore.CYAN + "Characters are missing. Trying to recreate...")
    print("Viewing into gameplay...")
    charcount = 0
    gameplay = open("gameplay.txt","r")
    for l in gameplay:
        l = l.replace("\n", "")
        l = l.split(":")
        if(l[0] == "say" or l[0] == "sayvar"): # both of them have charid on l[1]
            if(int(l[1]) > charcount):
                charcount = int(l[1])
                print("Already found "+str(charcount)+" characters.")
    tempv = ""
    for i in range(charcount):
        tempv = tempv+names.get_first_name()+","+random.choice(list(tech.colors))+"\n"
    with open("characters.txt","w") as ch:
        ch.write(tempv)
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

try:
    GameSettings['pastebinplay']
except KeyError:
    usePastebinGameplay = False
else:
    usePastebinGameplay = True

try:
    GameSettings['health']
except KeyError:
    print(Fore.RED + "You cannot remove 'health' parameter from settings!")
    exit(-1)
try:
    GameSettings['inventory']
except KeyError:
    print(Fore.RED + "You cannot remove 'inventory' parameter from settings!")
    exit(-1)

def isDebug():
    global args
    if args.debug: return True
    else: return False

#OK
print(Fore.CYAN + ("Loading complete.\n"))
cls()
motd = open('motd.txt', 'r')
for l in motd:
	print(l.replace('\n',''))

time.sleep(2)
cls()

def SaveGame(line):
    global tessa
    print("Working on savefile.. Saving from line "+str(line))
    savetime = time.time()
    if not (os.path.isdir("saves")):
        os.mkdir("saves")
    sf = configparser.ConfigParser(allow_no_value=True)
    sf.add_section("DefaultSave")
    sf.set("DefaultSave", "ResumeLine", str(line))
    sf.set("DefaultSave", "SaveDate", str(savetime))
    sf.add_section("IVars")
    for ivar in tessa.ivars:
        sf.set("IVars", ivar, tessa.ivars[ivar])
    sff = open("saves/save"+str(savetime)+".ini", 'w')
    sf.write(sff)
    sff.close()

# Gameplay
if(usePastebinGameplay):
    gameplay = requests.get("https://pastebin.com/raw/"+GameSettings['pastebinplay']);
    with open('gameplay.txt','wb') as f:
        f.write(gameplay.content)
gameplay = open('gameplay.txt', 'r')
ln = 0
def GPStart(gp,dln):
    global ln
    ln = dln
    rl = 0
    inIfSkippage = False
    for l in gp:
        rl += 1
        if(rl+1 < ln):
            continue
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
        gva = l.split(':',1)
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
        elif(gv[0] == "give_item"):
            tessa.AddInventory(gv[1])
        elif(gv[0] == "take_item"):
            tessa.TakeItem(gv[1])
        elif(gv[0] == "has_item"):
            if(tessa.HasItem(gv[1]) != True):
                inIfSkippage = True
        elif(gv[0] == "comparestr"):
            if(tessa.GetIVar(gv[1]) != gv[2]):
                inIfSkippage = True
        elif(gv[0] == "ifend"):
            pass
        elif(gv[0] == "else"):
            inIfSkippage = True
            pass
        elif(gv[0] == "damage"):
            tessa.DamageSelf(int(gv[1]))
        # 1.3.0
        elif(gv[0] == "go"):
            if(os.path.isfile(gv[1])):
                GPStart(open(gv[1],'r'))
        elif(gv[0] == "goend"):
            if(os.path.isfile(gv[1])):
                GPStart(open(gv[1],'r'))
                print("    -- The End. --   ")
                exit(0)
        elif(gv[0] == "setvar"):
            tessa.SetIVar(gv[1], gv[2])
        elif(gv[0] == "beep"):
            winsound.Beep(int(gv[1]), int(gv[2]))
        elif(gv[0] == "sound"): # ONLY WAV
            winsound.PlaySound(gv[1], winsound.SND_FILENAME)
        elif(gv[0] == "py"):
            exec(gva[1])
        elif(gv[0] == "tsound"):
            if(gv[1] == "excl"):
                winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
            elif(gv[1] == "ast"):
                winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS)
        else:
            if isDebug():
                print(Fore.CYAN + "[TESSA]: " + Fore.RED + "UNKNOWN TYPE OF ACTION. (GAMEPLAY.TXT/"+str(ln)+")")
slo=0
if(os.path.isdir("saves") and len(os.listdir("saves")) > 0):
    print(Fore.CYAN+"You have "+str(len(os.listdir("saves"))) + " saves available!")
    print(Fore.CYAN+"Choose one to continue or type '0' to start a new one!")
    savel = 1
    savelist = []
    for f in os.listdir('saves'):
        try:
            svf = configparser.ConfigParser()
            svf.read("saves/"+f)
            print("["+str(savel)+"] "+datetime.utcfromtimestamp(int(round(float(svf['DefaultSave']['SaveDate'])))).strftime('%Y-%m-%d %H:%M:%S'))
            savelist.append(f)
            savel += 1
        except KeyError:
            print(Fore.RED + "Some of your save files are corrupted.")
            exit(0)
    print("Enter: ", end='')
    saveloadid = input()
    svf = configparser.ConfigParser()
    svf.read("saves/"+savelist[int(saveloadid)])
    if not(saveloadid == "0"):
        print(Fore.GREEN+"Loading...")
        slo = int(svf['DefaultSave']['ResumeLine'])
        tessa.ivars = {}
        for iv in svf['IVars']:
            tessa.ivars[iv] = svf['IVars'][iv]
        cls()

try:
    GPStart(gameplay,slo)
except KeyboardInterrupt:
    print(Fore.CYAN+"Saving the game..")
    SaveGame(ln)

print("    -- The End. --   ")
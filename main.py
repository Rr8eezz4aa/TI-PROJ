from program import *
from colorama import Fore
import os
import time

os.system('cls' if os.name=='nt' else 'clear')
print(f"""{Fore.RED}==================================================={Fore.LIGHTYELLOW_EX}
████████ ██       ██████  ██████   ██████       ██ 
   ██    ██       ██   ██ ██   ██ ██    ██      ██ 
   ██    ██ █████ ██████  ██████  ██    ██      ██ 
   ██    ██       ██      ██   ██ ██    ██ ██   ██ 
   ██    ██       ██      ██   ██  ██████   █████  {Fore.RED}
===================================================
""", flush=True)

def log(msg):
    print(f"{Fore.RED}[{Fore.LIGHTYELLOW_EX}TI-PROJ{Fore.RED}]{Fore.LIGHTYELLOW_EX}$ {Fore.LIGHTRED_EX}", end="", flush=True)
    for c in msg:
        print(c, end="", flush=True)
        time.sleep(.05)
    print(Fore.RESET)

log("Getting informations from typeiran.com")
info = get_informations()

log("Removing dublicate projects")
info = remove_dublicate_projects(info)

log("Writing projects code")
write_projects_code(info)

log("Saving projects informations")
write_project_informations(info)

print()
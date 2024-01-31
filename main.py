from colorama import Fore, Back
import os, socket, sys

name = socket.gethostname()
ip= socket.gethostbyname(name)

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

def menu():
      os.system('clear')
      title = f'''
                /%&@.           [#] Aliado de Guerra (Kriegsverbündeter).                      
                (.%(#           [#] Usar siempre con responsabilidad y de acuerdo            
               #..&&#&          con la licencia (https://github.com/ZombieGeeK0/MultiTool/blob/main/LICENSE.md).
               #.,&&(@                                    
               #./&&#%          [#] Esta es una herramienta multifunciones creada por ZombieGeek0.
              #*.(&&##%          
              %*,(#%#%&         [#] Ip: {ip}.                        
              ,  /##*/%         [#] Nombre de la máquina: {name}                         
              ,  /##*/%                                   
              ,  /##//%         [00]: Salir.                          
             ,,  ,/(,*/#        [01]: Volver al menú.                          
            *,   (##%///#       [02]: Generar una wordlist con crunch (de palabras).                     
            *,   (##%//(#       [03]: Poner al día todos los paquetes.                          
            *,   ###%//(#                                 
            *,  .#%#%//(#                                 
            *,  .#%%%//(#                                 
            *,  .#%%%//(#                                 
            *,  .#%%%//(#                                 
            *, ..#%%%//(#                                 
            *. ..#%%%/((#                                 
            /. ..#%%%/((#                                 
            /. ..##%%(((#                                 
            /,..,##%%(((#                                 
            /,..,##%%(((#                                 
            /...,(#%%(((#                                 
            /...,##%%((##                                 
            /,..,##%%(#(#                                 
            (((/(#%%#%%&&                                 
            .,.../##/(#%(                                                      
      '''
      print(Fore.YELLOW + Back.RESET + title)

      choice = input(Fore.YELLOW + Back.RESET + '\n[#]> ')

      if choice == '00':
            print(Fore.RESET + Back.RESET)
            os.system('clear')
            sys.exit()

      elif choice == '01':
            menu()

      elif choice == '02':
            print(Fore.YELLOW + Back.RESET + '\n[#] Ingresa la cantidad mínima de caracteres: ')
            choice = input(Fore.YELLOW + Back.RESET + '[#]> ')
            print(Fore.YELLOW + Back.RESET + '\n[#] Ingresa la cantidad máxima de caracteres: ')
            choice2 = input(Fore.YELLOW + Back.RESET + '[#]> ')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            os.system(f'crunch {choice} {choice2}')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            print('\n[#] Presiona ENTER para volver al menú.')
            choice = input(Fore.YELLOW + Back.RESET + '\n[#]> ')
            menu()

      elif choice == '03':
            print('\n[#] En proceso...')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            os.system('sudo apt update && sudo dist-upgrade -y && sudo apt autoremove .y && sudo apt update && sudo apt -y upgrade && sudo apt -y full-upgrade && sudo apt dist-upgrade')
            os.system("alias fullupgrade='sudo apt update && sudo dist-upgrade -y && sudo apt autoremove .y && sudo apt update && sudo apt -y upgrade && sudo apt -y full-upgrade && sudo apt dist-upgrade'")
            print('[#]> ------------------------------------------------------------------------- <[#]')
            print('[#] A partir de ahora, usa el comando fullupgrade para actualizarlo todo.')
            print('\n[#] Presiona ENTER para volver al menú.')
            choice = input(Fore.YELLOW + Back.RESET + '\n[#]> ')
            menu()
      

      else:
            print('\n[#] Error: Command not found :(. Presiona ENTER para volver al menú.')
            choice = input(Fore.YELLOW + Back.RESET + '\n[#]> ')
            menu()

menu()

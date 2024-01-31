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
            *,   (##%///#       [02]: Realizar una búsqueda en plataformas con Sherlock.                         
            *,   (##%//(#                                 
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
            print(Fore.YELLOW + Back.RESET + '\n[#] Ingresa el nombre de usuario: ')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            os.system(f'cd .. && cd sherlock && python3 sherlock {choice}')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            print('\n[#] Presiona ENTER para volver al menú.')
            choice = input(Fore.YELLOW + Back.RESET + '\n[#]> ')
            menu()

      else:
            print('\n[#] Error: Command not found :(. Presiona ENTER para volver al menú.')
            choice = input(Fore.YELLOW + Back.RESET + '\n[#]> ')
            menu()

menu()

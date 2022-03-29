<<<<<<< HEAD
import os, sys, platform
sys.dont_write_bytecode = True
from internal.parser import Parser
class Terminal:
    def Run():
        lines = []
        pr = None
        if platform.architecture()[0] == "WindowsPE":
            os.system('cls')
        else:
            os.system('clear')
        print("Ventura Interpreter 1.3 Phoenix // Terminal mode")
        print('Terminal mode still in Preview')
        while True:
            act = input(f'\33[92m>>>\33[0m ')
            if act == '.clear':
                lines = []
                print('Script was cleared.')
            elif act == '.ver':
                print('Version 1.3 Phoenix // Build 74')
            elif act == '.lines':
                print('Lines in current script:')
                line_num = 0
                for line in lines:
                    line_num += 1
                    print(f'\33[93m{line_num}\33[0m   {line}')
                print('')
            elif act == '.run':
                pr = Parser('')
                pr.Parse(lines)
                del pr
                pr = Parser('')
            elif act == '.help':
                print("Ventura Terminal Mode Help Page\n.ver - Shows version of Ventura.\n.clear - Clears script.\n.lines - Shows all lines in script.\n.run - executes current script.\n.help - Shows help.\n.exit - Close Terminal Mode.\n")
            elif act == '.exit':
                print('Exiting terminal mode...')
                sys.exit()
            else:
                lines.append(act)
=======
import os, sys, platform
sys.dont_write_bytecode = True
from internal.parser import Parser
class Terminal:
    def Run():
        lines = []
        pr = None
        if platform.architecture()[0] == "WindowsPE":
            os.system('cls')
        else:
            os.system('clear')
        print("Ventura Interpreter 1.3 Phoenix // Terminal mode")
        print('Terminal mode still in Preview')
        while True:
            act = input(f'\33[92m>>>\33[0m ')
            if act == '.clear':
                lines = []
                print('Script was cleared.')
            elif act == '.ver':
                print('Version 1.3 Phoenix // Build 74')
            elif act == '.lines':
                print('Lines in current script:')
                line_num = 0
                for line in lines:
                    line_num += 1
                    print(f'\33[93m{line_num}\33[0m   {line}')
                print('')
            elif act == '.run':
                pr = Parser('')
                pr.Parse(lines)
                del pr
                pr = Parser('')
            elif act == '.help':
                print("Ventura Terminal Mode Help Page\n.ver - Shows version of Ventura.\n.clear - Clears script.\n.lines - Shows all lines in script.\n.run - executes current script.\n.help - Shows help.\n.exit - Close Terminal Mode.\n")
            elif act == '.exit':
                print('Exiting terminal mode...')
                sys.exit()
            else:
                lines.append(act)
>>>>>>> origin/master

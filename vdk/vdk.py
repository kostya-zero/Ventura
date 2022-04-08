from sys import exit
from os import system, path, getcwd
from platform import architecture, node, system
from bin.core import Core


core = Core()
core.log('Checking architecture...')
if not architecture()[0] == '64bit':
    core.log('Checking failed! Exiting...')
else:
    core.log('Check.')
    core.log('Loading UI...')

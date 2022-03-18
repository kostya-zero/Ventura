from setuptools import setup
from os import system, environ, path
from Cython.Build import cythonize
from sys import argv, exit
from datetime import datetime
import time

stop = 0.1

def log(msg: str):
    print(f'[{datetime.now().time()}]: {msg}')

# * Greetings!
print('Ventura Build Script')
log('Installing/Updating packages...')
system('pip install PyInstaller')
system('pip install EasyCython')
system('pip install Cython')
system('pip install setuptools')

log('Done.')
log('Checkng files...')
i = 0
if path.exists('src\\ventura.py'): i += 1 ; log('src\\ventura.py -> Found.')
time.sleep(stop)
if path.exists('src\\internal\\arch.pyx'): i += 1 ; log('src\\internal\\arch.pyx -> Found.')
time.sleep(stop)
if path.exists('src\\internal\\args.pyx'): i += 1 ; log('src\\internal\\args.pyx -> Found.')
time.sleep(stop)
if path.exists('src\\internal\\filesystem.pyx'): i += 1 ; log('src\\internal\\filesystem.pyx -> Found.')
time.sleep(stop)
if path.exists('src\\internal\\formater.pyx'): i += 1 ; log('src\\internal\\formater.pyx -> Found.')
time.sleep(stop)
if path.exists('src\\internal\\funcs.pyx'): i += 1 ; log('src\\internal\\funcs.pyx -> Found.')
time.sleep(stop)
if path.exists('src\\internal\\resolver.pyx'): i += 1 ; log('src\\internal\\resolver.pyx -> Found.')
time.sleep(stop)
if path.exists('src\\internal\\exceptions.py'): i += 1 ; log('src\\internal\\exceptions.py -> Found.')
time.sleep(stop)
if path.exists('src\\internal\\parser.py'): i += 1 ; log('src\\internal\\parser.py -> Found.')
time.sleep(stop)
if path.exists('src\\libs\\lib_main.py'): i += 1 ; log('src\\libs\\lib_main.py -> Found.')
time.sleep(stop)
if path.exists('src\\libs\\lib_text.py'): i += 1 ; log('src\\libs\\lib_text.py -> Found.')
time.sleep(stop)
if path.exists('src\\libs\\lib_fstream.py'): i += 1 ; log('src\\libs\\lib_fstream.py -> Found.')
time.sleep(stop)
print(i)

# TODO: Complete this section.
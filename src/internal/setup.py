from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('formater.pyx'))
setup(ext_modules=cythonize('args.pyx'))
setup(ext_modules=cythonize('arch.pyx'))
setup(ext_modules=cythonize('filesystem.pyx'))
setup(ext_modules=cythonize('funcs.pyx'))
setup(ext_modules=cythonize('parser.py'))
setup(ext_modules=cythonize('exceptions.py'))
setup(ext_modules=cythonize('logic.pyx'))
setup(ext_modules=cythonize('resolver.pyx'))
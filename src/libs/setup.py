from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("lib_main.py")
)

setup(
    ext_modules = cythonize("lib_text.py")
)

setup(
    ext_modules = cythonize("lib_shell.py")
)

setup(
    ext_modules = cythonize("lib_fstream.py")
)

setup(
    ext_modules = cythonize("lib_env.pyx")
)

setup(
    ext_modules = cythonize("lib_console.pyx")
)

setup(
    ext_modules = cythonize("lib_dirsmgr.pyx")
)

setup(
    ext_modules = cythonize("lib_hash.pyx")
)

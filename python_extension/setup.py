from distutils.core import setup, Extension

setup(name="noodle",version="1.0",ext_modules=[Extension("noodle",["noodlemodule.c"])])

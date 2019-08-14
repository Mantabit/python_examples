# Compilation of .ui file with pyuic #

1. Locate the Python User-Interface Compiler (`pyuic5`) (on Windows: `C:\Users\xyz\AppData\Local\Continuum\Anaconda\Library\bin\pyuic5.bat` and add the corresponding directory to the environmental variable `PATH`. `pyuic5` comes with the PyQt5 python  package.
2. Compile the design.ui file using `pyuic5 -x design.ui -o design_ui.py` in the windows shell.

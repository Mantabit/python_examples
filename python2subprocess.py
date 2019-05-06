from ECB import initECBapi,setDesCurrents,enableECBCurrents,disableECBCurrents,exitECBapi
from time import sleep
import ast
import sys

"""
only call this script from python2
"""

currents=ast.literal_eval(sys.argv[1])
timesec=ast.literal_eval(sys.argv[2])

sleep(timesec)

sys.stdout.write("currents applied [mA]:"+str(currents))

exitECBapi()
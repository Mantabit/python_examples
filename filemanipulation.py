import os

def moveup():
    cwd=os.getcwd()
    pathcomps=os.path.split(cwd)
    os.chdir(pathcomps[0])

#print all files in the current working idrectory (cwd)
cwd=os.getcwd()
files=[f for f in os.listdir(cwd) if os.path.isfile(f)]
for f in files:
    print(str(f))
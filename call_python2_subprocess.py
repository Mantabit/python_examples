import subprocess

"""
This script will cal the python2 interpreter from a python3 script via bash and will apply a provided
current vector for a certain time in seconds
"""

script = ["python2.7", "python2subprocess.py", "[1000,0,0,0,0,0,0,0]", "2"]    
#this launches a terminal subprocess calling python2 in the current directory and returns the stout in output
process = subprocess.Popen(" ".join(script),shell=True,stdout=subprocess.PIPE,env={"PYTHONPATH": "."})

output,error=process.communicate()

print(output)

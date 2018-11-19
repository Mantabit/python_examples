import matplotlib.pyplot as plt
import numpy as np
import re

#matching and dissecting URLs using regular expressions
url_strings=[]
url_matches=[]
url_strings.append(r"https://www.google.com")
url_strings.append(r"ftp://file_server.com:21/top_secret/life_changing_plans.pdf")
url_strings.append(r"https://regexone.com/lesson/introduction#section")
url_strings.append(r"file://localhost:4040/zip_file")
url_strings.append(r"https://s3cur3-server.com:9999/")
url_strings.append(r"market://search/angry%20birds")

for s in url_strings:
    url_matches.append(re.search(r"(\w+)://([\w\.-]+)(:(\d+))?(.*)?",s))
    
for i in range(0,len(url_strings)):
    print("String: "+url_strings[i])
    print("Protocol: "+url_matches[i].groups()[0])
    print("Host: "+url_matches[i].groups()[1])
    if type(url_matches[i].groups()[3])!=type(None):
        print("Port: "+url_matches[i].groups()[3])
    if type(url_matches[i].groups()[4])!=type(None):
        print("Ressource: "+url_matches[i].groups()[4])
    print("\n")
    
#matching and dissecting Phone Numbers using regular expressions
number_strings=[]
number_matches=[]
regexstring=r"(\+(\d{2})|00 (\d{2}))?(0(\d{2})| (\d{2})) (\d{3}) (\d{2}) (\d{2})"
#compile the regex for faster processing
reg=re.compile(regexstring)
number_strings.append(r"+41 79 829 33 55")
number_strings.append(r"00 41 79 829 44 55")
number_strings.append(r"079 829 33 66")

for s in number_strings:
    number_matches.append(reg.search(s))
    
for i in range(0,len(number_strings)):
    groups=number_matches[i].groups()
    if groups[0]!=None:
        #number of type +41...
        if groups[1]!=None:
            print("International Prefix: "+groups[1])
            print("Second Part: "+groups[3])
            print("Third Part: "+groups[5])
            print("Foruth and Fifth Part: "+groups[6]+" "+groups[7]+"\n")
        else:
            print("International Prefix: "+groups[2])
            print("Second Part: "+groups[5])
            print("Third Part "+groups[6])
            print("Fourth and Fifth: "+groups[7]+" "+groups[8]+"\n")
    else:
        print("International Prefix: None")
        print("Second Part: "+groups[4])
        print("Third Part: "+groups[6])
        print("Fourth and Fifth Part: "+groups[7]+" "+groups[8]+"\n")
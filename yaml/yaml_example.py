# -*- coding: utf-8 -*-

import yaml

#read a simple yaml file and parse it
fp = open("denis.yaml","r")
file_contents = yaml.load(fp)
for (key,value) in file_contents.items():
    print(key) #key corresponds to name of person
    #the value of a certain key is itself a dictionary
    print(value["Name"])
    print(value["Age"])
    print(value["Occupation"])
    print("\n")
fp.close()

#write the same file "denis.yaml" using python
fp = open("denis2.yaml","w")
#create an empty dictionary and fill it
people = {"Denis" : dict() , "Marvin" : dict()}
people["Denis"]["Age"]=25
people["Denis"]["Occupation"]="Electrical Engineer"
people["Denis"]["Male"]=True
people["Marvin"]["Age"]=27
people["Marvin"]["Occupation"]="Electrical Engineer"
people["Marvin"]["Male"]=True
#dump dictionary into yaml file
yaml.dump(people,stream=fp)
fp.close()

#define a yaml object in a single line (useful for ROS commands)
yaml_object = "{Currents : [1000,1000,1000] , State : 0 , DesAdvSpeed : 200}"
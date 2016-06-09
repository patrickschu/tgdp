#The Corpusbuilder
Takes a collection of zip files and a JSON-file to build a corpus according to user criteria. 

##Description
The corpusbuilder takes the following arguments:
     corpusbuilder (inputfile, repair_formatting = True, **kwargs)
    
    
    inputfile --- Location of the JSON file.
    repair_formatting  --- Fixes mis-formatted JSON files. Accepted input: True or False, defaults to True.
    criteria  --- A variable number of conditions on any of the criteria (such as date of birth, gender, ...) contained in the input JSON file. The input needs to be formatted like so: --criterion "operator, condition", e.g. --DOB "> 1900". Detailed description here. 

All the possible criteria and their options for the specific setting are described in the help file which can be accessed by typing

    python corpusbuilder.py --help
    




##How to run it





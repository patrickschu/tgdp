#The Corpusbuilder
Takes a collection of zip files and a JSON-file to build a corpus according to user criteria. 

##Description
The corpusbuilder takes the following arguments:
     corpusbuilder (json_file, input_folder, output_folder, --repair_formatting=True, **kwargs)
    
    json_file --- Location of the JSON file.
    input_folder --- Path to a folder of zip files that will be used to build your corpus.
    output_folder --- Path to a (preferably empty) folder that your corpusfiles will be copied into.
    repair_formatting  --- Fixes mis-formatted JSON files. Accepted input: True or False, defaults to True.
    criteria  --- A variable number of conditions on any of the criteria (such as date of birth, gender, ...) contained in the input JSON file. The input needs to be formatted like so: --criterion "operator, condition", e.g. --DOB "> 1900". Detailed description here. 

All the possible criteria and their options for the specific setting are described in the help file which can be accessed by typing

    python corpusbuilder.py --help
    




##How to run it

This examples shows the basic setup: 

python filepicker.py 'Downloads/informants.json' --gender "=M"





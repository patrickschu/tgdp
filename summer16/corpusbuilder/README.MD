# The Corpusbuilder
Takes a collection of zip files and a JSON-file to build a corpus according to user criteria. 

## Description
The corpusbuilder takes the following arguments:

     corpusbuilder (json_file, input_folder, output_folder, --repair_formatting=True, **kwargs)
    
    json_file --- Location of the JSON file.
    input_folder --- Path to a folder of zip files that will be used to build your corpus.
    output_folder --- Path to a (preferably empty) folder that your corpusfiles will be copied into.
    repair_formatting  --- Fixes mis-formatted JSON files. Accepted input: True or False, defaults to True.
    criteria  --- A variable number of conditions on any of the criteria (such as date of birth, gender, ...) contained in the input JSON file. The input needs to be formatted like so: --criterion "operator, condition", e.g. --DOB "> 1900". Detailed description here. 

All the possible criteria and their options for the specific setting are described in the help file which can be accessed by typing

    python corpusbuilder.py --help
    

## How to run it
Run it in a shell. See here for instructions. 

This example shows the basic setup for the corpusbuilder specificially: 

    python corpusbuilder.py '~/Downloads/informants.json' '~/Downloads/inputfolder' '~/Downloads/outputfolder' --gender "=M"

This will search through all the informant metadata stored in ~/Downloads/informants.json. Since we specified that --gender should be "=M", it will extract all the data associated with speakers that have gender set to "M", i.e. male speakers. It will then go into  ~/Downloads/inputfolder, which we specified as our inputfolder. It will then copy all the files associated with male speakers into ~/Downloads/outputfolder, our output_folder. This is our new corpus. 

More refined settings are possible. This example will extract all male speakers who currently live in Fredericksburg. 

    python corpusbuilder.py [...] --gender "=M" --current_residence "=fredericksburg"

(Note that inputfile etc have been omitted for better readability here; they need to be specified every time the program is run).

Numerical values allow for more fine-grained comparision. The following example will extract all recordings of male speakers born between 1900 and 1940. 

    python corpusbuilder.py [...] --gender "=M" --DOB ">=1900" --DOB "<1941"

 


## Notes:
1. The possible constraints can vary from dataset to dataset. The Texas German corpus contains the following categories: 

>--language_home (e.g. german, unknown, english)

>--current_residence (e.g doss, floresville, universal city)

> --is_locked (e.g. 1,0)

>--gender (e.g. m, f) 

>--created_at (e.g. 2016-05-05 16:41:00, 2016-05-05 16:58:47)

>--updated_at (e.g. 2015-02-04 13:23:59, 2015-03-04 15:16:48)

> --childhood_residence (e.g. clifton, geronemo, rural)

> --island_id (e.g. 1, 0)

>--DOB (e.g. 1908, 1920, 1921) 

>--language_school (e.g. german, unknown)

>--education_complete (e.g. middle school, unknown, elementary school)

>--questionnaire (e.g. {"interview_id":"X","upload_status":"none","informant_id":"X","first_name":"X"," [...]}

>--informant_id (e.g. 344, 345)



2. Capitalization does not matter. *Fredericksburg* is treated the same as *fredericksburg*. 


3. The following comparison operators are allowed: 

>"<": less than
>
>"<=": less than or equal to
>
>">=": more than or equal to
>
>">": more than
>
>"==": equal to
>
>"=":  equal to
>
>"!=": not equal to




# The Corpusbuilder
Takes a collection of zip files and a JSON-file to build a corpus according to user criteria. 

This is useful if you have a big corpus and would like to extract speaker interviews by characteristics, e.g. all speakers from one location, all speakers born before a certain date, of a certain gender, or a combination of those. 

## Description
The corpusbuilder takes the following arguments:

    corpusbuilder (fix_formatting_off, manual_input, json_file, input_folder, output_folder, **criteria)
    
    Basic input:
    json_file --- a [JSON](http://www.json.org/)-formatted file containing informant metadata such as place of residence, age, etc. 
    input_folder ---  a folder containing the entire corpus (files in .wav or .zip format). 
    output_folder --- a (preferably emtpy) folder where the selected corpus files will be copied to. 
    json_file, input_folder, output_folder are all set through a graphical interface after the script is started. 
    criteria  --- A variable number of criteria (such as place of residence, age, ...) to select which files to copy from input_folder to output_folder. Any criteria contained in json_file can be used. 
    Criteria are specified in the terminal before the script is run. 
    The input needs to be formatted like so: --criterion "operator, condition", e.g. --DOB "> 1900". Detailed description [here](https://github.com/patrickschu/tgdp/blob/master/summer16/corpusbuilder/README.MD#how-to-run-it). 
    
    Optional input:
    fix_formatting_off --- if set, switches off algorithm that fixes faulty formatting in JSON files. 
    manual_input --- if set, accepts a text file instead of using the graphical interface. That way, a list of directories can be provided as input_folder. The text file needs to consists of one full path per line. It will be chosen through a GUI.

All the possible criteria and their options for the specific setting are described in the help file which can be accessed by typing

    python corpusbuilder.py --help
    

## How to run it
Run it in a shell. See here for instructions. 

This example shows the basic setup for the corpusbuilder specificially: 

    python corpusbuilder.py --gender "=M"

Since we specified that `--gender` should be `"=M"`, the corpusbuilder will search the metadata file and extract all the data associated with speakers that have gender set to "M", i.e. male speakers. The terminal input needs to be formatted like this: `--criterion "operator, condition"`. It then extracts all matching files from the input_folder. See [here](https://github.com/patrickschu/tgdp/tree/master/summer16/corpusbuilder#notes) for a complete list of operators. 

More refined settings are possible. This example will extract all male speakers who currently live in Fredericksburg. 

    python corpusbuilder.py --gender "=M" --current_residence "=fredericksburg"

Numerical values allow for more fine-grained comparision. The following example will extract all recordings of male speakers born between 1900 and 1940. 

    python corpusbuilder.py --gender "=M" --DOB ">=1900" --DOB "<1941"

All settings are described in more detail in the help file which can be accessed by running `python corpusbuilder.py --help`.

## Notes:
**1. The possible constraints can vary from dataset to dataset.** 

Type `python corpusbuilder.py --help` to see which ones are available in your dataset. The Texas German corpus can be sorted by the following categories:

>--language_home (e.g. german, unknown, english)

>--current_residence (e.g doss, floresville, universal city)

>--is_locked (e.g. 1,0)

>--gender (e.g. m, f) 

>--created_at (e.g. 2016-05-05 16:41:00, 2016-05-05 16:58:47)

>--updated_at (e.g. 2015-02-04 13:23:59, 2015-03-04 15:16:48)

>--childhood_residence (e.g. clifton, geronemo, rural)

>--island_id (e.g. 1, 0)

>--DOB (e.g. 1908, 1920, 1921) 

>--language_school (e.g. german, unknown)

>--education_complete (e.g. middle school, unknown, elementary school)

>--questionnaire (e.g. {"interview_id":"X","upload_status":"none","informant_id":"X","first_name":"X"," [...]}

>--informant_id (e.g. 344, 345)

**2. The following comparisons are possible:**

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

**3. Capitalization does not matter.** *Fredericksburg* is treated the same as *fredericksburg*. 

**4. Missing data can trip you up. If you for example coding missing dates of birth as DOB = 0, this will match searches like `--DOB "<1941"` although this might not be true. 

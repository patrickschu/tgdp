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
- Capitalization does not matter. *Fredericksburg* is treated the same as *fredericksburg*. 
- The following comparison operators are allowed: 

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

- The possible constraints can vary from dataset to dataset. The Texas German corpus contains the following categories: 

>--language_home (e.g. german, unknown, english)

>--current_residence (e.g doss, floresville, universal city)

> --is_locked (e.g. 1,0)

>--gender (e.g. m, f) 

>--created_at (e.g. 2016-05-05 16:41:00, 2016-05-05 16:58:47)

>--updated_at (e.g. 2015-02-04 13:23:59, 2015-03-04 15:16:48)

> --childhood_residence (e.g. clifton, geronemo, rural)

> --island_id (e.g. 1, 0)
>--DOB (e.g. 1908, 1920, 1921)
  --language_school LANGUAGE_SCHOOL
                        Possible input to the argument 'language_school'
                        includes: german, unknown, None, english
  --education_complete EDUCATION_COMPLETE
                        Possible input to the argument 'education_complete'
                        includes: None, middle school, unknown, elementary
                        school, college, high school, graduate, professional
                        degree
  --questionnaire QUESTIONNAIRE
                        Possible input to the argument 'questionnaire'
                        includes: , {"interview_id":"694417549","upload_status
                        ":"none","informant_id":"26","first_name":"aldolph","m
                        iddle_name":"","last_name":"scheel","gender":"m","date
                        _of_birth":"1912-01-01","city_of_birth":"new braunfels
                        ","state_of_birth":"texas","country_of_birth":"usa","s
                        treet_address_of_residence":"481 old cimarron
                        trail","city_of_residence":"universal city","state_of_
                        residence":"texas","country_of_residence":"usa","phone
                        _number":"","previous_residences":"comal county, tx","
                        religious_affiliation":"catholic","religious_affiliati
                        on_other":"","region_in_europe_of_origin":"michaelsrom
                        bach, hessen, germany","first_languages_german_english
                        _german":"german","first_languages_german_english_comm
                        ent":"","languages_at_school_entry_german":"german","l
                        anguages_at_school_entry_comment":"","second_language_
                        age":"10","who_taught_second_language":"schoolteachers
                        at honey creek catholic school","how_often_child_germa
                        n_parents":"always","how_often_child_german_parents_co
                        mment":"","how_often_child_english_parents":"never","h
                        ow_often_child_english_parents_comment":"","how_often_
                        child_german_grandparents":"always","how_often_child_g
                        erman_grandparents_comment":"","how_often_child_englis
                        h_grandparents":"never","how_often_child_english_grand
                        parents_comment":"","how_often_child_german_teachers":
                        "often","how_often_child_german_teachers_comment":"","
                        how_often_child_english_teachers":"sometimes","how_oft
                        en_child_english_teachers_comment":"","how_often_child
                        _german_friends":"often","how_often_child_german_frien
                        ds_co
  --informant_id INFORMANT_ID
                        Possible input to the argument 'informant_id'
                        includes: 344, 345, 346, 347, 340, 341, 342, 343, 348,
                        292, 199, 198, 195, 194, 197, 196, 191, 190, 193, 192,
                        449, 448, 443, 442, 440, 447, 446, 445, 444, 108, 102,
                        103, 101, 106, 107, 104, 105, 39, 38, 33, 32, 31, 30,
                        37, 36, 35, 34, 438, 439, 436, 437, 434, 433, 430,
                        431, 339, 338, 335, 334, 337, 336, 331, 330, 333, 332,
                        6, 98, 91, 90, 93, 92, 95, 94, 97, 96, 239, 235, 233,
                        1, 147, 144, 145, 142, 143, 140, 141, 149, 133, 132,
                        131, 130, 137, 136, 135, 134, 139, 138, 24, 25, 26,
                        27, 20, 21, 22, 23, 28, 29, 407, 406, 405, 404, 403,
                        402, 401, 400, 409, 408, 379, 378, 371, 370, 373, 372,
                        375, 374, 377, 393, 392, 88, 89, 397, 396, 395, 394,
                        82, 83, 80, 81, 86, 87, 84, 85, 7, None, 245, 244,
                        247, 241, 240, 249, 248, 450, 451, 453, 454, 455, 179,
                        178, 177, 176, 175, 174, 173, 172, 171, 170, 182, 183,
                        180, 181, 186, 187, 184, 185, 188, 189, 11, 10, 13,
                        12, 15, 14, 17, 16, 19, 18, 322, 323, 320, 321, 326,
                        327, 328, 329, 201, 200, 202, 205, 204, 207, 206, 209,
                        208, 77, 76, 75, 74, 73, 72, 71, 70, 79, 78, 2, 8,
                        120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 414,
                        415, 416, 417, 410, 411, 412, 413, 319, 318, 313, 312,
                        311, 310, 317, 316, 315, 314, 3, 368, 369, 366, 367,
                        365, 380, 381, 382, 384, 385, 386, 387, 388, 389, 60,
                        61, 62, 63, 64, 65, 66, 67, 252, 69, 250, 251, 253,
                        254, 255, 168, 169, 164, 165, 166, 167, 160, 161, 162,
                        163, 9, 352, 350, 216, 214, 215, 212, 213, 210, 211,
                        219, 4, 281, 283, 282, 285, 284, 287, 286, 262, 261,
                        268, 59, 58, 55, 54, 57, 56, 51, 50, 53, 52, 115, 114,
                        117, 116




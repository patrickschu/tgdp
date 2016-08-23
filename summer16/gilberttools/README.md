# The Gilbertfinder
Takes a collection of recordings of Gilbert's interview questions and extracts files according to user criteria. In addition to printing results out on the screen, the gilbertfinder can also export them as a comma-separated spreadsheet or move relevant files to a new directory. 

This is useful to extract all instances of a sentence, word or sound from the bigger corpus. 

Download the script [here](https://raw.githubusercontent.com/patrickschu/tgdp/master/summer16/gilberttools/gilbertfinder_original.py).

## Description
The gilbertfinder takes the following arguments:

    gilbertfinder (input_file --move_data --output_csv *criteria)
    
    Basic input:
    
    input_file --- A comma-separated spreadsheet containing the Gilbert sentence numbers, target forms, etc.
    criteria  --- Any number of conditions, where the criterion can be any column in input_file.
    These to be formatted like so:  --criterion "operator, condition"
    
     e.g. --transcription "= ʁ" to extract files whose transcription contains the character  "ʁ".
    Criteria are specified in the terminal before the script is run. Every column in the input_file is a valid criterion. 
        
    Optional input:
    --move_data --- If this flag is set, files that match criteria are copied from input_folder to output_folder. input_folder and output_folder are set through graphical interface.
    
     --output_csv --- If this flag is set, a csv file containing the sentences that match the criteria is written. The output_folder is set through graphical interface.
    

All the possible criteria and their options for the specific setting are described in the help file which can be accessed by typing

    python gilbertfinder.py --help
    

## How to run it
Run it in a shell. See here for instructions. 

#### The basics 

This example illustrated the basic setup for the gilbertfinder: 

    python gilbertfinder.py gilbert_questions.csv --transcription "=ʁ" --items "<3"

Since we specified that `--transcription` needs to contain `"ʁ"`, the corpusbuilder will search the metadata file and extract all the Gilbert sentences that contain this sound, such as *diː haːɐ̯ˈbʏʁstə*. Additionally, we set `--items` to `<3`, that is only sentences with less than 3 words will be extracted. 

Setting the `--output_csv` flag allows us to output our results as a comma-separated spreadsheet: 

    python gilbertfinder.py gilbert_questions.csv --transcription "=ʁ" --items "<3"  --move_data --output_csv

The spreadsheet will be saved to a folder specified by the user through a graphical interface. 

If we  set the `--move_data` flag like so,

    python gilbertfinder.py gilbert_questions.csv --transcription "=ʁ" --items "<3"  --move_data

the gilbertfinder will copy all recordings that meet the criteria from an input_folder to an output_folder, both specified by the user through the graphical interface. Each sentence will be copied to a folder named after the sentence number, e.g. recordings of sentence 37 will be copied to a folder called *37*. In that folder, a spreadsheet will be created, containing 
columns for:

 - id 	*Unique row number*

 - file_name 	*Full name of file, e.g. '1-34-3-16-a.wav'*

 - gilbert_number 	*Number of sentence in the Gilbert questionnaire, e.g. '1'*

 - input_form 	*The Gilbert sentence, e.g 'a hairbrush'*
 
 - target_form 	*The expected German target form, e.g. 'eine haarbuerste'*

 - variable 	*The variable searched for, e.g. 'ʁ'*
  
 - transcription 	*Phonetic transcription of the target form in Standard German, e.g. 'ˈaɪ̯nə haːɐ̯ˈbʏʁstə'*
 
 - post_sound 	*Phonetic context: The sound following the variable, e.g. 's'*
 
 - pre_sound 	*Phonetic context: The sound preceding the variable, e.g. 'ʏ'*

 - speaker_number 	*The speaker number, e.g. '10'*

 - dob 	*Date of birth of speaker*
 
 - gender 	*Gender of speaker*
 
 - location 	*The current residence of the speaker, e.g. 'fredericksburg'*

 - iver_number 	*The interviewer number, e.g. '1'*
 

    
All settings are described in more detail in the help file which can be accessed by running `python gilbertfinder.py --help`.

## Notes:

The transcriptions are Standard German realizations of the target form, not transcriptions of what the speaker actually produced in each recording. 


All transcriptions were extracted from [de.wiktionary.org](de.wiktionary.org). If there were various transcriptions available, the first one was chosen. 



# Summer 2016 Corpus tools

Contains the [Datadownloader](https://github.com/patrickschu/tgdp/tree/master/summer16/downloader) and the [Corpusbuilder](https://github.com/patrickschu/tgdp/tree/master/summer16/corpusbuilder). 





##Agenda
Develop dialects maps for Texas English; in the process produce tools for future use on any data from speechislands website

####Requirements

- Tools should be easily executable in shell, per copy&paste commands (Linux, Mac, Cygwin, Win)

- No outside program installation or computing expertise necessary;
 
- Clear error messages, documentation

---
####I STEP 1
Downloading big datasets

[Python script](https://raw.githubusercontent.com/patrickschu/tgdp/master/summer16/downloader.py)

DONE

---
####II STEP 2
A. Extracting files needed based on criteria (e.g. Fredericksburg files only)

[Python script](https://raw.githubusercontent.com/patrickschu/tgdp/master/summer16/corpusbuilder/corpusbuilder_original.py)

DONE

B. Extracting Gilbert files by phonetic criteria and word count

[Python script](https://raw.githubusercontent.com/patrickschu/tgdp/master/summer16/gilberttools/gilbertfinder.py)

DONE EXCEPT FOR DOCUMENTATION

---
####III STEP 3
Make measurements 
Produce spreadsheet for Mapping application, e.g. Gabmap

A.Extract 
i: versus y:, "the only difference is lip-rounding", Benware 8. 

i versus y, "the only difference is lip-rounding", Benware 8.

~~e versus oe~~

B. Measure per speaker: Distance unrounded vs rounded. [Vowel chart](https://utexas.box.com/shared/static/s8waxx113wxzolpbsyj2oecrf3tnu7nv.jpg) from Benware. 

C. Lip-rounding is mainly reflected in the F3 measurement, Ladefoged 131-32: Plot F1-F2, as well as F1-F3. [Chart](https://utexas.box.com/shared/static/4ihj2hyc82lu3onriwao8d390d12yndg.jpg) from Ladefoged. 

D. Translate into spreadsheet: one measurement per location, per speaker? Cf Gabmap conventions. 







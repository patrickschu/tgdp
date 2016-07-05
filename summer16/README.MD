# Summer 2016 Corpus tools

Contains the [Datadownloader](https://github.com/patrickschu/tgdp/tree/master/summer16/downloader), the [Corpusbuilder](https://github.com/patrickschu/tgdp/tree/master/summer16/corpusbuilder) and the [Gilbertfinder](https://raw.githubusercontent.com/patrickschu/tgdp/master/summer16/gilberttools/gilbertfinder.py).

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

~~e versus oe, lax and tense~~

[Vowel chart](https://utexas.box.com/shared/static/s8waxx113wxzolpbsyj2oecrf3tnu7nv.jpg) from Benware.

Liprounding lengthens front part of vocal tract, lowering frequencies of front cavity resonances. 

Lip-rounding is mainly reflected in the F3 measurement, Ladefoged 131-32: Plot F1-F2, as well as F1-F3. [Chart](https://utexas.box.com/shared/static/4ihj2hyc82lu3onriwao8d390d12yndg.jpg) from Ladefoged. 

Rounding leads to lower F2;  closer proximity of F2 and F3; lowers center of gravity for spectral peak formed by F2 and F3 (??) ; decreases bandwidth of 3rd formant, Stevens 291-292.

The increased prominence of spectral peak (F2, F3, F4 for front vowels) and lowered COG of this peak, are prime acoustic correlates of rounding, Stevens 294. 

B. Measure per speaker
- Vowel formants F1, F2, F3 --> measure points??
- Distance unrounded vs rounded. 
- How merged are they. 



C. Translate into spreadsheet: one measurement per location, per speaker? Cf Gabmap conventions. 

Stevens, K. Acoustic Phonetics, MIT Press. 
Ladefoged, P. Phonetic Data Analysis, Blackwell. 
Benware, W. Phonetics and Phonology of Modern German. Georgetown Press. 





# vowel_capture_aug09
# Tyler Kendall, 2009
#
# Editor script for capturing vowel formant data (and Praat setting inforation) in three formats:
#  (a) 1/3 and 2/3 locations, stored to main ..._vowels.txt file (and/or printed to Praat's info window)
#  (b) full formant contours, stored in individual .txt files
#  (c) EPS files of the spectrogram and formant track for each vowel's selected span ± .02 seconds
# These files are stored in the same directory as this script.  They are labeled according to the name 
#   of the sound file.
#
# This script works best when used with a Sound+TextGrid tier with the vowels labeled in the first (and
#   only) tier of the TextGrid.  When used this way you don't need to enter anything in the form window.
#
# The data from the main ..._vowels.txt file can easily be trimmed down to a NORM-ready file (cf.
#   http://ncslaap.lib.ncsu.edu/tools/norm/ ) by removing columns 3,4,6,7,11,12,16,17, and 18.
#   Tyler likes to keep the vowel duration data and storing it in the 3rd column (NORM's "context" column).
#   In R, using the vowels.R package, this can be done by executing:
#   > data<-read.delim(file.choose(), header=FALSE) # assuming you don't add header info to the file
#   > vowels<-data[,c(1,2,5,8,9,10,13,14,15)] # column 5 is duration
#   > library("vowels") # load the vowels.R package, if it's not already loaded
#   > vowels<-label.columns(vowels)

form What is the vowel context?
	boolean getwordfromTextGrid 1
	comment Or uncheck and type the word here:
	sentence word
	comment ------------------------------
	boolean showinfo 0
	boolean writeout 1
	sentence notes
endform

settings$ = Editor info

winl = extractNumber(settings$, "Window start: ")
winr = extractNumber(settings$, "Window end: ")

# if there is a textgrid attempt to get the default vowel label from the current interval.
vowel$ = word$
if (getwordfromTextGrid)
	editortype$ = extractLine$(settings$, "Editor type: ")
	if (editortype$ == "TextGridEditor")
		label$ = Get label of interval
		if (label$ != "")
			vowel$ = label$
		endif
	endif
endif

# if vowel is still blank, reprompt the user
if (vowel$ == "")
	form What is the vowel context?
		sentence wordAgain
	endform
	vowel$ = wordAgain$
endif

begin = Get start of selection
end = Get end of selection
dur = (end-begin)

onset = begin + (dur/3)
Move cursor to... onset
opitch = Get pitch
of1 = Get first formant
of2 = Get second formant
of3 = Get third formant

glide = end - (dur/3)
Move cursor to... glide
gpitch = Get pitch
gf1 = Get first formant
gf2 = Get second formant
gf3 = Get third formant

maxforms$ = extractLine$(settings$, "Formant maximum formant: ")
numpoles$ = extractLine$(settings$, "Formant number of poles: ")

soundinfo$ = Sound info
sndfile$ = extractLine$(soundinfo$, "Object name: ")

if showinfo
	clearinfo
	printline File/Spkr'tab$'Vowel'tab$'Start'tab$'End'tab$'Dur'tab$'oTime'tab$'oPitch'tab$'oF1'tab$'oF2'tab$'oF3'tab$'gTime'tab$'gPitch'tab$'gF1'tab$'gF2'tab$'gF3'tab$'MaxFormants'tab$'NumberPoles'tab$'Notes
	printline 'sndfile$''tab$''vowel$''tab$''begin:3''tab$''end:3''tab$''dur:3''tab$''onset:3''tab$''opitch:2''tab$''of1:2''tab$''of2:2''tab$''of3:2''tab$''glide:3''tab$''gpitch:2''tab$''gf1:2''tab$''gf2:2''tab$''gf3:2''tab$''maxforms$''tab$''numpoles$''tab$''notes$'
	printline
endif

if writeout
	fileappend "'sndfile$'_vowels.txt" 'sndfile$''tab$''vowel$''tab$''begin:3''tab$''end:3''tab$''dur:3''tab$''onset:3''tab$''opitch:2''tab$''of1:2''tab$''of2:2''tab$''of3:2''tab$''glide:3''tab$''gpitch:2''tab$''gf1:2''tab$''gf2:2''tab$''gf3:2''tab$''maxforms$''tab$''numpoles$''tab$''notes$''newline$'
	printline Wrote the data to 'defaultDirectory$'/'sndfile$'_vowels.txt
endif

Select... begin end

if writeout
	all$ = Formant listing
	fileappend "'sndfile$'_'vowel$'_ftrack.txt" 'all$'
	printline Wrote the full formant track to 'defaultDirectory$'/'sndfile$'_'vowel$'_ftrack.txt

	zbegin = begin - 0.02
	zend = end + 0.02
	Zoom... zbegin zend
	endeditor
	Black
	editor 
	Paint visible spectrogram... 1 far 1 1 1
	endeditor
	Red
	editor
	Draw visible formant contour... 0 no 0 0 0
	endeditor
	Write to EPS file... 'sndfile$'_'vowel$'_spectrogram.eps
	editor
	Zoom... winl winr
	printline Wrote the spectrogram to 'defaultDirectory$'/'sndfile$'_'vowel$'_spectrogram.eps
endif
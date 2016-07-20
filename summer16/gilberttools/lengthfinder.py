import wave
import re
import codecs

#determine length of wav file
def lengthfinder(wav_file):
	"""
	The lengthfinder takes a path to a wav_file as input, returns its length.
	We use this to make Praat Textgrids.
	"""
	f=wave.open(wav_file,'r')
	frames = f.getnframes()
	rate = f.getframerate()
	duration = frames / float(rate)
	return duration
	
lengthfinder('/Users/ps22344/Desktop/dataset_rounding/short_i/2/1-24-2-2-a.wav')




textgrid_template="""File type = "ooTextFile"
Object class = "TextGrid"

xmin = 0 
xmax = 11 
tiers? <exists> 
size = 1 
item []: 
    item [1]:
        class = "IntervalTier" 
        name = "" 
        xmin = 0 
        xmax = 11 
        intervals: size = 1 
        intervals [1]:
            xmin = 0 
            xmax = 11 
            text = "" """



def textgridmaker(file_name, tier_name, transcription, length):
	"""
	The textgridmaker creates a one-tier Praat Textgrid and saves it to file_name. 
	Tier_name is the name of the tier, transcription then entry on that tier.
	Length is the desired length, e.g. the length of the sound file. 
	"""
	print "before", textgrid_template, "\n\n"
	outputgrid= re.sub(r'name = \"\" ', 'name = \"'+tier_name+'\" ', textgrid_template)
	outputgrid= re.sub(r'text = \"\" ', 'text = \"'+transcription+'\" ', outputgrid)
	outputgrid= re.sub(r"xmax = .*? \n", "xmax = "+str(length)+" \n", outputgrid)
	print outputgrid
	with codecs.open(file_name, "w", "utf-8") as outputfile:
		outputfile.write(outputgrid)
	

textgridmaker("aa", "erere", "assssssikind", 20000)
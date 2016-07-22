#exploratory plotting after first measurements of hairbrush

#Patrick's ue: 452.98	1182.29	2337.36

#Moving parts
setwd('~/Desktop/rplots')
hair=read.csv('/Users/ps22344/Downloads/tgdp/summer16/gilberttools/gilbertsound_21.csv', header=T)
outputfile='sentence21_F1_F2.png'

#Print
cat ("Range F1");
f1range=range(hair$oF1, na.rm=TRUE);
print (f1range)
cat ("Range F2");
f2range=range(hair$oF2, na.rm=TRUE);
print (f2range)


summary(hair);


#Make F1 - F2 plot
png(outputfile,  width=960, height=640, res=100);

	plot(hair$oF2, hair$oF1, ylim=c(810, 370), xlim=c(2300,1000), 
	type="n", main="Scatterplot of all tokens of /ue/ in sentence 21");

	text( hair$oF2, hair$oF1, labels=hair$speaker_number, col=c("red", "blue")[hair$gender]);

	points (1387, 400, col="red", pch=3, cex=3);
	points(1182.29, 452.98, col="green", pch="Patrick", cex=3);
	legend('bottomright', legend="Speaker IDs; men in blue, women in red; blue cross is mean from Rausch 72; green cross is Patrick's vowel");

dev.off()


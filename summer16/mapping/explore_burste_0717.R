#exploratory plotting after first measurements of hairbrush

#Patrick's ue: 452.98	1182.29	2337.36

#Moving parts
setwd('~/Desktop/rplots')
hair=read.csv('/Users/ps22344/Downloads/tgdp/summer16/gilberttools/gilbertsound_21.csv', header=T)
outputfile='sentence21'

#Print
cat ("Range F1");
f1range=range(hair$oF1, na.rm=TRUE);
print (f1range)
cat ("Range F2");
f2range=range(hair$oF2, na.rm=TRUE);
print (f2range)
cat ("Range F3");
f3range=range(hair$oF3, na.rm=TRUE);
print (f3range)

summary(hair);


#Make F1 - F2 plot
png(paste(outputfile, "F1_F2.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF2, hair$oF1, ylim=c(810, 370), xlim=c(2300,1000), xlab="F2", ylab="F1",
	type="n", main="Scatterplot of all tokens of /ue/ in sentence 21");

	text( hair$oF2, hair$oF1, labels=hair$speaker_number, col=c("red", "blue")[hair$gender]);

	points (1387, 400, col="red", pch=3, cex=3);
	points(1182.29, 452.98, col="green", pch="Patrick", cex=2);
	legend('bottomright', legend="Speaker IDs; men in blue, women in red; blue cross is mean from Rausch 72; 'P' is Patrick's vowel");

dev.off()

#Make F1 - F3 plot
png(paste(outputfile, "F1_F3.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF3, hair$oF1, ylim=c(810, 370), xlim=c(2500,1000), xlab="F3", ylab="F1",
	type="n", main="Scatterplot of all tokens of /ue/ in sentence 21");

	text( hair$oF3, hair$oF1, labels=hair$speaker_number, col=c("red", "blue")[hair$gender]);


	points(2337.36, 452.98, col="green", pch="P", cex=2);
	legend('bottomright', legend="Speaker IDs; men in blue, women in red; 'P' is Patrick's vowel");

dev.off()



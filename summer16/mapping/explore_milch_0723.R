#exploratory plotting after first measurements of lightning bug

#Patrick's ue in kuerbis F1 is surely mismeasured, ill keep it out 125.66	1162.02	2093.16
#Moving parts
setwd('~/Desktop/rplots')
#read the csv file containing measurements
hair=read.csv('/Users/ps22344/Downloads/tgdp/summer16/gilberttools/gilbertsound_26_shorti.csv', header=T)
outputfile='sentence 26'

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


#Print
tokens=nrow(hair)-summary(hair$oF1)[7];
cat("# of tokens: ", tokens);
tokens2=nrow(hair[complete.cases(hair$oF1),]);
cat("# of tokens: ", tokens2);

#Make F1 - F2 plot
png(paste(outputfile, "F1_F2.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF2, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(1100, f2range[2]+100), xlab="F2", ylab="F1",	type="n", main=paste("Scatterplot of all tokens of ɪ in ", outputfile));

	text( hair$oF2, hair$oF1, labels=hair$speaker_number, col=c("red", "blue")[hair$gender]);

	points (1387, 400, col="blue", pch="ʏ", cex=3);
	points (2025, 371, col="blue", pch="ɪ", cex=3);
	points(1933, 455, col="green", pch="P", cex=2);
	legend('bottomright', legend="Speaker IDs; men in blue, women in red; blue IPA is mean from Rausch 72; 'P' is Patrick's vowel");

dev.off()

#Make F1 - F3 plot
png(paste(outputfile, "F1_F3.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF3, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(f3range[1]-100, f3range[2]+100) , xlab="F3", ylab="F1",
	type="n", main=paste("Scatterplot of all tokens of ɪ in ", outputfile));

	text( hair$oF3, hair$oF1, labels=hair$speaker_number, col=c("red", "blue")[hair$gender]);


	points(2579, 455, col="green", pch="P", cex=2);
	legend('bottomright', legend="Speaker IDs; men in blue, women in red; 'P' is Patrick's vowel");

dev.off()

#Patrick's milch
# 455.09	1933.77	2579.32

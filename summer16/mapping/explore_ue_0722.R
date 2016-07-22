#exploratory plotting after first measurements of all short ue

#Patrick's ue in kuerbis F1 is surely mismeasured, ill keep it out 125.66 -->460	1162.02	2093.16
#Patrick's ue: 452.98	1182.29	2337.36
#Patrick's ue in wuermchen: 511.64	1345.00	2258.89	



#Moving parts
setwd('~/Desktop/rplots')
#read the csv file containing measurements
hair=read.csv('~/Downloads/tgdp/summer16/mapping/gilbertsound_1.csvgilbertsound_16.csv_merged.csvgilbertsound_21.csv_merged.csvgilbertsound_111.csv_merged.csvgilbertsound_125.csv_merged.csv', header=T)
outputfile='entire dataset by location'
#TO DO: set limits up here
#Print
tokens=nrow(hair)-summary(hair$oF1)[7]
cat("# of tokens: ", tokens)

f1range=range(hair$oF1, na.rm=TRUE);
f2range=range(hair$oF2, na.rm=TRUE);
f3range=range(hair$oF3, na.rm=TRUE);

cat ("Range F1", f1range);
cat ("Range F2", f2range);
cat ("Range F3", f3range);




outputfile='entire dataset by location'
#Make F1 - F2 plot
png(paste(outputfile, "F1_F2.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF2, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(1100, f2range[2]+100), xlab="F2", ylab="F1",
	type="n", main=paste("Scatterplot of all tokens of ʏ in ", outputfile));

	text( hair$oF2, hair$oF1, labels=hair$location, cex=0.6,  col=c("red", "blue")[hair$gender]);

	points (1387, 400, col="blue", pch=3, cex=3);
	points(1162.02, 511.64, col="green", pch="P", cex=2);
	legend('bottomright', legend="Current residence; men in blue, women in red; blue cross is mean from Rausch 72; 'P' is Patrick's vowel");

dev.off()

#Make F1 - F3 plot
png(paste(outputfile, "F1_F3.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF3, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(f3range[1]-100, f3range[2]+100), xlab="F3", ylab="F1",
	type="n", main=paste("Scatterplot of all tokens of ʏ in ", outputfile));

	text( hair$oF3, hair$oF1, labels=hair$location, cex=0.6, col=c("red", "blue")[hair$gender]);


	points(2093.16, 511.64, col="green", pch="P", cex=2);
	legend('bottomright', legend="Current residence; men in blue, women in red; 'P' is Patrick's vowel");

dev.off()



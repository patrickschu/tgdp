#exploratory plotting after first measurements of all short ue




#Moving parts
setwd('~/Desktop/rplots')
#read the csv file containing measurements
hair=read.csv('/Users/ps22344/Downloads/tgdp/summer16/mapping/gilbertsound_26_shorti.csvgilbertsound_74_shorti.csv_merged.csvgilbertsound_114_shorti.csv_merged.csvgilbertsound_125_shorti.csv_merged.csv', header=T)
summary(hair)
nrow(hair)
#remove the crazy outlier

#TO DO: set limits up here
#Print
tokens=nrow(hair)-summary(hair$oF1)[7]
tokens2=nrow(hair[complete.cases(hair$oF1),])
cat("# of tokens: ", tokens)
cat("# of tokens: ", tokens2)

f1range=range(hair$oF1, na.rm=TRUE);
f2range=range(hair$oF2, na.rm=TRUE);
f3range=range(hair$oF3, na.rm=TRUE);

cat ("Range F1", f1range);
cat ("Range F2", f2range);
cat ("Range F3", f3range);

cat("Means", "\nf1o", mean(hair$oF1, na.rm=TRUE), "\nf2o", mean(hair$oF2, na.rm=TRUE), "\nf3o", mean(hair$oF3, na.rm=TRUE))
cat("Stdevs", "\nf1o", sd(hair$oF1, na.rm=TRUE), "\nf2o", sd(hair$oF2, na.rm=TRUE), "\nf3o", sd(hair$oF3, na.rm=TRUE))


#BY SPEAKER
outputfile='entire dataset by speaker'
#Make F1 - F2 plot
png(paste(outputfile, "F1_F2.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF2, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(1100, f2range[2]+100), xlab="F2", ylab="F1", type="n",
	 main=paste("F1 - F2 Scatterplot of all tokens of ɪ in ", outputfile, ",", tokens, "tokens"));

	text( hair$oF2, hair$oF1, labels=hair$speaker, cex=1,  col=c("red", "blue")[hair$gender]);

	points (1387, 400, col="blue", pch="ʏ", cex=2.5);
	points (2025, 371, col="blue", pch="ɪ", cex=2.5);		
	#points (1635, 404, col="green", pch="T", cex=2)
	points(1162.02, 511.64, col="green", pch="P", cex=2);
	legend('bottomright', legend="Speaker number; men in blue, women in red; blue means from Rausch 72; 'P' is Patrick's vowel", cex=0.9);

dev.off()

#Make F1 - F3 plot
png(paste(outputfile, "F1_F3.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF3, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(f3range[1]-100, f3range[2]+100), xlab="F3", ylab="F1",
	type="n", main=paste("F1 - F3 Scatterplot of all tokens of ɪ in ", ",", tokens, "tokens"));

	text( hair$oF3, hair$oF1, labels=hair$speaker, cex=1, col=c("red", "blue")[hair$gender]);


	points(2521.04, 549, col="green", pch="P", cex=2);
	legend('bottomright', legend="Speaker number; men in blue, women in red; blue cross is mean from Rausch 72; 'P' is Patrick's vowel", cex=0.9);

dev.off()





##BY WORD
outputfile='entire dataset by gilbert sentence'
#Make F1 - F2 plot
png(paste(outputfile, "F1_F2.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF2, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(1100, f2range[2]+100), xlab="F2", ylab="F1",
	type="n", main=paste("F1 - F2 Scatterplot of all tokens of ɪ in ", outputfile, ",", tokens, "tokens"));

	text( hair$oF2, hair$oF1, labels=hair$gilbert_number, cex=1,  col=c("red", "blue")[hair$gender]);1		
	points (1387, 400, col="blue", pch=3, cex=3);
	points(1642.54, 549.01, col="green", pch="P", cex=2);
	legend('bottomright', legend="Target word; men in blue, women in red; blue cross is mean from Rausch 72; 'P' is Patrick's vowel", cex=0.9);

dev.off()

#Make F1 - F3 plot
png(paste(outputfile, "F1_F3.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF3, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(f3range[1]-100, f3range[2]+100), xlab="F3", ylab="F1",
	type="n", main=paste("F1 - F3 Scatterplot of all tokens of ɪ in ", outputfile,",", tokens, "tokens"));

	text( hair$oF3, hair$oF1, labels=hair$gilbert_number, cex=1, col=c("red", "blue")[hair$gender]);

	points(2521.04, 549.01, col="green", pch="P", cex=2);
	legend('bottomright', legend="Target word; men in blue, women in red; blue cross is mean from Rausch 72; 'P' is Patrick's vowel", cex=0.9);

dev.off()

##BY LOCATION
outputfile='entire dataset by location'
png(paste(outputfile, "F1_F2.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF2, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(1100, f2range[2]+100), xlab="F2", ylab="F1", type="n",
	 main=paste("F1 - F2 Scatterplot of all tokens of ɪ in ", outputfile, ",", tokens, "tokens"));

	text( hair$oF2, hair$oF1, labels=hair$location, cex=0.6,  col=c("red", "blue")[hair$gender]);

	points (1387, 400, col="blue", pch="ʏ", cex=2.5);
	points (2025, 371, col="blue", pch="ɪ", cex=2.5);		
	#points (1635, 404, col="green", pch="T", cex=2)
	points(1162.02, 511.64, col="green", pch="P", cex=2);
	legend('bottomright', legend="Current residence; men in blue, women in red; blue means from Rausch 72; 'P' is Patrick's vowel", cex=0.9);

dev.off()

#Make F1 - F3 plot
png(paste(outputfile, "F1_F3.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF3, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(f3range[1]-100, f3range[2]+100), xlab="F3", ylab="F1",
	type="n", main=paste("F1 - F3 Scatterplot of all tokens of ɪ in ", ",", tokens, "tokens"));

	text( hair$oF3, hair$oF1, labels=hair$location, cex=0.6, col=c("red", "blue")[hair$gender]);


	points(2521.04, 549, col="green", pch="P", cex=2);
	legend('bottomright', legend="Current residence; men in blue, women in red; blue cross is mean from Rausch 72; 'P' is Patrick's vowel", cex=0.9);

dev.off()



##Make plot with glides

#Make F1 - F2 plot GLIDES
png(paste(outputfile, "F1_F2glides.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF2, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(1100, f2range[2]+100), xlab="F2", ylab="F1",
	type="n", main=paste("F1 - F2 glides Scatterplot of all tokens of ʏ in ", outputfile));

	text( hair$gF2, hair$gF1, labels=hair$speaker_number,   col=c("red", "blue")[hair$gender]);

	points (1387, 400, col="blue", pch=3, cex=3);
	points (1635, 404, col="green", pch="T", cex=2)
	points(1162.02, 511.64, col="green", pch="P", cex=2);
	legend('bottomright', legend="Current residence; men in blue, women in red; blue cross is mean from Rausch 72; 'P' is Patrick's vowel; 'T' is Tobi's vowel", cex=0.9);

dev.off()

#Make F1 - F3 plot GLIDES
png(paste(outputfile, "F1_F3glides.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF3, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(f3range[1]-100, f3range[2]+100), xlab="F3", ylab="F1",
	type="n", main=paste("F1 - F3 glides Scatterplot of all tokens of ʏ in ", outputfile));

	text( hair$gF3, hair$gF1, labels=hair$speaker_number,  col=c("red", "blue")[hair$gender]);

	points(2403, 404, col="green", pch="T", cex=2)
	points(2093.16, 511.64, col="green", pch="P", cex=2);
	legend('bottomright', legend="Current residence; men in blue, women in red; blue cross is mean from Rausch 72; 'P' is Patrick's vowel; 'T' is Tobi's vowel", cex=0.9);

dev.off()




##THE HISTOGRAMMER

histogrammer = function (formant)
{
	var=hair[complete.cases(hair[,formant]),];
	var=var[,formant];
	histi=hist(var, main = paste("Histogram of ",formant ));
	#this part stolen from http://www.statmethods.net/graphs/density.html
	xfit<-seq(min(var),max(var),length=40) ;
	yfit<-dnorm(xfit,mean=mean(var),sd=sd(var)) ;
	yfit <- yfit*diff(histi$mids[1:2])*length(var) ;
	lines(xfit, yfit, col="blue", lwd=2);
	points(x = mean(var)-2*(sd(var)), y = 1, col="red", cex=3);
	points(x = mean(var)+2*(sd(var)), y = 1, col="red", cex=3);
}


png("shorti_histf3.png")
histogrammer('oF3')
dev.off()


#Patrick's begraebnis vowel: 549.01	1642.54	2521.04
#Patrick's ue in kuerbis F1 is surely mismeasured, ill keep it out 125.66 -->460	1162.02	2093.16
#Patrick's ue: 452.98	1182.29	2337.36
#Patrick's ue in wuermchen: 511.64	1345.00	2258.89	
# tobis_vowels	tobi_kuerbis	8.666	8.771	0.105	8.701	136.35	404.23	1635.08	2403.18	8.736	147.48	431.50	1536.89	2409.24	5500 Hz	10	
# tobis_vowels	tobi_wuermchen	13.932	14.048	0.116	13.971	109.68	414.51	1791.47	2394.90	14.010	109.55	449.18	1045.42	2754.74	5500 Hz	10	
# tobis_vowels	tobi_buerste	29.368	29.368	0	29.368	122.48	472.93	1589.55	2327.85	29.368	122.48	472.93	1589.55	2327.85	5500 Hz	10

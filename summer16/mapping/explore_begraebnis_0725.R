#exploratory plotting after first measurements of lightning bug

#Patrick's begraebnis vowel: 549.01	1642.54	2521.04


#Moving parts
setwd('~/Desktop/rplots')
#read the csv file containing measurements
hair=read.csv('/Users/ps22344/Downloads/tgdp/summer16/gilberttools/gilbertsound_114_shorti.csv', header=T)
outputfile='sentence 114'

#Print
tokens=nrow(hair)-summary(hair$oF1)[7];
cat("# of tokens: ", tokens);
tokens2=nrow(hair[complete.cases(hair$oF1),]);
cat("# of tokens: ", tokens2);

#summary(hair)

f1range=range(hair$oF1, na.rm=TRUE);
f2range=range(hair$oF2, na.rm=TRUE);
f3range=range(hair$oF3, na.rm=TRUE);

cat ("Range F1", f1range);
cat ("Range F2", f2range);
cat ("Range F3", f3range);

cat("Means", "\nf1o", mean(hair$oF1, na.rm=TRUE), "\nf2o", mean(hair$oF2, na.rm=TRUE), "\nf3o", mean(hair$oF3, na.rm=TRUE))
cat("Stdevs", "\nf1o", sd(hair$oF1, na.rm=TRUE), "\nf2o", sd(hair$oF2, na.rm=TRUE), "\nf3o", sd(hair$oF3, na.rm=TRUE))



#Make F1 - F2 plot
png(paste(outputfile, "F1_F2.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF2, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(1100, f2range[2]+100), xlab="F2", ylab="F1",	type="n", main=paste("Scatterplot of all tokens of ɪ in ", outputfile));

	text( hair$oF2, hair$oF1, labels=hair$speaker_number, col=c("red", "blue")[hair$gender]);

	points (1387, 400, col="blue", pch="ʏ", cex=3);
	points (2025, 371, col="blue", pch="ɪ", cex=3);
	points(1642.54, 549.01	, col="green", pch="P", cex=2);
	legend('bottomright', legend="Speaker IDs; men in blue, women in red; blue IPA is mean from Rausch 72; 'P' is Patrick's vowel");

dev.off()

#Make F1 - F3 plot
png(paste(outputfile, "F1_F3.png", sep="_"),  width=960, height=640, res=100);

	plot(hair$oF3, hair$oF1, ylim=c(f1range[1]-50, f1range[2]+30), xlim=c(f3range[1]-100, f3range[2]+100) , xlab="F3", ylab="F1",
	type="n", main=paste("Scatterplot of all tokens of ɪ in ", outputfile));

	text( hair$oF3, hair$oF1, labels=hair$speaker_number, col=c("red", "blue")[hair$gender]);


	points(2521.04, 549, col="green", pch="P", cex=2);
	legend('bottomright', legend="Speaker IDs; men in blue, women in red; 'P' is Patrick's vowel");

dev.off()

histogrammer = function (formant)
{
	var=hair[complete.cases(hair[,formant]),];
	var=var[,formant];
	histi=hist(var, main = paste("Histogram of ",formant ), ylab="Hertz");
	#this part stolen from http://www.statmethods.net/graphs/density.html
	xfit<-seq(min(var),max(var),length=40) ;
	yfit<-dnorm(xfit,mean=mean(var),sd=sd(var)) ;
	yfit <- yfit*diff(histi$mids[1:2])*length(var) ;
	lines(xfit, yfit, col="blue", lwd=2);
	points(x = 410, y = 5);
	points(x = mean(var)-2*(sd(var)), y = 1, col="red", cex=3);
	points(x = mean(var)+2*(sd(var)), y = 1, col="red", cex=3);
}

png("114_histf3.png")
histogrammer('oF3')
dev.off()



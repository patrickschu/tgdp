#exploratory plotting after first measurements of hairbrush

hair=read.csv('/Users/ps22344/Downloads/tgdp/summer16/gilberttools/gilbertsound_16.csv', header=T)
outputfile='sentence16_F1_F2.png'
cat ("Range F1");
range(hair$oF1, na.rm=TRUE);


cat ("Range F2");
range(hair$oF2, na.rm=TRUE);



summary(hair);
png(outputfile,  width=960, height=640, res=100);

plot(hair$oF2, hair$oF1, ylim=c(810, 370), xlim=c(2300,1300), 
type="n", main="Scatterplot of all tokens of /ue/ in sentence 16");

text( hair$oF2, hair$oF1, labels=hair$speaker_number, col=c("red", "blue")[hair$gender]);

points (1387, 400, col="red", pch=3, cex=10);
legend('bottomright', legend="Speaker IDs; men in blue, women in red; blue cross is mean from Rausch 72");

dev.off()
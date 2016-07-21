#exploratoty plotting after first measurements of hairbrush

hair=read.csv('/Users/ps22344/Downloads/tgdp-master/summer16/gilberttools/aseftgregtergtertret.csv', header=T)

cat ("Range F1");
range(hair$oF1, na.rm=TRUE);


cat ("Range F2");
range(hair$oF2, na.rm=TRUE);



summary(hair);
png('buerste_F1_F2.png',  width=960, height=640, res=100);

plot(hair$oF2, hair$oF1, ylim=c(810, 370), xlim=c(2300,1300), 
type="n", main="Scatterplot of all tokens of /ue/ in buerste");

text( hair$oF2, hair$oF1, labels=hair$speaker_number, col=c("red", "blue")[hair$gender]);

points (1387, 400, col="red", lty=2, cex=20);
legend('bottomright', legend="Speaker IDs; men in blue, women in red; blue cross is mean from Rausch 72");

dev.off()
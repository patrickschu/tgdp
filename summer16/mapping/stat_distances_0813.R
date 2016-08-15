disti=read.csv('E:cygwin/home/ps/tgdp/summer16/mapping/distances_0813.csv', header=T)
factorstatter=function (dataset, factor){

for (level in levels(dataset[[factor]])){
	cat ("working on level'", level,"'\n");
	cat ("len initial dataset:", nrow(dataset), "\n");
	disti=dataset[complete.cases(dataset[['oF3_oF1_distance']]),];
	cat ("len dataset complete cases:", nrow(disti), "\n" );
	disti2=disti[disti$gender==level,];
	cat ("len dataset by factor", nrow(disti2), "\n");
	#f3.- F1
	linmod=lm(disti2[['oF3_oF1_distance']]~disti2[['dob']]+ disti2[['location']]+disti2[['gilbert_number']]);
	cat ("\nlinearmodel F3, F1");
	print (summary(linmod));
	#F2 - F1
	linmod=lm(disti2[['oF2_oF1_distance']]~disti2[['dob']]+ disti2[['location']]+disti2[['gilbert_number']]);
	cat ("\nlinearmodel F2, F1") ;
	print (summary(linmod));

	correlation=cor(disti2[['oF3_oF1_distance']],disti2[['oF2_oF1_distance']], method='spearman');
	cat("correlation F1-F2 and F1-F3", level, correlation, "\n")
}
}

factorstatter(disti, 'gender')
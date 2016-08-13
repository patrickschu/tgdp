
#this plots the euclidean distance between vowels
#note that NAs are still in here
setwd('C:/Users/ps/Documents/rplots')
##PER GENDER
levels(disti2[['gender']])
#female

###F1 - F3
factorplotter=function (dataset, factor){

for (level in levels(dataset[[factor]])){
	cat ("working on level'", level,"'\n");
	cat ("len initial dataset:", nrow(dataset), "\n");
	disti=dataset[complete.cases(dataset[['oF3_oF1_distance']]),];
	cat ("len dataset complete cases:", nrow(disti), "\n" );
	disti2=disti[disti$gender==level,];
	cat ("len dataset by factor", nrow(disti2), "\n");
	png(paste("euclid_f1_f3_",factor, level, ".png")); 
	plot(
	disti2[order(disti2$oF3_oF1_distance),]$oF3_oF1_distance,
	type='n', 
	main=paste(
	"Euclidean distance ? to ?, F1-F3, ", factor, ":", level, "speakers:", nrow(disti2)),
	ylim=c(range(disti$oF3_oF1_distance)[1],range(disti$oF3_oF1_distance)[2])
	);
	text(
	disti2[order(disti2$oF3_oF1_distance),]$oF3_oF1_distance, 
	labels=disti2[order(disti2$oF3_oF1_distance),]$speaker_number, cex=0.8
);
	dev.off()
}
}

###F1 - F2
factorplotter=function (dataset, factor){

for (level in levels(dataset[[factor]])){
	cat ("working on level'", level,"'\n");
	cat ("len initial dataset:", nrow(dataset), "\n");
	disti=dataset[complete.cases(dataset[['oF2_oF1_distance']]),];
	cat ("len dataset complete cases:", nrow(disti), "\n" );
	disti2=disti[disti$gender==level,];
	cat ("len dataset by factor", nrow(disti2), "\n");
	png(paste("euclid_f1_f2_",factor, level, ".png")); 
	plot(
	disti2[order(disti2$oF2_oF1_distance),]$oF2_oF1_distance,
	type='n', 
	main=paste(
	"Euclidean distance ? to ?, F1-F2, ", factor, ":", level, "speakers:", nrow(disti2)),
	ylim=c(range(disti$oF2_oF1_distance)[1],range(disti$oF2_oF1_distance)[2])
	);
	text(
	disti2[order(disti2$oF2_oF1_distance),]$oF2_oF1_distance, 
	labels=disti2[order(disti2$oF2_oF1_distance),]$speaker_number, cex=0.8
);
	dev.off()
}
}


#this plots the euclidean distance between vowels
#note that NAs are still in here
setwd('C:/Users/ps/Documents/rplots')
##PER GENDER
levels(disti2[['gender']])
#female

###F1 - F3
factorplotter=function (dataset, factor){

for (level in levels(dataset[[factor]])){
	cat ("working on level'", level,"'\n");
	cat ("len initial dataset:", nrow(dataset), "\n");
	disti=dataset[complete.cases(dataset[['oF3_oF1_distance']]),];
	cat ("len dataset complete cases:", nrow(disti), "\n" );
	disti2=disti[disti$gender==level,];
	cat ("len dataset by factor", nrow(disti2), "\n");
	png(paste("euclid_f1_f3_",factor, level, ".png")); 
	plot(
	disti2[order(disti2$oF3_oF1_distance),]$oF3_oF1_distance,
	type='n', 
	main=paste(
	"Euclidean distance ? to ?, F1-F3, ", factor, ":", level, "speakers:", nrow(disti2)),
	ylim=c(range(disti$oF3_oF1_distance)[1],range(disti$oF3_oF1_distance)[2])
	);
	text(
	disti2[order(disti2$oF3_oF1_distance),]$oF3_oF1_distance, 
	labels=disti2[order(disti2$oF3_oF1_distance),]$speaker_number, cex=0.8
);
	dev.off()
}
}

###ALL Fs
factorplotter=function (dataset, factor){

for (level in levels(dataset[[factor]])){
	cat ("working on level'", level,"'\n");
	cat ("len initial dataset:", nrow(dataset), "\n");
	disti=dataset[complete.cases(dataset[['oF2_oF1_distance']]),];
	cat ("len dataset complete cases:", nrow(disti), "\n" );
	disti2=disti[disti$gender==level,];
	cat ("len dataset by factor", nrow(disti2), "\n");
	png(paste("euclid_allfs_",factor, level, ".png")); 
	plot(
	disti2[order(disti2$oF3_oF1_distance),]$oF3_oF1_distance,
	type='n', 
	main="Euclidean distance ? to ?, F3 to F1: blue and F2 and F1: red", 
	sub=paste(factor, ":", level, "speakers:", nrow(disti2)),
	ylim=c(range(disti$oF3_oF1_distance)[1],range(disti$oF3_oF1_distance)[2])
	);
	text(
	disti2[order(disti2$oF2_oF1_distance),]$oF2_oF1_distance, 
	labels=disti2[order(disti2$oF2_oF1_distance),]$speaker_number, cex=0.8, col='red'
);
	text(
	disti2[order(disti2$oF3_oF1_distance),]$oF3_oF1_distance, 
	labels=disti2[order(disti2$oF3_oF1_distance),]$speaker_number, cex=0.8, col='blue'
);

	dev.off()
}
}


###LABEL BY LOCATION





###LABEL BY DOB
#plotting leaders and losers in F3 distance
setwd('C:/Users/ps/Documents/rplots')


leaders=c(437, 410, 224, 96)
losers=c(88, 98, 147)
#leaderlists
ue=list(c(2177.0549999999998, 448.13999999999999), c(2472.02, 696.77999999999997), c(2329.4899999999998, 471.81999999999999), c(2126.9499999999998, 485.80000000000001))
i=list(c(2833.9549999999999, 547.505), c(3096.5999999999999, 410.98000000000002),c(2965.5166666666664, 448.69666666666666),  c(2780.2833333333328, 568.23000000000002))

#loserlists
ue=list(c(2478.8400000000001, 375.01999999999998), c(2796.8299999999999, 572.21500000000003), c(2280.6500000000001, 385.85000000000002))
i=list(c(2441.0733333333333, 315.01999999999998), c(2760.27, 584.90499999999997), c(2324.2233333333334, 452.49666666666667))

#disti=read.csv('E:cygwin/home/ps/tgdp/summer16/mapping/distances_0813.csv', header=T)
var1=read.csv('E:cygwin/home/ps/tgdp/summer16/mapping/var1_only.csv', header=T)
count=1
for (l in losers)
{
print (l);
print (count);
subsetivar1=var1[var1$speaker_number==l, ];
print ('ue')
print (subsetivar1[['oF3_oF1_coords']]);
subseti=disti[disti$speaker_number==l, ];
print ('i');
print (subseti[['oF3_oF1_coords']]);

png(paste("losers_F1_F3", l, ".png", sep="_"),  width=960, height=640, res=100);

plot(
subseti[['oF1_mean']], subseti[['oF2_mean']],
ylim=c(810, 400), xlim=c(3100,1000), xlab="F3", ylab="F1",,
main=paste("Speaker", l, ",", subseti[['gender']]),
type='n');

points(i[[count]][1],i[[count]][2] , pch="?", cex=1.1);
points(ue[[count]][1],ue[[count]][2], pch="?", cex=1.1);
dev.off();
count=count+1
}
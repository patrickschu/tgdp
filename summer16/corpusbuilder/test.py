import pandas


t={'assi':['1','2','3'],
'name':['patrick','oberassi','unterassi']
}


t2={'assi':['1','2'],
'name':['patrick','oberassi']
}

full=pandas.DataFrame(t)
partial=pandas.DataFrame(t2)
print full
print partial

res=pandas.merge(full, partial, how='inner', on='name')

print "\n\nreulst"
print  res


#regex=9-134-2-2-a.wav
#regex = "(\d+)-(\d+)-(\d+)-(\d+)-(\D+)\.wav"
# thus 
#[0]= iv_number
#[1]= speaker_number
#[2]= ??
#[3]= gilbert_number
#[4] = random alpha character			
# 
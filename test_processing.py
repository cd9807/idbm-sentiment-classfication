import pandas as pd


file = pd.read_csv('E:/python_code/idbm_bert/data/nocut/test_old.tsv',sep='\t',header=None)
for index in file.index:
    #print( file.loc[index][0])
    file.loc[index,0] = 'NA'

file.to_csv('E:/python_code/idbm_bert/data/nocut/test.tsv', columns= None, header=None, index=False, sep = '\t')
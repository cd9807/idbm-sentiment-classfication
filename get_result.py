import os
import pandas as pd

file = pd.read_csv('E:/kaggle/IMDB/nocut/imdb_out/test_results.tsv',sep='\t',header=None)
data = pd.DataFrame(columns=['polarity'])
for index in file.index:
    negative_score = file.loc[index].values[0]
    positive_score = file.loc[index].values[1]
    if max(negative_score, positive_score) == negative_score:
        # data.append(pd.DataFrame([index, "neutral"],columns=['id','polarity']),ignore_index=True)
        data.loc[index + 1] = ["0"]
    elif max(negative_score, positive_score) == positive_score:
        # data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
        data.loc[index + 1] = ["1"]
data.to_csv(os.path.join('E:/kaggle/IMDB/nocut/imdb_out/', "result.tsv"), index=False, sep = '\t')
file =pd.DataFrame
file = pd.read_csv('E:/kaggle/IMDB/nocut/imdb_out/result.tsv', sep='\t', header=None,quoting=1)
file1 = pd.read_csv('E:/python_code/idbm_bert/data/nocut/test_org.tsv', sep='\t', header=None,quoting=1)
a = []
b = []
cnt = 0
for i in file.index:
    res = file.loc[i].values[0]
    a.append(res)
for i in file1.index:
    res = file1.loc[i].values[0]
    b.append(str(res))
a.remove('polarity')

for i in range(2501):
    if a[i] == b[i]:
        cnt += 1
print('测试集中精度为:', cnt / 2501)
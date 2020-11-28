import os
import pandas as pd
from sklearn.utils import shuffle


if __name__ == '__main__':
    path = "E:/python_code/idbm_bert/data/nocut/"
    pd_all = pd.read_csv(os.path.join(path, "labeledTrainData_nocut.tsv"), sep='\t' )
    pd_all = shuffle(pd_all)


    val_set = pd_all.iloc[0:int(pd_all.shape[0] / 10)]
    test_set = pd_all.iloc[int(pd_all.shape[0] / 10):int(pd_all.shape[0] / 5)]
    train_set = pd_all.iloc[int(pd_all.shape[0] / 5): int(pd_all.shape[0])]
    val_set.to_csv("E:/python_code/idbm_bert/data/nocut/val.tsv", index=False, header=None, sep='\t')
    train_set.to_csv("E:/python_code/idbm_bert/data/nocut/train.tsv", index=False, header=None, sep='\t')
    test_set.to_csv("E:/python_code/idbm_bert/data/nocut/test_old.tsv", index=False, header=None, sep='\t')


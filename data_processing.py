import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


stop_words = set(stopwords.words('english'))

sentiment = []
review_new = []
train = pd.read_csv('data/labeledTrainData_org.tsv', header=0, delimiter="\t", quoting=3)#读原始评论
for i in range(25000):
    sentiment.append(str(train['sentiment'][i]))
    cut_review = (re.sub("[^a-zA-Z.]", " ", train['review'][i]))# 将HTML标签、标点等替换为空格去除停用词
    review_token = word_tokenize(cut_review)
    review = [w for w in review_token if not w in stop_words]
    print(review)
    review_new.append(review)
train_new = pd.DataFrame({'sentiment': sentiment, 'review': review_new})
# train_new.to_csv('data/stop/labeledTrainData_stop.tsv',sep='\t', index=False, header=None, encoding='utf-8')
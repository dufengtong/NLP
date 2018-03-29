# -*- coding:utf-8 -*-
from nltk.book import text1
import nltk

nltk.download()
fd1=nltk.FreqDist(text1)
print(fd1.keys())
print("文本总词数：%d"%len(fd1.keys()))

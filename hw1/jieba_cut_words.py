# -*-coding:utf-8-*-
# cut text to words using jieba
# calculating R, P, F value
import jieba
from utils import calculate_PRF, standard_words

with open("express.txt","r") as f:
    origin_text = f.read()

cut_result = jieba.cut(origin_text)
cut_words = list(cut_result)

p, r, f = calculate_PRF(cut_words, standard_words)














# -*-coding:utf-8-*-
# cut text to words using thulac
# calculating R, P, F value
import thulac
import re
from utils import calculate_PRF, standard_words

with open("express.txt","r") as f:
    origin_text = f.read()

thu = thulac.thulac(seg_only=True)
result = thu.cut(origin_text, text=True)
cut_words = re.split(" ", result)

p, r, f = calculate_PRF(cut_words, standard_words)












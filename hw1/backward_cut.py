# -*-coding:utf-8-*-
import re
from utils import calculate_PRF, standard_words

f = open("dict_cn.txt","r")
raws = f.readlines()
f.close()
dic = [re.split(" ",raw)[0] for raw in raws ]
max_len = max([len(word) for word in dic])

f = open("express.txt","r")
sentence = f.read()
f.close()

result_cut=[]
while(1):
	word=sentence[-max_len:]
	if len(word) == 0:
		break
	while(1):
		if word in dic:
			result_cut.append(word)
			sentence = sentence[:-len(word)]
			break
		else:
			word = word[1:]
			if len(word)==1:
				result_cut.append(word)
				sentence = sentence[:-1]
				break
			elif len(word)==0:
				sentence = sentence[:-1]
				break

p, r, f = calculate_PRF(result_cut, standard_words)

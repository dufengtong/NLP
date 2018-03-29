from nltk.book import text1
import matplotlib.pyplot as plt
import nltk
len_fre={}
len_words = [len(w) for w in text1]
for len_word in len_words:
	key=len_fre.keys()
	if str(len_word) in len_fre.keys():
		len_fre["{}".format(len_word)] = len_fre["{}".format(len_word)] + 1
	else:
		len_fre["{}".format(len_word)] = 1
plt.xlabel('word length')
plt.ylabel('word frequency')
plt.title('NLTK word length-frequency plot')
plt.plot(list(map(int,len_fre.keys())),list(map(int,len_fre.values())),"*")
plt.show()


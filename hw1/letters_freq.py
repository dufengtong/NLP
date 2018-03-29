import re
import nltk
from nltk.book import text1
fd1 = nltk.FreqDist(text1)
fre = {}
for letter in 'abcdefghijklmnopqrstuvwxyz':
	words = [w for w in text1 if re.search('{}$'.format(letter), w)]
	fre["{}".format(letter)] = len(words)
print(fre)


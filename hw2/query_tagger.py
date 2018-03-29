import nltk
from nltk.corpus import brown

'''query tagger'''
# get frequence of each word
fd = nltk.FreqDist(brown.words(categories='news'))
# get tagged (word, tag) pairs and frequency of each pair
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
# 100 most frequent words
most_freq_words = [w for (w,n) in fd.most_common(500)]

# start tagging
# use tag of the most frequent (test_word, tag) pair as the tag of test_word
likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
# just tag the 100 most frequent words, left other words untagged
baseline_tagger = nltk.UnigramTagger(model=likely_tags)
print('query tagger result:')
print(baseline_tagger._context_to_tag)

brown_tagged_sents = brown.tagged_sents(categories='news')
print('brown tag ground truth:')
print(brown_tagged_sents)

accuracy = baseline_tagger.evaluate(brown_tagged_sents)
print('query tagger accuracy:%f'%accuracy)
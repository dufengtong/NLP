import nltk
from nltk.corpus import brown
from taggers import reg_exp_tagger, query_tagger


test_word = brown.words(categories='news')
train_word = brown.tagged_words(categories='news')
likely_tags = query_tagger(test_word, train_word)

test_sent = brown.sents(categories='news')
rt = reg_exp_tagger(test_word)
btr = nltk.UnigramTagger(model=likely_tags,backoff=rt)
brown_tagged_sents = brown.tagged_sents(categories='news')
accuracy = btr.evaluate(brown_tagged_sents)
print('combine tagger accuracy:%f'%accuracy)





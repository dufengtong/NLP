import nltk
from taggers import reg_exp_tagger, query_tagger
import thulac

with open("Leipzig10ksents_500.txt","r") as f:
    origin_text = f.read()


# get test words and tag of test words
thu_tag = thulac.thulac()
train_word = thu_tag.cut(origin_text)
test_word = [i[0] for i in train_word]
print('test words:')
print(test_word)
print('train words:')
print(train_word)

# query tagger
likely_tags = query_tagger(test_word, train_word)

# regular expression tagger
rt = reg_exp_tagger(test_word)

# combine tagger
btr = nltk.UnigramTagger(model=likely_tags, backoff=rt)

train_word = [[tuple(i) for i in train_word]]

accuracy = btr.evaluate(train_word)
print('combine tagger accuracy:%f'%accuracy)






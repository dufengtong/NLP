import nltk
from nltk.corpus import brown

'''regular expression tagger'''
patterns = [(r'.*ing$', 'VBG'), # gerunds
            (r'.*ed$', 'VBD'), # simple past
            (r'.*es$', 'VBZ'), # 3rd singular present
            (r'.*ould$', 'MD'), # modals
            (r'.*\'s$', 'NN$'), # possessive nouns
            (r'.*s$', 'NNS'), # plural nouns
            (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
            (r'.*', 'NN')] # nouns (default)]

# get raw sentences from brown corpus
brown_sentences = brown.sents(categories='news')
# get already tagged sentences from brown corpus. (ground truth)
brown_tagged_sents = brown.tagged_sents(categories='news')
print('brown tagged ground truth:')
print(brown_tagged_sents)

# start tagging
rt = nltk.RegexpTagger(patterns)
tag_result = rt.tag(brown_sentences[0])
print('brown tag result using regular expression tagger:')
print(tag_result)
accuracy = rt.evaluate(brown_tagged_sents)
print('regular expression tagger accuracy:%f'%accuracy)
import nltk

def query_tagger(test_words, train_words):
    # get frequence of each word
    fd = nltk.FreqDist(test_words)
    # get tagged (word, tag) pairs and frequency of each pair
    cfd = nltk.ConditionalFreqDist(train_words)
    # 100 most frequent words
    most_freq_words = [w for (w, n) in fd.most_common(500)]

    # start tagging
    # use tag of the most frequent (test_word, tag) pair as the tag of test_word
    likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
    # just tag the 100 most frequent words, left other words untagged
    # baseline_tagger = nltk.UnigramTagger(model=likely_tags)
    # print('query tagger result:')
    # print(baseline_tagger._context_to_tag)
    return likely_tags

def reg_exp_tagger(test_sents):
    '''regular expression tagger'''
    patterns = [(r'.*ing$', 'VBG'),  # gerunds
                (r'.*ed$', 'VBD'),  # simple past
                (r'.*es$', 'VBZ'),  # 3rd singular present
                (r'.*ould$', 'MD'),  # modals
                (r'.*\'s$', 'NN$'),  # possessive nouns
                (r'.*s$', 'NNS'),  # plural nouns
                (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
                (r'.*', 'NN')]  # nouns (default)]

    # start tagging
    reg_exp_tagger = nltk.RegexpTagger(patterns)
    # tag_result = reg_exp_tagger.tag(test_sents)
    # print('brown tag result using regular expression tagger:')
    # print(tag_result)
    return reg_exp_tagger



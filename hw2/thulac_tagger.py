import thulac

# get thulac word part labels
thu=thulac.thulac()
label_dict = thu.cut('将句子从繁体转化为简体')
print('thulac label: ')
print(label_dict)
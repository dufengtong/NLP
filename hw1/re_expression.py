import re

f = open('28885.txt', 'r')

title_p = re.compile('Title:(.*)')
author_p = re.compile('Author:(.*)')
language_p = re.compile('Language:(.*)')
content_start_p = re.compile('CHAPTER I(.*)')
content_end_p = re.compile('(.*)THE END')
lines = f.readlines()
for idx, line  in enumerate(lines):
    title_m = re.search(title_p, line)
    if title_m:
        title = title_m.group(1)
        print('title: %s'%title)
    author_m = re.search(author_p, line)
    if author_m:
        author = author_m.group(1)
        print('author: %s'%author)
    language_m = re.search(language_p, line)
    if language_m:
        language = language_m.group(1)
        print('language: %s'%language)
    content_start_m = re.search(content_start_p, line)
    if content_start_m:
        content_start_idx = idx
    content_end_m = re.search(content_end_p, line)
    if content_end_m:
        content_end_idx = idx
    

print('content: ')
print(''.join(lines[content_start_idx+1:content_end_idx]))

    
        

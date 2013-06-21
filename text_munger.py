import re

def clean_word(str):
    'Returns a string in lowercase with only alphanumerics'
    return re.sub('[^\w]','',str.lower())

def extract_words(str):
    'Extracts words from subtitle, removes tags and non-alphanumerics'
    return [w for w in map(clean_word,str.split()) if w]
import re

def count_words(phrase):
    res = re.sub(r'[^\w\s]', '', phrase)
    words = res.lower().split()
    
    unique_words = set(words)
    words_count = len(unique_words)
    
    print(f'Existem {words_count} palavras únicas, e elas são: {unique_words} ')
    
    
count_words('Frase de teste. No teste, apenas as palavras únicas serão contadas')

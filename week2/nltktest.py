print("Starting script")

import nltk

nltk.download('words')
nltk.download('maxent_ne_chunker')
str = "chief executive officer at Coca Cola while in Madrid"
tokens = nltk.word_tokenize(str)
info = nltk.ne_chunk(nltk.pos_tag(tokens))

print(info)
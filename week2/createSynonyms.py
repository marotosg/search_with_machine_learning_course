import fasttext

#file with main words
fileWords = "/workspace/datasets/fasttext/top_words.txt"
model_filename = "/workspace/datasets/fasttext/title_model.bin"
model = fasttext.load_model(model_filename)

# Using readlines()
file1 = open(fileWords, 'r')
lines = file1.readlines()

# open file in write mode
with open(r'/workspace/datasets/fasttext/synonyms.csv', 'w') as fp:
    for line in lines:
        word = line.rstrip()
        synonyms = model.get_nearest_neighbors(word)
        listSyn = word
        for syn in synonyms:
            listSyn += "," + syn[1]
        fp.write("%s\n" % listSyn)
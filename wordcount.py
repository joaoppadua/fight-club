#! python3
#script for counting words using nltk

import nltk, os, sys

def find(name, path='c:\\Users'):
    for root, dirs, files in os.walk(path):
        if name in files:
            return(os.path.join(root, name))

def tokenMaker(txt):
    stop_words = nltk.corpus.stopwords.words('portuguese')
    global tokens
    tokens = nltk.wordpunct_tokenize(txt)
    clean_tokens = [word.lower() for word in tokens if word.isalpha()]
    clean_tokens = [w for w in clean_tokens if w not in stop_words and len(w) > 3]
    return nltk.Text(clean_tokens)

def wordcount(text):
    counter = dict()
    for word in tokenMaker(text):
        if word in counter:
            counter[word] = counter[word] + 1
        else:
            counter[word] = 1
    sorted_counter = sorted(counter.keys(), key=lambda k: (counter[k], k), reverse=True)
    counterList = [counter[word] for word in sorted_counter]
    return [(word, count) for (word, count) in zip(sorted_counter, counterList)]


if len(sys.argv) > 1:
    filename = ' '.join(sys.argv[1:])
else:
    filename = find(input('Enter a file name: '))

with open(filename, encoding='utf8', errors='ignore') as f:
    data = f.read()

# iterate over return to get a string
big_string = '\n'.join('{} {}'.format(x, y) for (x,y) in wordcount(data)[:100])

with open('C:\\Users\\João Pedro\\Desktop\counter_file.txt', 'w') as file:
    file.write(big_string)
    file.write('\n\ntokens and types:' + '\n' + str(len(tokens)) + ', ' + str(len(set(tokens))))
    file.write('\n\ntype/token ratio: ' + str(len(set(tokens)) / len(tokens)))
#debug
#print(big_string)
#print(wordcount(data))

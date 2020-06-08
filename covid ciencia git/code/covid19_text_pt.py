#Script to linguistically analyze covid19 ad hoc corpus

import nltk, time, linguistics
from nltk.corpus import PlaintextCorpusReader
from nltk.probability import FreqDist

var = input('Do you want stop words removed? ')
if var == 'No' or var == 'no':
    stop = False
else:
    stop = True
#print(stop)

with open('/Users/joaopedropadua/Desktop/covid_pt.txt', 'r', errors='ignore') as f:
    text_data = f.read()
    data = linguistics.clean_txt(text_data, 'portuguese', stop=stop)

#corpus = corpus_maker('/Users/joaopedropadua/Desktop')

fdist = FreqDist(data)
concordance_par = input('What word do you want concordance lines for? ')
print("Fetching data...")
time.sleep(5)
print(f'Data is {len(data)} words long')
print(f'Type-token ratio of data is {len(set(data))/len(data)}.')
time.sleep(2)
print('Most common words:\n', fdist.most_common(50))
time.sleep(10)
print('Main collocations:\n', data.collocation_list())
time.sleep(10)
print('\nConcordances:\n')
data.concordance(concordance_par)


#DEBUGGER:
#print(data.collocation_list())
#print(data.concordance('death'))
#print(data.similar('distancing'))
#rint(corpus.words('covid19.txt'))



#fdist.tabulate()
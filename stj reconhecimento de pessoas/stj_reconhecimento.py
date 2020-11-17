#Script to analyze language from ad hoc corpus from Superior Tribunal de Justiça

import linguistics, nltk
from nltk.lm import MLE
from matplotlib import pyplot as plt
import pandas as pd

#Function to define Bigram probDist
def bigram_generator(word1, condfreqdist, freqdist):
    prob_list = list()
    for word in condfreqdist[word1]:
        bigram_count = condfreqdist[word1][word]
        try:
            prob = bigram_count/freqdist[word1]
        except:
            prob == 0
        prob_list.append((word1 + ' ' + word, prob))
    return sorted(prob_list, key=lambda x: x[1], reverse=True)

with open('corpus_stj_art_226.txt', 'r', encoding='utf-8') as f:
    raw = f.read()
    data_clean = linguistics.clean_txt(raw, 'portuguese')
    data_full = [word.lower() for word in nltk.word_tokenize(raw)]
    data_count = linguistics.clean_txt(raw, 'portuguese', stop=False)
    dataLM = nltk.sent_tokenize(raw)

#Some useful variables
size_full = len(data_full)
size_clean = len(data_count)
type_token, coll, fdist = linguistics.text_basics(data_clean)
TEXT = nltk.Text(data_full)
bgrams = list(nltk.bigrams(data_full))
freq_bgrams = nltk.FreqDist(bgrams) # work on this for a bigram LM
cfd = nltk.ConditionalFreqDist(bgrams)
prob_reconhecimento = bigram_generator('reconhecimento', cfd, fdist)

#Some unigrams for crime types
uni_roubo = fdist['roubo']/size_full
uni_homicidio = fdist['homicídio']/size_full
uni_furto = fdist['furto']/size_full
uni_estupro = fdist['estupro']/size_full
uni_trafico = fdist['tráfico']/size_full
uni_corrupcao = fdist['corrpução']/size_full

#Printing useful data from text
print(f'N for all words is {size_full}\n')
print(f'N for clean corpus is {size_clean}\n')
print(f'Type-token ratio: {type_token}\n')
print('Unigrams for different crime types:')
print(f'\tRoubo: {uni_roubo}')
print(f'\tHomicídio: {uni_homicidio}')
print(f'\tFurto: {uni_furto}')
print(f'\tEstupro: {uni_estupro}')
print(f'\tTráfico de drogas: {uni_trafico}')
print(f'\tCorrupção: {uni_corrupcao}\n')
print(f'Count for "roubo": ', fdist['roubo'], '\n')
print(f'Count for "reconhecimento": ', fdist['reconhecimento'], '\n')
print('Most common bigrams for "reconhecimento"', cfd['reconhecimento'].most_common(10), '\n')
print('Most common bigrams for "roubo"', cfd['roubo'].most_common(10), '\n')
print(f'Bigram probability model for "reconhecimento": {prob_reconhecimento}\n')
print('Bigram probability model for "mera": ', bigram_generator('mera', cfd, fdist), '\n\n')

#Condordance tables
TEXT.concordance('reconhecimento')
TEXT.concordance('recomendação')
TEXT.collocations()

#Bigram plots for key lexical items
cfd.plot(conditions=['reconhecimento'], cumulative=False)

#Creating dataframes for bigrams
data_df=[prob_reconhecimento[i][1] for i in range(len(prob_reconhecimento))]
df_reconhecimento = pd.DataFrame(data=data_df, index=[prob_reconhecimento[i][0] for i in range(len(prob_reconhecimento))], columns=['Probabilidade bigrama'])


#DEBUGGERS AND OTHER 
#df_reconhecimento.to_excel('reconhecimento bigrama.xlsx')
#cfd.plot(conditions=['artigo'], cumulative=False)

#freq_bgrams.plot()
#plt.show()

#print(data_clean[:10])
#print(data_full[:10])
#print(df_reconhecimento.head())
#print('Bigrams for "roubo":', cfd['roubo'].max())
#print('Bigrams for "reconhecimento":', cfd['reconhecimento'].max())
# Script to process Whatsapp data

#! python3

"""
Target message:
"[02/01/2019 17:06:20] MARIO SCANGARELLI: vou providenciar hoje"

"""

import os, pandas as pd, seaborn as sb, matplotlib as plt, re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD


# Functions

def getFile(name, path='C:\\Users'):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def getDateTime(s):
    pattern = "(\[\d\d\/\d\d\/\d\d\d\d \d\d:\d\d:\d\d\])"
    result = re.match(pattern, s)
    if result:
        return True
    return False

def getAuthor(s):
    patterns = [
        '([a-zA-Z]+:)',           
        '([a-zA-Z]+[\s][a-zA-Z]+:)'
    ]    
    pattern = '|'.join(patterns)
    result = re.match(pattern, s)
    if result:
        return True
    return False

def getDataPoint(line):
    splitline = line.split('] ')
    dateTime = splitline[0][1:] # because I have '[text text]' format
    date, time = dateTime.split(' ')
    message = ' '.join(splitline[1:]) 
    if getAuthor(message):
        splitMessage = message.split(': ')
        author = splitMessage[0]
        message = ' '.join(splitMessage[1:])
    else:
        author = None
    return date, time, author, message

def basic_cleaning(dataFrame, category):
    dataFrame[category] = dataFrame[category].str.replace(r'[^a-zA-Z]', ' ')
    dataFrame[category] = dataFrame[category].apply(lambda x: ' '.join([w for w in x.split() if len(w) > 3]))
    dataFrame[category] = dataFrame[category].apply(lambda x: x.lower())
    return dataFrame

def removeStopwords(dataFrame, category):
    stopWords = stopwords.words('portuguese')
    tokenizedDoc = dataFrame[category].apply(lambda x: x.split())
    tokenizedDoc = tokenizedDoc.apply(lambda x: [item for item in x if item not in stopWords])
    detokenizedDoc = list()
    for i in range(len(dataFrame)):
        t = ' '.join(tokenizedDoc[i])
        detokenizedDoc.append(t)
    dataFrame[category] = detokenizedDoc
    return dataFrame

def vectorization(dataFrame, category, num_features):
    global vectorizer
    vectorizer = TfidfVectorizer(max_features=num_features, max_df=0.5, smooth_idf=True)
    X = vectorizer.fit_transform(dataFrame[category])
    return X

def topicModeling(varX, n_components):
    svd_model = TruncatedSVD(n_components=n_components, algorithm='randomized', n_iter=100, random_state=122)
    svd_model.fit(varX)
    return svd_model 
    


name = input('Enter file: ')
filepath = getFile(name)
if filepath == None:
    raise NameError('File not found')
#DEBUGGER: print(filepath)

parsedData = list()

with open(filepath, 'r') as f:
    f.readline()
    messageBuffer = []
    date, time, author = None, None, None
    while True:
        line = f.readline()
        if not line : break
        line = line.strip()
        if getDateTime(line):
            if len(messageBuffer) > 0:
                parsedData.append([date, time, author, ' '.join(messageBuffer)])
            messageBuffer.clear()
            date, time, author, message = getDataPoint(line)
            messageBuffer.append(message)
        else:
            messageBuffer.append(line)

#DEBUGGER: print(parsedData[:20])

df = pd.DataFrame(parsedData, columns=['Date', 'Time', 'Author', 'Message'])
#print(df.head())

#Clean text
df_clean = df #DEBUGGER

df_clean = basic_cleaning(df_clean, 'Message')
df_clean = removeStopwords(df_clean, 'Message')

#print(df_clean.head())
print(df_clean.describe())
t = topicModeling(vectorization(df_clean, 'Message', 9000), 20)
#print(len(t.components_))

terms = vectorizer.get_feature_names()
for i, comp in enumerate(t.components_):
    terms_comp = zip(terms, comp)
    sorted_items = sorted(terms_comp, key=lambda x:x[1], reverse=True)[:7]
    print('Topic '+str(i)+': ')
    for t in sorted_items:
        print(t[0])
    print(' ')

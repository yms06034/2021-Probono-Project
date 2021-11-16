from konlpy.tag import Okt
okt = Okt()

import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def STTTokenize(text): 
    tokenized=okt.morphs(text)
    return tokenized

def STTstopWord(tokenized): 
    stopWords = pd.read_csv('stop_words_new.txt',names = ['words'], encoding='utf-16')
    stopData = np.array(stopWords['words']).tolist()
    stopResult=[]
    for token in tokenized:
      if token not in stopData:
        stopResult.append(token)
    return stopResult

def STTtransform(stopResult, t):
    sequenceData = t.texts_to_sequences(stopResult)
    transformList=[]
    for i in sequenceData:
      for j in i:
        transformList.append(j)

    vocaList=np.array([]) 
    for voca in transformList:
      if voca > 499:
        voca = 499
      vocaList=np.append(vocaList,voca)
    vocaList=np.array([vocaList])

    return vocaList

def STTpadding(vocaList):
    pad = pad_sequences(vocaList, truncating = 'post', maxlen = 500)
    
    return pad

def test(pad,rnn_model):
    predicts=rnn_model.predict(pad[0:1])
    #print(predicts)
    if predicts>0.7:
        return 1
    else:
        return 0

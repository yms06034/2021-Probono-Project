#라이브러리
from konlpy.tag import Okt
okt = Okt()

import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


#STT를 위한 함수들 
#토큰화
def STTTokenize(text): 
    tokenized=okt.morphs(text)
    return tokenized

#불용어 처리
def STTstopWord(tokenized): 
    stopWords = pd.read_csv('stop_words_new.txt',names = ['words'], encoding='utf-16')
    stopData = np.array(stopWords['words']).tolist()
    stopResult=[]
    for token in tokenized:
      if token not in stopData:
        stopResult.append(token)
    return stopResult


#transform + 단어사전 줄이기 
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

#Padding
def STTpadding(vocaList):
    pad = pad_sequences(vocaList, truncating = 'post', maxlen = 500)
    print(pad[0])
    
    return pad

#vptest
def test(pad,rnn_model):
    predicts=rnn_model.predict(pad[0:1])
    print(predicts)
    if predicts>0.5:
        return 1
    else:
        return 0



    

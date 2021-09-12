import Kor_Easy_Data_Augmentation as KEDA
import numpy as np
import pandas as pd

#C:\\Users\\LG\\Desktop\\probono\\textvp.txt
text_data = pd.read_csv("/content/textvp.txt", names=['data', 'label'], sep='|')
#print(text_data[:50])

text_train = text_data['data'].to_numpy()
text_target = text_data['label'].to_numpy()

body=[]

print("data set count : ",end='')

for sample in text_train:
    for n in KEDA.KOR_EDA(sample):
        body.append(n)
print(len(body))
print(body[0])

#lengths = np.array([len(x) for x in body])
#print(np.mean(lengths), np.median(lengths))

'''데이터 정규화 ?????? 표준화??
정규화 = 크기를 같게 만든다
표준화 = 데이터의 범위를 같게 만든다 (maybe)
지금 샘플의 크기가 다 다르니까 . . . 그 크기를 같게!
pad_sequences
토큰으로 나누고, 숫자로 바꾸고, 크기를 정규화 (+어휘사전) ~.~ (+) 불용어처리 
음.... 내가 할 수 있을거같나요 ...'''

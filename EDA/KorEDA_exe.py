import KorEDA as KEDA
import numpy as np
import pandas as pd
#C:\\Users\\LG\\Desktop\\probono\\textvp.txt
#C:\\Users\\LG\\Desktop\\probonoPJ\\vpFiles\yesvp.txt -> 되는거 확인 
text_data = pd.read_csv("/content/yesvp.txt" , names=['data', 'label'], sep='|')
#/content/yesvp.txt

text_train = text_data['data'].to_numpy()
text_target = text_data['label'].to_numpy()

body=[]

print("data set count : ",end='')

for sample in text_train:
    for n in KEDA.KOR_EDA(sample):
        body.append(n)
print(len(body))
print(body[0:1])

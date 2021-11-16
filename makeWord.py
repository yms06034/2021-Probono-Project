from tensorflow.keras.preprocessing.text import Tokenizer
import pickle

t = Tokenizer()

with open("./stopWordsOutput.txt", "rb") as f:
	readTxt = pickle.load(f)

t.fit_on_texts(readTxt)
f.close()

def loadW():
	return t

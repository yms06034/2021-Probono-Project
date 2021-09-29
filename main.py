import preprocessing as prep
import Engine as en
import ETRI_STT as STTAPI
import STTPPver2 as STT


#preprocessing
yesA=prep.yesAug("C:\\Users\\LG\\Desktop\\probonoPJ\\vpFiles\yesvp.txt")
notA=prep.notAug("C:\\Users\\LG\\Desktop\\probonoPJ\\vpFiles\notvp.txt")
comb=prep.combine(yesA,notA)

targetData=prep.target()

tokenized=prep.Tokenized(comb)
stop_words=prep.stopWords(tokenized)
word_dic,word_text=prep.wordDic(stop_words)
pad=prep.padding(word_text)
x_train, x_val, x_test, y_train, y_val, y_test=prep.split(pad, targetData)


#Engine
rnn_model=en.engine(x_train, x_val, y_train, y_val)

#ETRI_STT
text=''
string = STTAPI.stt("/content/VOICETEST1.wav")
text = text+string
string = STTAPI.stt("/content/VOICE-TEST-2.wav")
text = text+string
string = STTAPI.stt("/content/VOICE-TEST-3.wav")
text = text+string



#STTPPver2
STTtokenize=STT.STTTokenize(text)
STTstop_word=STT.STTstopWord(STTtokenize)
STTtrans=STT.STTtransform(STTstop_word, word_dic)
STTpad=STT.STTpadding(STTtrans)

STTtest=STT.test(STTpad,rnn_model)

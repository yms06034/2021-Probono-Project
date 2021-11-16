import preprocessing as prep
import model as md
import ETRI_STT as STTAPI
import STTpreprocessing as STTprep


#preprocessing
yesA=prep.yesAug("C:\\Users\\LG\\Desktop\\probonoPJ\\vpFiles\yesvp.txt")
notA=prep.notAug("C:\\Users\\LG\\Desktop\\probonoPJ\\vpFiles\notvp.txt")
comb=prep.combine(yesA,notA)
print("complete combine!")
targetData=prep.target()

tokenized=prep.Tokenized(comb)
print("complete tokenized!")
stop_words=prep.stopWords(tokenized)
print("complete stop words!")
word_dic,word_text=prep.wordDic(stop_words)
pad=prep.padding(word_text)
print("complete padding!")
x_train, x_val, x_test, y_train, y_val, y_test=prep.split(pad, targetData)


#model
rnn_model=md.engine(x_train, x_val, y_train, y_val)
print("complete learning!")

#ETRI_STT
print("START Speech to Text!")
text=''
string = STTAPI.stt("/content/VOICETEST1.wav")
text = text+string
string = STTAPI.stt("/content/VOICETEST2.wav")
text = text+string
string = STTAPI.stt("/content/VOICETEST3.wav")
text = text+string
print("complete Speech to Text!")


#STTpreprocessing
print("START STT Preprocessing!")
STTtokenize=STTprep.STTTokenize(text)
STTstop_word=STTprep.STTstopWord(STTtokenize)
STTtrans=STTprep.STTtransform(STTstop_word, word_dic)
STTpad=STTprep.STTpadding(STTtrans)

STTtest=STTprep.test(STTpad,rnn_model)

if STTtest==1:
    print("=====WARNING=====")
else:
    print("it's okay^^ Don't worry~")
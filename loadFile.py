import pickle

def A():
	with open('./textDataOutput.txt', 'rb') as f:
		one = pickle.load(f)

	with open('./targetDataOutput.txt', 'rb') as f:
		two = pickle.load(f)

	f.close()
	return one, two

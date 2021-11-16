import numpy as np

index = np.arange(20052)
np.random.shuffle(index)

trainIndex = index[:10026]
valIndex = index[10026:16042]
testIndex = index[16042:]

def B(text, target):
	x_train = []; x_val=[]; x_test = []
	y_train=[]; y_val=[]; y_test = []
	for i in trainIndex:
		x_train.append(text[i])
		y_train.append(target[i])
	for j in valIndex:
		x_val.append(text[j])
		y_val.append(target[j])
	for k in testIndex:
		x_test.append(text[k])
		y_test.append(target[k])

	x_train = np.array(x_train)
	x_val = np.array(x_val)
	x_test = np.array(x_test)
	y_train = np.array(y_train)
	y_val = np.array(y_val)
	y_test = np.array(y_test)

	return  x_train, x_val, x_test, y_train, y_val, y_test

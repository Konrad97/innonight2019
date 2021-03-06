from numpy.random import seed
seed(1)
from tensorflow import set_random_seed
set_random_seed(2)

#Importing Libraries for data preparation
import pandas as pd
import numpy as np
import datetime
import os
import time
#Read Necessary files

from keras import Sequential
from keras.layers import Dense, BatchNormalization, Dropout
from keras.callbacks import TensorBoard, EarlyStopping
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler, RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def encode(data, to_encode):
	le = LabelEncoder()
	data[to_encode + '_encoded'] = le.fit_transform(data[to_encode])

	ohe = OneHotEncoder()
	X = ohe.fit_transform(data[to_encode].values.reshape(-1,1)).toarray()

	dfOneHot = pd.DataFrame(X, columns = [to_encode+str(int(i)) for i in range(X.shape[1])])
	data = pd.concat([data, dfOneHot], axis=1)

	del data[to_encode]
	return data

def scale(data):
	mms = RobustScaler()
	return mms.fit_transform(data)


def load(file):

	fullData = pd.read_csv(file)

	fullData = encode(fullData, 'job')
	fullData = encode(fullData, 'marital')
	fullData = encode(fullData, 'education')
	fullData = encode(fullData, 'default')
	fullData = encode(fullData, 'housing')
	fullData = encode(fullData, 'loan')
	fullData = encode(fullData, 'contact')
	fullData = encode(fullData, 'day')
	fullData = encode(fullData, 'month')
	#del fullData['day']
	#del fullData['month']
	fullData = encode(fullData, 'poutcome')


	res = fullData['deposit']

	del fullData['deposit']

	fullData = scale(fullData)

	le = LabelEncoder()
	res = le.fit_transform(res)

	return [fullData, res]


fullData, res = load("dataset.csv")

print (res)
print(fullData)

train_x, test_x, train_y, test_y = train_test_split(fullData, res, test_size=0.2, random_state=42, shuffle=True)

model = Sequential()
model.add(Dense(100, input_dim=len(fullData[0]), activation= "relu"))
model.add(Dropout(0.2))

model.add(Dense(100, activation= "relu"))
model.add(Dropout(0.2))

model.add(Dense(50, activation= "relu"))
model.add(Dropout(0.2))

model.add(Dense(1, activation= "sigmoid"))
model.summary()

# Compile model
model.compile(loss= "binary_crossentropy" , optimizer="adagrad", metrics=["accuracy"])

ts = time.time()
time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H-%M-%S')

tensorboard = TensorBoard(log_dir=os.path.join('tb', time), histogram_freq=0, write_graph=True, write_images=True)

stop = EarlyStopping(monitor='val_loss', min_delta=0, patience=5, verbose=0, mode='auto', baseline=None, restore_best_weights=True)

model.fit(train_x, train_y, epochs=200000, validation_data=(test_x, test_y), callbacks=[tensorboard, stop])

# Use the load function to load the csv
# Use the model to run the inference




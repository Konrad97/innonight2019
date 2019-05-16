from numpy.random import seed
seed(1)
from tensorflow import set_random_seed
set_random_seed(2)

#Importing Libraries for data preparation
import pandas as pd
import numpy as np

#Read Necessary files
fullData = pd.read_csv("dataset.csv")

from keras import Sequential
from keras.layers import Dense, BatchNormalization
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#del fullData['duration']

def encode(data, to_encode):
	le = LabelEncoder()
	data[to_encode + '_encoded'] = le.fit_transform(data[to_encode])

	ohe = OneHotEncoder()
	X = ohe.fit_transform(data[to_encode].values.reshape(-1,1)).toarray()

	dfOneHot = pd.DataFrame(X, columns = [to_encode+str(int(i)) for i in range(X.shape[1])])
	data = pd.concat([data, dfOneHot], axis=1)

	del data[to_encode]
	return data

fullData = encode(fullData, 'job')
fullData = encode(fullData, 'marital')
fullData = encode(fullData, 'education')
fullData = encode(fullData, 'default')
fullData = encode(fullData, 'housing')
fullData = encode(fullData, 'loan')
fullData = encode(fullData, 'contact')
fullData = encode(fullData, 'day')
fullData = encode(fullData, 'month')
fullData = encode(fullData, 'poutcome')

def scale(data):
	mms = MinMaxScaler()
	return mms.fit_transform(data)

res = fullData['deposit']

del fullData['deposit']

fullData = scale(fullData)

le = LabelEncoder()
res = le.fit_transform(res)

print (res)
print(fullData)

train_x, test_x, train_y, test_y = train_test_split(fullData, res, test_size=0.2, random_state=42, shuffle=True)

model = Sequential()
model.add(Dense(100, input_dim=len(fullData[0]), activation= "relu"))
model.add(BatchNormalization())
model.add(Dense(100, activation= "relu"))
model.add(BatchNormalization())
model.add(Dense(50, activation= "relu"))
model.add(BatchNormalization())
model.add(Dense(1, activation= "sigmoid"))
model.summary()

# Compile model
model.compile(loss= "binary_crossentropy" , optimizer="adam", metrics=["accuracy"])

model.fit(train_x, train_y, epochs=1)


pred= model.predict_classes(test_x)
score = accuracy_score(test_y,pred)
print (score)

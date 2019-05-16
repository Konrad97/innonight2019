import numpy as np
from sklearn import preprocessing
from numpy import array
from numpy import argmax
from keras.utils import to_categorical
from enum_marital

class Prepare:

	def prepare(self, data):
		#self._norm(self, data)
		#self._binary(self, data)
		self._one_hot()

	def _norm(self, data):
		data[0] = preprocessing.normalize([data[0]])		# age
		data[5] = preprocessing.normalize([data[5]])		# balance
		data[11] = preprocessing.normalize([data[11]])	# duration
		data[12] = preprocessing.normalize([data[12]])	# campaign
		data[13] = preprocessing.normalize([data[13]])	# pdays
		data[14] = preprocessing.normalize([data[14]])	# previous

	#def _binary(self, data):

	def _one_hot(self):
		data = [['married', 'single', 'divorced', 'married', 'married', 'single', 'single', 'single', 'married', 'single'],['secondary', 'secondary','primary', 'secondary','primary', 'tertiary', 'primary', 'unknown']]

		#marital
		for int i in data[2]{
			data[2][i]=enum_marital(data[2][i])
		}

		#education
		for int i in data[2]{
			if(data[2][i]=="primary"){
				data[2][i]=0
			}
			else if(data[2][i]== "secundary"){
				data[2][i]=1
			}
			else if(data[2][i]== "tertiary"){
				data[2][i]=2
			}
			else {
				data[2][i]=3
			}
		}
		
		#data = array(data)

		data1 = array(data[0])
		data2 = array(data[1])

		#transform data in int
		labelEncoder = preprocessing.LabelEncoder()
		trafomed_label1 = labelEncoder.fit_transform(data1)
		trafomed_label2 = labelEncoder.fit_transform(data2)
		print(trafomed_label1)

		# one hot encode
		encoded1 = to_categorical(trafomed_label1)
		encoded2 = to_categorical(trafomed_label2)
		print(encoded1)
		print(encoded2)

		# invert encoding (gibt hinterlegten Wert aus Vektor zurück)
		#inverted = argmax(encoded[0])
		
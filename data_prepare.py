import numpy as np
from sklearn import preprocessing
from numpy import array
from numpy import argmax
from keras.utils import to_categorical

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
		#data = array(data)

		data1 = array(data[0])
		data2 = array(data[1])
		# one hot encode
		encoded1 = to_categorical(data1)
		encoded2 = to_categorical(data2)
		print(encoded1)
		print(encoded2)

		# invert encoding (gibt hinterlegten Wert aus Vektor zurück)
		#inverted = argmax(encoded[0])
		
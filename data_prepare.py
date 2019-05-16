from numpy import array
from numpy import argmax
from keras.utils import to_categorical

class Prepare:

	def prepare(self, data):
		self._norm(self, data)
		self._binary(self, data)
		self._one_hot(self, data)

	def _norm(self, data):

	def _binary(self, data):

	def _one_hot(self, data):
		#data = [1, 3, 2, 0, 3, 2, 2, 1, 0, 1]
		#data = array(data)

		# one hot encode
		encoded = to_categorical(data)

		# invert encoding
		inverted = argmax(encoded[0])
		
import numpy as np
from sklearn import preprocessing

class Prepare:

	def prepare(self, data):
		self._norm(self, data)
		self._binary(self, data)
		self._one_hot(self, data)

	def _norm(self, data):
		data[0] = preprocessing.normalize([data[0]])		# age
		data[5] = preprocessing.normalize([data[5]])		# balance
		data[11] = preprocessing.normalize([data[11]])	# duration
		data[12] = preprocessing.normalize([data[12]])	# campaign
		data[13] = preprocessing.normalize([data[13]])	# pdays
		data[14] = preprocessing.normalize([data[14]])	# previous

	def _binary(self, data):

	def _one_hot(self, data):
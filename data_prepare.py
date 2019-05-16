import numpy as np
from sklearn.basepreprocessing import minmax_scale
from numpy import array
from numpy import argmax
from keras.utils import to_categorical

class Prepare:

	def prepare(self, data):
		self._norm(data)
		#self._binary(self, data)
		self._one_hot()

	def _norm(self, data):
		data[0] = minmax_scale(data[0])		#age
		data[5] = minmax_scale(data[5])		#balance
		data[11] = minmax_scale(data[11])	#campaign
		data[12] = minmax_scale(data[12])	#pdays
		data[13] = minmax_scale(data[13])	#previous
		data[0] = preprocessing.normalize([data[0]])	# age
		data[5] = preprocessing.normalize([data[5]])	# balance
		data[12] = preprocessing.normalize([data[11]])	# campaign
		data[13] = preprocessing.normalize([data[12]])	# pdays
		data[14] = preprocessing.normalize([data[13]])	# previous

	def _binary(self, data):
		self._binary_para(self,data,6) #default
		self._binary_para(self,data,8) #housing
		self._binary_para(self,data,9) #loan
	def _binary_para(self,data,col):
		for int i in data[col]:	# is yes or no
			if data[col][i] == "no" :
				data[col][i]=b
			else :
				data[col][i]=b

	def _one_hot(self):
		data = [['married', 'single', 'divorced', 'married', 'married', 'single', 'single', 'single', 'married', 'single'],['secondary', 'secondary','primary', 'secondary','primary', 'tertiary', 'primary', 'unknown']]
		job = 1
		mari = 2
		edu = 3
		con = 8
		day = 9
		mon = 10
		pou = 14
		#job
		for int i in data[job]	for int i in data[job]:
			if(data[job][i]=="admin."):
				data[job][i]=0
			
			else if(data[job][i]== "blue-collar"):
				data[job][i]=1
			
			else if(data[job][i]== "entrepreneur"):
				data[job][i]=2
			
			else if(data[job][i]== "housemaid"):
				data[job][i]=3
			
			else if(data[job][i]== "management"):
				data[job][i]=4
			
			else if(data[job][i]== "retired"):
				data[job][i]=5
			
			else if(data[job][i]== "self-employed"):
				data[job][i]=6
			
			else if(data[job][i]== "services"):
				data[job][i]=7
			
			else if(data[job][i]== "student"):
				data[job][i]=8
			
			else if(data[job][i]== "technician"):
				data[job][i]=9
			
			else if(data[job][i]== "services"):
				data[job][i]=10
			
			else if(data[job][i]== "unemployed"):
				data[job][i]=11
			
			else :
				data[job][i]=12
			
		encodedJob = self._encode(data[job])

		#marital
		for int i in data[mari]	for int i in data[mari]:
			if(data[mari][i]=="married"):
				data[mari][i]=0
			
			else if(data[mari][i]== "single"):
				data[mari][i]=1
			
			else :
				data[mari][i]=2
			
		encodedMari = self._encode(data[mari])

		#education
		for int i in data[edu]:
			if(data[edu][i]=="primary"):
				data[edu][i]=0
			
			else if(data[edu][i]== "secundary"):
				data[edu][i]=1
			
			else if(data[edu][i]== "tertiary"):
				data[edu][i]=2
			
			else :
				data[edu][i]=3
			
		encodedEdu = self._encode(data[edu])
		
		#contact
		for int i in data[con]:
			if(data[con][i]=="telephone"):
				data[con][i]=0
			
			else if(data[con][i]== "cellular"):
				data[con][i]=1
			
			else :
				data[con][i]=2
			
		encodedCon = self._encode(data[con])

		#day
		encodedDay = self._encode(data[day])

		#month
		for int i in data[mon]	for int i in data[mon]:
			if(data[mon][i]=="jan"):
				data[mon][i]=0
			
			else if(data[mon][i]== "feb"):
				data[mon][i]=1
			
			else if(data[mon][i]== "mar"):
				data[mon][i]=2
			
			else if(data[mon][i]== "apr"):
				data[mon][i]=3
			
			else if(data[mon][i]== "may"):
				data[mon][i]=4
			
			else if(data[mon][i]== "jun"):
				data[mon][i]=5
			
			else if(data[mon][i]== "jul"):
				data[mon][i]=6
			
			else if(data[mon][i]== "aug"):
				data[mon][i]=7
			
			else if(data[mon][i]== "sep"):
				data[mon][i]=8
			
			else if(data[mon][i]== "oct"):
				data[mon][i]=9
			
			else if(data[mon][i]== "nov"):
				data[mon][i]=10
			
			else :
				data[mon][i]=11
			
		encodedMon = self._encode(data[mon])

		#poutcome
		for int i in data[pou]:
			if(data[pou][i]=="failure"):
				data[pou][i]=0
			
			else if(data[pou][i]== "other"):
				data[pou][i]=1
			
			else if(data[pou][i]== "success"):
				data[pou][i]=2
			
			else :
				data[pou][i]=3
			
		encodedPou = self._encode(data[pou])


		data1 = array(data[0])
		data2 = array(data[1])

	def _encode(data):
		# one hot encode
		onehot_encoded = list()
		for value in data:
			zahl = [0 for _ in range(32)]
			zahl[value] = 1
			onehot_encoded.append(zahl)
		print(onehot_encoded)

		
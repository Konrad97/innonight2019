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
				data[job][i]=a
			
			else if(data[job][i]== "blue-collar"):
				data[job][i]=b
			
			else if(data[job][i]== "entrepreneur"):
				data[job][i]=c
			
			else if(data[job][i]== "housemaid"):
				data[job][i]=d
			
			else if(data[job][i]== "management"):
				data[job][i]=e
			
			else if(data[job][i]== "retired"):
				data[job][i]=f
			
			else if(data[job][i]== "self-employed"):
				data[job][i]=g
			
			else if(data[job][i]== "services"):
				data[job][i]=h
			
			else if(data[job][i]== "student"):
				data[job][i]=i
			
			else if(data[job][i]== "technician"):
				data[job][i]=j
			
			else if(data[job][i]== "services"):
				data[job][i]=k
			
			else if(data[job][i]== "unemployed"):
				data[job][i]=l
			
			else :
				data[job][i]=m
			
		encodedJob = to_categorical(data[job])



		#marital
		for int i in data[mari]	for int i in data[mari]:
			if(data[mari][i]=="married"):
				data[mari][i]=a
			
			else if(data[mari][i]== "single"):
				data[mari][i]=b
			
			else :
				data[mari][i]=c
			
		
		encodedMari = to_categorical(data[mari])

		#education
		for int i in data[edu]:
			if(data[edu][i]=="primary"):
				data[edu][i]=a
			
			else if(data[edu][i]== "secundary"):
				data[edu][i]=b
			
			else if(data[edu][i]== "tertiary"):
				data[edu][i]=c
			
			else :
				data[edu][i]=d
			
		
		encodedEdu = to_categorical(data[edu])
		
		#contact
		for int i in data[con]:
			if(data[con][i]=="telephone"):
				data[con][i]=a
			
			else if(data[con][i]== "cellular"):
				data[con][i]=b
			
			else :
				data[con][i]=c
			
		
		encodedCon = to_categorical(data[con])

		#day
		encodedDay = to_categorical(data[day])

		#month
		for int i in data[mon]	for int i in data[mon]:
			if(data[mon][i]=="jan"):
				data[mon][i]=a
			
			else if(data[mon][i]== "feb"):
				data[mon][i]=b
			
			else if(data[mon][i]== "mar"):
				data[mon][i]=c
			
			else if(data[mon][i]== "apr"):
				data[mon][i]=d
			
			else if(data[mon][i]== "may"):
				data[mon][i]=e
			
			else if(data[mon][i]== "jun"):
				data[mon][i]=f
			
			else if(data[mon][i]== "jul"):
				data[mon][i]=g
			
			else if(data[mon][i]== "aug"):
				data[mon][i]=h
			
			else if(data[mon][i]== "sep"):
				data[mon][i]=i
			
			else if(data[mon][i]== "oct"):
				data[mon][i]=j
			
			else if(data[mon][i]== "nov"):
				data[mon][i]=k
			
			else :
				data[mon][i]=l
			
		
		encodedMon = to_categorical(data[mon])

		#poutcome
		for int i in data[pou]:
			if(data[pou][i]=="failure"):
				data[pou][i]=a
			
			else if(data[pou][i]== "other"):
				data[pou][i]=b
			
			else if(data[pou][i]== "success"):
				data[pou][i]=c
			
			else :
				data[pou][i]=d
			
		encodedPou = to_categorical(data[pou])


		data1 = array(data[0])
		data2 = array(data[1])

		zahlen = 'abcdefghijklmno'
		# one hot encode
		onehot_encoded = list()
		for value in integer_encoded:
			letter = [0 for _ in range(len(zahlen))]
			letter[value] = 1
			onehot_encoded.append(letter)
		print(onehot_encoded)

		
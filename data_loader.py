import pandas as pd

class Loader:

	def __init__(self):
		
	def load_csv(self, name: str):
		# return raw array/objectarray
		string = name + '.csv'
		input = pd.read_csv(string)
		print(input)
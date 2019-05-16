import numpy as np
import pandas as pd

class Loader:

#	def __init__(self):
		
	def load_csv(self, name: str):
		# return raw array/objectarray
		df = pd.read_csv('dataset.csv', usecols=['age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome', 'deposit'])
		term_deposits = df.copy()
		
		# Have a grasp of how our data looks.
		df.head()
		return df.to_numpy().transpose()
		
import pandas as pd


class DatasetManager():

	def __init__(self, file_name, delimiter=','):
		self.dataset = pd.read_csv(file_name, delimiter=delimiter)
		print('Read '+file_name+" with "+str(self.dataset.shape[0])+" rows!")
		print("\n")

	def adjust_columns(self):
		'''replace the 'Close' with 'Adj Close' '''
		self.dataset['Close'] = self.dataset['Adj Close'];del(self.dataset['Adj Close'])

		'''changing column names to lower case '''
		self.lower_column_names()
		
		self.dataset['daily_variance'] = (self.dataset['high']-self.dataset['low'])/self.dataset['low']*100
		self.dataset['daily_perfomance'] = (self.dataset['close']-self.dataset['open'])/self.dataset['open']*100
		

		if self.dataset.isna().sum().sum()>0:
			print('Filling NaN with 0!')
			self.dataset.fillna(0, inplace=True)

		self.dataset.set_index('date', inplace=True)
		
	def lower_column_names(self):
		self.dataset['date']=self.dataset['Date']; del(self.dataset['Date'])
		self.dataset['open']=self.dataset['Open']; del(self.dataset['Open'])
		self.dataset['high']=self.dataset['High']; del(self.dataset['High'])
		self.dataset['low']=self.dataset['Low']; del(self.dataset['Low'])
		self.dataset['close']=self.dataset['Close']; del(self.dataset['Close'])
		self.dataset['volume']=self.dataset['Volume']; del(self.dataset['Volume'])

	def delete_columns(self, column_list):
		for column in column_list:
			del(self.dataset[column])

	def print(self, count=11):
		print(self.dataset.head(count))
		print(".\n.\n.\n")
		print(self.dataset.tail(count))

	def build(self, offset=10):
		label_column='close'
		self.dataset['label']=self.dataset[label_column].shift(-offset)
		self.dataset.dropna(inplace=True)

def main():
	dataset=DatasetManager('googl.csv')
	dataset.adjust_columns()
	dataset.delete_columns(['open','high', 'low'])		
	dataset.build()

if __name__=="__main__":
	main()
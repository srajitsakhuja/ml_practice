import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import svm
from dataset_manager import DatasetManager

class Estimator():

	def __init__(self, dataset_manager):
		self.dataset=dataset_manager.dataset

	def separate_labels(self):
		self.x=np.array(self.dataset.drop(['label'], axis=1))
		self.y=np.array(self.dataset['label'])
		assert(self.x.shape[0]==self.y.shape[0])
	
	def scale_dataset(self):
		self.x=preprocessing.scale(self.x)

	def split_dataset(self, test_size):
		self.train_x, self.test_x, self.train_y, self.test_y=train_test_split(self.x, self.y, test_size=test_size)
		assert(self.train_x.shape[0]==self.train_y.shape[0])
		assert(self.test_x.shape[0]==self.test_y.shape[0])
		
	def train(self, classifier="linear_regression"):
		if classifier=='linear_regression':
			self.clf=LinearRegression()
		elif classifier=='svm':
			self.clf=svm.SVR(kernel='poly')
		self.clf.fit(self.train_x, self.train_y)

	def test(self, print_comparison=False):
		self.prediction=self.clf.predict(self.test_x)
		self.score=self.clf.score(self.test_x, self.test_y)

		if print_comparison:
			for (predicted, actual) in zip(self.prediction, self.test_y):
				print(round(predicted,2), round(actual,2), round(abs(predicted-actual),2))
		
		return self.score, self.prediction

	def build(self, test_size=0.25):
		self.separate_labels()
		self.scale_dataset()
		self.split_dataset(test_size)

def main():
	dataset_manager=DatasetManager('googl.csv')
	dataset_manager.adjust_columns()
	dataset_manager.delete_columns(['open','high', 'low'])		
	dataset_manager.build_labels(offset=1)

	estimator=Estimator(dataset_manager)
	estimator.build(0.2)
	estimator.train()
	print(estimator.test())
if __name__=="__main__":
	main()
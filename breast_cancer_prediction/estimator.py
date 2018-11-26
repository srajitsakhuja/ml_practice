import numpy as np
from dataset_manager import DatasetManager
from sklearn.model_selection import train_test_split
from sklearn import neighbors

class Estimator():

	def __init__(self, dataset_manager):
		self.dataset_manager=dataset_manager

	def print(self):
		self.dataset_manager.print()

	def build(self, test_size=0.25):
		self.separate_labels()
		self.train_test_split(test_size)

	def separate_labels(self):
		self.x=np.array(self.dataset_manager.dataset.drop('label', axis=1))
		self.y=np.array(self.dataset_manager.dataset['label'])
		assert(self.x.shape[0]==self.y.shape[0])

	def train_test_split(self, test_size):
		self.train_x, self.test_x, self.train_y, self.test_y=train_test_split(self.x, self.y, test_size=test_size)

	def train(self):
		self.classifier=neighbors.KNeighborsClassifier()
		self.classifier.fit(self.train_x, self.train_y)

	def test(self, x=[], y=[]):
		if len(x)==0 or len(y)==0:
			x=self.test_x
			y=self.test_y

		print(self.classifier.score(x, y))

def main():
	dataset_manager=DatasetManager('breast_cancer_data.txt', columns=['id', 
											'clump_thickness', 
											'cell_size', 
											'cell_shape', 
											'adhesion', 
											'epi_cell_size', 
											'bare_nuc','bland_chrom', 
											'normal_nuc', 
											'mitoses', 
											'label'])
	estimator=Estimator(dataset_manager)
	estimator.build()
	estimator.train()
	estimator.test()

if __name__=="__main__":
	main()
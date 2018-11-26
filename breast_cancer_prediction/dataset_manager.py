import pandas as pd


class DatasetManager():
	def __init__(self, file_name, columns=[], delimiter=","):
		'''read dataset'''
		self.dataset=pd.read_csv(file_name, delimiter=delimiter)

		'''set column names'''
		if len(columns)==self.dataset.shape[1]:
			self.dataset.columns=columns

		self.dataset.drop('id', inplace=True, axis=1)
		self.dataset.replace('?', 0, inplace=True)
		
		self.print()
		print("\nRead "+file_name+" with "+str(self.dataset.shape[0])+" rows!\n\n")

	def print(self, limit=5):
		print(self.dataset.head(limit))

	def explore(self):
		print(self.dataset.describe().loc[['min', 'max', 'mean', 'count']])

		print("\n\n")
		
		for col in self.dataset.columns:
			print(self.dataset[col].value_counts()[:4])
			print("NULL VALUES:"+str(self.dataset[col].isnull().sum()))
			print("\n\n")

def main():
	dataset_manager=DatasetManager('breast_cancer_data.txt', 
									columns=['id', 
											'clump_thickness', 
											'cell_size', 
											'cell_shape', 
											'adhesion', 
											'epi_cell_size', 
											'bare_nuc','bland_chrom', 
											'normal_nuc', 
											'mitoses', 
											'label'])
	dataset_manager.explore()

if __name__=='__main__':
	main()
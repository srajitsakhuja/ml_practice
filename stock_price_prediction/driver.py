from dataset_manager import DatasetManager
from estimator import Estimator
from pprint import pprint
from plotter import Plotter


def main():
	dataset_manager=DatasetManager('googl.csv')
	dataset_manager.adjust_columns()
	dataset_manager.delete_columns(['open','high', 'low'])
	dataset_manager.build()

	estimator=Estimator(dataset_manager)
	estimator.build(0.2)
	estimator.train('linear_regression')
	accuracy, prediction=estimator.test()
	
	plotter=Plotter(estimator)

if __name__=="__main__":
	main()

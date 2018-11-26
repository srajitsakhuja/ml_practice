import matplotlib.pyplot as plt
from matplotlib import style

class Plotter():

	def __init__(self,estimator):
		print(estimator.test_y.shape)
		self.estimator=estimator
		style.use('ggplot')
		# plt.plot(estimator.test_y)
		# plt.plot(estimator.prediction)
		# plt.show()
		estimator.dataset['label'].plot()
		plt.legend(loc=4)
		plt.xlabel('Date')
		plt.show()
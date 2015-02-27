import numpy as np

a = np.random.normal(50, 10, 36).reshape((6,6))

b = a.dot(a.T)


samples = np.random.normal(0, 6, 360)

for i in range(len(samples)):
	samples[i] -= 0.1*i


if __name__ == '__main__':
	print samples.sum()

	
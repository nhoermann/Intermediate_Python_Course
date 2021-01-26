import numpy as np
import matplotlib.pyplot as plt

dataset = np.random.randint(1, 101, 20)
plt.hist(dataset)

# save as pdf
plt.savefig('rand_data_hist.pdf')

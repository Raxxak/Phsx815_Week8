import numpy as np
import matplotlib.pyplot as plt




number_experiment=10000
number_measurement=1

i = -100
mu_true_array = []
mu_best_array = []
for i in range(0,100):
    
    mu_true = (i-100)/10
    
    # generating sample
    sample = np.random.normal(mu_true, 2, size=(number_experiment,number_measurement))
    
    mu_best = np.sum(sample, axis=1)/number_measurement 
    
    mu_best_array.append(mu_best)
    
    mu_true_array.append(mu_true * np.ones(number_experiment))


mu_true_array = np.array(mu_true_array).flatten()
mu_best_array = np.array(mu_best_array).flatten()




plt.hist2d(mu_true_array,mu_best_array, bins =[100,100])
plt.colorbar()
plt.xlabel('True value of $\\mu$')
plt.ylabel('Sampleed of $\\mu$')
plt.title('Neyman Construction of Gaussian')
plt.tight_layout() 

plt.show()
plt.savefig('Neyman.png')
    

''' 4. 
    Use numpy to create an array of numbers going from 20 to 100 by increments of .25
    Then, multiply all the values in the array by 4. 
    Then. find the sum of all the values.
'''
import numpy as np

list = np.arrange(20,100.1,0.25)

list = list*4

total = np.sum(list)
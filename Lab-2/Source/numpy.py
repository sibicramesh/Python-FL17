import numpy as np

newArr = np.random.random(15)
newArr[newArr.argmax()]=100
print (newArr)
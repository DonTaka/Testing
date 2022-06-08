import random
import numpy as np
m1 = np.random.randint(0,100, size=(3,3))
print(m1)

print(m1.mean());
print(m1.sum())
print(m1.max())
print(m1.min())
print(m1.diagonal())

m2 = np.diag([1,2,3]);
print(m2)
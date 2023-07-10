from numpy import random
import numpy as np
#rand = float, randint = integer

# Basic random 
# a = random.randint(100, size=(3))
# print(a)
# # b = random.rand(5)
# # print(b)
# c = random.choice([1,2,3,4,5,6,7,8,9])
# print(c)
# d = random.choice(a)
# print(d)

# # Data distribution in randomness
# e = random.choice([1,3,6,9], p=[0.1, 0.3, 0.6, 0], size=(10))
# print(e)

# # Permutasi ( [1,2,3] sama dengan [3,2,1] sama dengan [2,1,3]  )
# Shuffle = ganti isian list yang asli
# f = np.array([1,2,3,4,5,6,7])
# random.shuffle(f)
# print(f)

# Permutation = dia buat list baru dan teracak
g = np.array([10,11,12,13,14,15])
h = random.permutation(g)
print(h)
print(g)


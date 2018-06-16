import numpy as np

#A = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])

#print(A)

A=np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
#print(A)

#print("********")
B = A[[0, 2], 1:]


print(B)



#a=[ 1,2,3,4]

#b = np.ones((5, 5))
#b = a[:5]

#b = a[4:]
#b = np.ones(5, )



#x = np.random.rand(100)
#print(x)


#x[x > 0.5] = 1

#(x > 1).nonzero()[0][:3]
#x[:3] > 1
#x[x > 1][:3]
#(x > 1)[:3]


#data= {'a': 3, 'c': 9, 'b': 5}


#data['b'] = 100




#x = np.array([1,2,3,4,5])
#print(x)

#print(x**3)


#x = np.array([[1, 2, 3], [2, 3, 4]])
#x *= 5
#x -= 1
#x[x > 10] = 0
#x = x.T
#print(x)
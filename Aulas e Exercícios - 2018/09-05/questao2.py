from numpy import random as rd
l1=rd.randint(1,100,size=10)
l2=rd.randint(1,100,size=10)
elemento=0
for i in l1:
	for j in l2:
		if j == i:
			elemento+=1
print (elemento)
print (l1)
print (l2)

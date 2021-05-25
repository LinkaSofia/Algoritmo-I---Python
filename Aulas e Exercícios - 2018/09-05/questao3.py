from numpy import random as rd
l1=rd.randint(1,100,size=20)
l2=rd.randint(1,100,size=20)
l1.sort()
l2.sort()
ld=[]
for i in l1:
	igual=False
	for j in l2:
		if i == j:
			igual=True
			break
	if igual==False:
		ld.append(i)
	
print ('Numeros que não estão na segunda lista: ',ld)
print (l1)
print(l2)

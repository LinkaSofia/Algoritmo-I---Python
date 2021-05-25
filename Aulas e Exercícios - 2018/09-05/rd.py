from numpy import random as rd
lpar = []
limpar = []
lista1=rd.randint(100,1000,size=50)
for i in lista1:
	if i % 2 == 0:
		lpar.append(i)
	else:
		limpar.append(i)
print ('Pares: ', lpar,'\n')
print ('Impares: ', limpar)



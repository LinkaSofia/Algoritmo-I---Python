#Faça uma função que receba duas matrizes de mesma dimensão, caso não 
#forem retorne -1. Crie e retorne uma nova matriz que represente a soma
#das matrizes informadas
def matriz(m1,m2):
	m3=[]
	if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
		for i in range (len(m1)):
			soma=0
			v=[]
			for j in range (len(m1[0])):
				soma=m1[i][j] + m2[i][j]
				v.append(soma)
			m3.append(v)
		return m3
	else:
		return -1


m1=[[2,4],[6,8],[10,12]]
m2=[[1,3],[5,7], [9,11]]
sm=matriz(m1,m2)
print(sm)


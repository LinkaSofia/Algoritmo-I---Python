#para conseguir multiplar duas matrizes, uma deve ter o mesmo número de
#linhas e a outra de colunas
m1=[[1,2,1],[2,1,2]]
m2=[[1,2],[2,1],[3,1]]
def matriz(m1,m2):
	nl1=len(m1)
	nl2=len(m2)
	nc1=len(m1[0])
	nc2=len(m2[0])
	if nl1!=bl2:
		return [-1]
	mres=[]
	for c in range(nl1):
		lin=[0]
		for d in range(nc2):
			soma=0
			for k in range (nl2):
				soma+=m1[c][k]*m2[k][d]
			lin.append(soma)
		mres.append(lin)
print(mres)


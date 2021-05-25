# n=[[4,5,6],[1,2,3],[4,5,6]]
#n[0] é o mesmo que [4,5,6]
#n[1] é o mesmo que [1,2,3]
#n[2] é o mesmo que [4,5,6]
#[l][c]=linha e coluna

n=[[3,9,7,5],[10,5,15,20],[1,3,7,9],[6,7,8,9]]

#for i in range (len(n)):
#	print (n[i][i]) # imprime os numeros na diagonal

#for i in range (len(n)):
#	print (n[i]) # imprime toda matriz

#for i in range (len(n)):
#	for j in range (len(n[0])):
#		print (n[i][j], ' ', end='')
#	print()
#imprime de forma organizada

li=[]
for i in range (len(n)): #percorre a linha
	soma=0
	for j in range (len(n[0])): #percorre a coluna
		soma+=n[i][j]
	li.append(soma)
print(li)
#tem que dar 20
  

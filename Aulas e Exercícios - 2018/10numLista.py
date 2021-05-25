l=[]
for i in range(10):
	n=int(input('Informe o numero: '))
	l.append(n) #append inclui elemento na lista
for x in range(len(l)-1,-1,-1): #len utilizamos quando não sabemos o tamanho da lista
	print(l[x])
#pop() - elimina o ultimo elemento da lista (se não tiver nenhuma posição informada) ou elimina o elemento que eu colocar (posição 10 por ex)
#sort() - organiza em ordem crescente
#remove() - remover um valor duplicado ou o valor e não a posição 
#reverse() - ordem reversa (primeiro valor vai ser o ultimo)

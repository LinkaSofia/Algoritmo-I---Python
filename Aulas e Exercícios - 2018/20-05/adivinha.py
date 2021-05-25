import random as rd
#
def geraLista(menor,maior,quantidade):
	lista=[]
	i=1
	while i<=quantidade:
		n=rd.randint(menor,maior)
		if estahLista(n,lista)==False:
			lista.append(n)
			i+=1
		return lista
#	
def estahLista(n,l):
	for i in range(len(l)):
		if l[i]==n:
			return True
	return False
#	
#
print('Você tem que acertar um número de 40 entre 10 e 100')
lista=geraLista(10,100,40)
print(lista)
vezes=int(input('Numero tentativas: '))
for i in range(vezes):
	guess=int(input('Número: '))
	if estahLista(guess,lista)==True:
		print('You nailed it! Congrats!')
		break
	else:
		print('Come on! Try again. You have',vezes-i-1,' chances')

	
	

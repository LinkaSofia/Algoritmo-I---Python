from questao6 import nperfeito
n=int(input('Informe o número para saber se este é perfeito: '))
if nperfeito(n)==1:
	print(n, 'É perfeito')
if nperfeito(n)!=1:
	print(n,'Não é perfeito')

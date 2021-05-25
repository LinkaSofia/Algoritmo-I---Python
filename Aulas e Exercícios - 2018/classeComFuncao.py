class ExClasse:
	nome=''
	nvit=0
	nder=0
	nemp=0
def ex1(lis):
	for i in range (2):
		li=ExClasse()
		li.nome=(input('Informe o nome: '))
		li.nvit=int(input('Infome o número de vitórias: '))
		li.nder=int(input('Infome o número de derrotas: '))
		li.nemp=int(input('Infome o número de empates: '))
		lis.append(li)
lis=[]
ex1(lis)
pontos(lis)
#print(l[0].nome, l[0].nvit) - printa o primeiro elemento da de nome e o primeiro de vitorias
def retponto(lis):
	return li.nvit*3+t.nemp
def pontos(paises):
	mpt=0
	for i in range (len(paises)):
		pt=retpontos(paises[i])
		if pt>mpt:
			mpt=pt
	for i in range (len(paises)):
		if retpontos (paises[i])==mpt:
			print(paises[i].nome)
		
					

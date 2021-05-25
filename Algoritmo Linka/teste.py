from questao1 import conta
for i in range (5):
	nome=input('Informe o nome do aluno: ')
	nt1=float(input('Informe a primeira nota: '))
	nt2=float(input('Informe a segunda nota: '))
	print('O aluno', nome, 'ficou com a média de: ', conta(nt1,nt2))
		

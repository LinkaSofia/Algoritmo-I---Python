soma = 0
i = 0
n=0
maior=0
num=int(input('Digite um número: '))
while num>0:
	soma =soma+num
	i=i+1
	
	if num % 2 == 0:
		n=n+1
	if num>maior:
		maior=num
	num=int(input('Informe o outro número ou digite 0 para sair do programa: '))
	media=(soma/i)
	print('O maior número é: ',maior)
	print('Número(s) Par(es)', n)		
	print ('Soma',soma)
	print ('Média %.2f'%(media))
else:
	print('EROOOOOOOOOOOOOOUUUUUUUUU')

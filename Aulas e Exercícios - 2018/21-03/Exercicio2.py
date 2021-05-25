#faca um programa que peça o numero de votos de 3 candidatos no fim mostre o vencedor.
l1 = int (input('Informe o número de votos do primeiro candidato: '))
l2 = int (input('Informe o número de votos do segundo candidato: '))
l3 = int (input('Informe o número de votos do terceiro candidato: '))
if (l1>l2) and (l1>l3):
	print('O vencedor é o primerio candidato ')
if (l2>l1) and (l2>l3):
	print('O vencedor é o segundo candidato ')
if (l3>l1) and (l3>l2):
	print('O vencedor é o terceiro candidato ')
if (l1==l2):
 print ('O primeiro e o segundo candidatos empataram')
if (l1==l3): 
	 print ('O primeiro e o terceiro candidatos empataram')
if (l2==l3): 
	 print ('O segundo e o terceiro candidatos empataram')

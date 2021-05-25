primo=True
n= int(input('Digite o número: '))
for i in range (2,n):
	if n % i == 0:
		primo=False
		break
if primo == True:
	print('Primo')
else:
	print('Não é primo')

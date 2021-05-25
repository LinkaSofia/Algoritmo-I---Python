N=0
par=0
qntprimo=0
impar=0
primo=0
maior=0
soma=0
menor=100000
N=int(input('Informe o número: '))
while N>0:
	if N % 2 ==0:
		par+=1
	else: 
		impar+=1
	soma+=N
	if N > maior:
		maior = N
	if N < menor:
		menor = N
	primo=true
	for i in range(2,N):
		if N % i==0:
			primo: False
			break
	if primo == True:
		qntprimo+=1
	N=int(input('Informe o número: '))
print ('Média: ', soma/(par+impar))
print ('Pares: ', par)
print ('Impares: ', impares)
print ('Primos: ', qntprimo)
print ('Maior: ', maior)
print ('Menor: ', menor)

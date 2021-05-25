a,b,c = (input('Informe 3 números: ')).split()
a=int(a)
b=int(b)
c=int(c)
if abs(b-c)<a<b+c:
	print('É triangulo')
elif abs(a-c)<b<a+c:
	print('É triangulo')
elif abs(a-b)<c<a+b:
	print('É triangulo')
else:
	print('Não é triangulo')

num=[float(x) for x in input().split()]
num=sorted(num, reverse=True)
a=num[0]
b=num[1]
c=num[2]
if a>= b+c:
	print('NAO FORMA TRIANGULO')
elif a*a==(b*b+c*c):
	print('TRIANGULO RETANGULO')
elif a*a>(b*b+c*c):
	print('TRIANGULO OBTUSANGULO')
elif a*a<(b*b+c*c):
	print('TRIANGULO ACUTANGULO')
if a ==b and b==c:
	print('TRIANGULO EQUILATERO')
elif a == b and b!=c:
	print('TRIANGULO ISOSCELES')
elif b == c and b!=a:
	print('TRIANGULO ISOSCELES')
elif c == a and a!=b:
	print('TRIANGULO ISOSCELES')

from turtle import *
i=0
x=0
y=0
tamanho=100
while i<10:
	i+=1
	j=0	
	while (j<4):
		right(45)
		forward(tamanho)
		right(60)
		forward(70)
		right(60)
		forward(70)
		j+=1
	tamanho-=20
	penup() 
	y-=10
	setpos(x,y) 
	pendown() 

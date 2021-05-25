from turtle import *
i=0
x=0
y=0
tamanho=200
while i<10:
	i+=1
	j=0	
	while (j<4):
		forward(tamanho)
		right(90)
		j+=1
	tamanho-=20
	penup() #caneta sobe e para de escrever
	x+=10
	y-=10
	setpos(x,y) #vai dar uma nova posiçao para a seta
	pendown() #caneta volta a escrever

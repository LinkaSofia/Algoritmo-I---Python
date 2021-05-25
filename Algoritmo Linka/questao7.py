def notas(num):
	cont=0
	media=0
	for i in range (num):
		nota=float(input('Informe a Nota: '))
		cont+=nota
	media=(cont)/num
	return (media)

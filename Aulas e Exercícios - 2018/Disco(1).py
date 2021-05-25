f=open("teste2.txt", "w")
while True:
	t=(input('Informe a frase ou digite @ para finalizar o programa: '))
	if t=='@':
		break
	f.write(t+" ")
f.close()

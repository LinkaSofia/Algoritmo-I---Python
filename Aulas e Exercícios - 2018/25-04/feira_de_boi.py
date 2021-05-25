ttboi=0 #contador das notas
jovem=1000 #para saber qual boi é mais jovem
pesado=0
soma_geral=0
nome=(input('Informe o nome do boi: '))
while nome!='fim':
	peso=float(input('Informe o peso do boi em KG: '))
	idade=int(input('Informe a idade do boi em meses: '))
	soma_notas=0
	for i in range (6):
		i=float(input('Informe as notas do boi: '+str(i+1)))
		soma_notas+=notas 
	media=soma_notas/6
	soma_geral+=soma_notas
	print ('Média %.2f'%(soma_notas))
	ttboi+=1
	if peso>pesado:
		pesado=peso
		nom_pes=nome
	if idade<jovem:
		jovem=idade
		nom_jov=nome
	nome=input('Nome: ')
print ('Boi mais jovem: ', nom_jov)
print ('Boi mais pesado: ', nom_pes)
print ('Média das notas: ', soma_geral/ttboi)

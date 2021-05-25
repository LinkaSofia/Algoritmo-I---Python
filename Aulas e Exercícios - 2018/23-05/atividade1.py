class pessoa:
	nome=''
	cpf = 0
	idade = 0 
	nasc = 0
	rua = ''
	bairro = ''
	cidade=''
	estado=''
	
lpessoa=pessoa()
lpessoa.nome=input('Nome: ')
lpessoa.cpf = input ('CPF: ')
lpessoa.idade = input ('Idade:  ')
lpessoa.nasc = input ('Data de nascimento:  ')
lpessoa.rua = input ('Rua:  ')
lpessoa.bairro = input ('Bairro:  ')
lpessoa.cidade = input ('Cidade:  ')
lpessoa.estado = input ('Estado:  ')

print (lpessoa.nome,'-', lpessoa.cpf,'-', lpessoa.idade,'-',lpessoa.nasc,'-', lpessoa.rua,'-', lpessoa.bairro, '-',lpessoa.cidade,'-', lpessoa.estado)

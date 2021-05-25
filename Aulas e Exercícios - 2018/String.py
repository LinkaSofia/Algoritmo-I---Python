#Fazer uma função que receba uma cadeia de caracteres (String) e um
#caracter e retorne uma nova cadeia com o caracter passado como parâmetro
#substituido por *
def String(s,t):
	r=''
	for i in range(len(s)):
		if s[i]==t:
			r+='*'
		else:
			r+=s[i]
	return r

s=input('Informe a palavra: ')
t=input('Informe a letra que gostaria de substituir: ')
print(String(s,t))

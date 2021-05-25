Vlr_merc = float(input('Indorme o valor da mercadoria: '))
pag=int(input('Digite 1 caso for pagar a vista e 2 se for a prazo: '))
if pag == 1:
	desc=float(input('Informe o desconto: '))
	vlr=Vlr_merc-desc
	print('O valor final é', vlr)
if pag == 2:
	jur=float(input('Informe os juros: '))
	vlr_jur= Vlr_merc+jur
	print('O valor final é: ', vlr_jur)

from questao4 import primo
from questao4 import gemeos
gem=1
ver=0
for i in range (1,1001):
	if primo(gem) and primo (i):
		if gemeos(i,gem):
			print (gem, 'e',i,'sao gemeos')
		gem=i

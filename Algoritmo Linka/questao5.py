def soma(n,l1,l2,l3):
	concat1=''
	concat2=''
	
	for i in range (n):
		x=int(input('Digite os valores da lista 1: '))
		l1.append(x)
		
	for i in range (n):
		y=int(input('Digite os valores da lista 2: '))
		l2.append(y)
		
		
	for i in range (n):
		l3.append(0)
	
	for i in range (n-1,-1,-1):


		if l1[i]+l2[i] >=10:
			l3[i]=l1[i]+l2[i]-10
			l3[i-1]=l3[i-1]+1
			
		else:
			l3[i]=l3[i]+l1[i]+l2[i]
			
			if l3[i]>=10:
				l3[i]=l3[i]-10
				l3[i-1]=l3[i-1]+1
			
	


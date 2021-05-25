def q1():
    def media(n1,n2):
        med=(n1+n2)/2
        return med



    for i in range(5):
        nome=input('nome: ')
        n1=float(input('nota1: '))
        n2=float(input('nota2: '))
        med=media(n1,n2)
        print('%s possui media: %.2f' %(nome,med))

def q2():
    def min(n1,n2):
        if n1>n2:
            a=n1
        else:
            a=n2
        return a

    n1=int(input('Digite o primeiro numero: '))
    n2=int(input('Digite o segundo numero: '))
    a=min(n1,n2)
    print(a,'eh o maior')


def q3():
    def fat(n):
        f=1
        for i in range(0,n):
            f=f*(n-i)
        return f

    n=int(input('Digite um numero: '))
    fat=fat(n)
    print(fat)



def q4():
    def primo(n):
    	prim=True
    	for i in range(2,n):
    		if n%i==0:
    			prim=False
    			break
    	return prim

    def gemeo(i,aux):
        ehgemeo=False
        res=i-aux
        if res==2 or res==-2:
            ehgemeo=True
        return ehgemeo


    aux=1
    for i in range(1,1001):
        if primo(aux) and primo(i):
            if gemeo(i,aux):
                print(aux,'e',i,'sao gemeos')
            aux=i


def q5():
    n1 = []
    n2 = []
    n3 = []
    def soma(n,l1,l2,l3):
    	for i in range(n):
    		a=int(input('Digite os valores da lista 1: '))
    		l1.append(a)
    	for i in range(n):
    		b=int(input('Digite os valores da lista 2: '))
    		l2.append(b)
    	for i in range(n-1, -1, -1):
    		w=l1[i]+l2[i]
    		if w>9:
    			w-=10
    			l3.insert(0, w)
    			if i == 0:
    				l3.insert(0, 1)
    				break
    			l1[i-1] +=1
    		else:
    			l3.insert(0, w)
    n = int(input('Digite quantos valores terá cada lista: '))
    soma(n, n1, n2, n3)
    print(n3)


def q6():
    def pfto(n):
        cont=0
        for j in range(1,n):
            if n%j==0:
                cont+=j
        if cont==n:
            return 1
        else:
            return 0


    n=int(input('Digite um numero: '))
    if pfto(n)==1:
        print(n,'eh perfeito')
    else:
        print(n,'nao eh perfeito')


def q7():
    def media(n):
        med=0
        s=0
        for i in range(n):
            x=float(input('Digite a nota: '))
            s+=x
        med=s/n
        return med
    n=int(input('Digite o numero de notas: '))
    med=media(n)
    print('A media eh %.2f'%(med))


questao=input("Digite 'q' seguido do numero da questao para executar: ")
if questao=='q1':
    q1()
elif questao=='q2':
    q2()
elif questao=='q3':
    q3()
elif questao=='q4':
    q4()
elif questao=='q5':
    q5()
elif questao=='q6':
    q6()
elif questao=='q7':
    q7()

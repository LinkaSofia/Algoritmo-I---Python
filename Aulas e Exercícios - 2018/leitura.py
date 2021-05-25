f=open('teste2.txt','r+')
lista=f.readlines()
for i in range(len(lista)):
    print(lista[i][:-1]) #[:-1] tira as linhas em branco
f.close()

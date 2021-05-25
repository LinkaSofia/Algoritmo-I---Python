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

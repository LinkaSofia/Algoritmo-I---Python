
def primo2(n):
	prim=True
	for i in range (2,n):
		if n%i==0:
			return False
	return True 
	

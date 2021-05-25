def primo(num):
	pri=True
	for i in range (2,num):
		if num%i==0:
			pri=False
			break
	return pri

def gemeos(i, gem):
	gemeo=False
	ver=i-gem
	if ver==2 or ver ==-2:
		gemeo=True
	return gemeo		

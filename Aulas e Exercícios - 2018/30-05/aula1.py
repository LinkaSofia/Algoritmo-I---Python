def string(s):
	r=''
	for i in range (len(s)):
		if s[i]!=' ':
			r+=s[i] #junta a letra a palavra
	return r
	
s=input ('')
res=string(s)
print (res)
	

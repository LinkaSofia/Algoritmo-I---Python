#transposição de matrizes. 
# ex: [1 4]
#	  [2 6]     3x2
#	  [3 8]
#transforma-se em:
# [1 2 3]
# [4 6 8]    	2x3
def transp(m):
	m1=[]
	for j in range (len(m[0])):
		v=[]
		for i in range (len(m)):
			v.append(m[i][j])
		m1.append(v)
	return (m1)
m=[[1,4],[2,6],[3,8]]
print (transp(m))

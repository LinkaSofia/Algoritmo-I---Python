def nperfeito(n):
	perf=0
	for i in range (1,n):
		if n%i==0:
			perf+=i
	if perf==n:
		return 1
	else:
		return 0

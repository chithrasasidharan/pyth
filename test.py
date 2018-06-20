a = [[0 for x in range(7)] for y in range(7)]
a[0] = [1,0,1,2,3,0,0]
a[1] = [3 ,0, 2, 0 ,0, 3, 0]
n = 7
i = n-1
j=n-1
for k in range(2):
	i=n-1
	j=n-1
	while(i>=0):
		while(a[k][i]==0):
			i=i-1
		a[k][j] = a[k][i]
		a[k][i] = 0
		i=i-1
		j=j-1
for i in range(2):
	print(a[i])

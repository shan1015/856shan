a,g=map(int,input().split())
C=list(map(int,input().split()[:a]))
for i in range (0,g):
	C=[C[-1]]+C[:-1]
for j in C:
	print(j,end=" ")

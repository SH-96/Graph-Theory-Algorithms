#Import Modules & initialise lists
import os
A=[]
B=[]
C=[]
c=k=0

#Input
x=int(input("\nEnter number of vertices: ")) #number of vertices in the graph

for i in range(0,x):
	print("\nEnter the elements of row "+str(i+1)+" :")#Entering elements of adjacency matrix
	for j in range(0,x):
		val=int(input())
		if(val==1):
			c+=1
		B.append(val)
	A.append(B)
	B=[]
c=(c/2)+x

os.system('cls') #clear screen
for i in range(0,x): #printing original matrix
	print(str(A[i])+"\n")

for i in range(0,c): #creating empty final matrix
	for j in range(0,c):
		B.append(0)
	C.append(B)
	B=[]

for i in range(0,x): #checking vertex and edge adjacency
	for j in range(i,x):
		if(A[i][j]==1):
			C[i][j]=C[j][i]=1
			C[i][x+k]=C[x+k][i]=1
			C[j][x+k]=C[x+k][j]=1
			k+=1
	for l in range(c-1,x-1,-1): #checking edge-edge adjacency
		if(C[i][l]==1):
			for m in range(l-1,x-1,-1):
				if(C[i][m]==1):
					C[m][l]=1
					C[l][m]=1

for i in range(0,c):#printing final total matrix
	print(str(C[i])+"\n")
N = int(input())
for i in range(N):
    left_space = " "*(N-i-1)
    print(left_space,end="")
    for j in range(1,i+2):
        print(str(j),end=" ")
    print()    
for i in range(1,N+1):
    left_space = " "*(i)
    print(left_space,end="")
    for j in range(1,N):
        print(str(j),end=" ")
    print()       
    N = N - 1
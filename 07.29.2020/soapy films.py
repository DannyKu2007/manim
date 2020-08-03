a = [[-1,-1,-1,-1,-1],[-1,1,0,1,-1],[-1,1,0,1,-1],[-1,1,0,1,-1],[-1,-1,-1,-1,-1]]
b = [[-1,-1,-1,-1,-1],[-1,1,0,1,-1],[-1,1,0,1,-1],[-1,1,0,1,-1],[-1,-1,-1,-1,-1]]
epsilon = 1
while epsilon > 0.001:
    epsilon = 0
    for i in range(1,len(a)-1):
        for j in range(1,len(a[0])-1):
            b[i][j] = (a[i][j+1]+a[i+1][j]+a[i-1][j]+a[i][j-1])/4
            epsilon += (a[i][j] - b[i][j])**2
    
    for i in range(5):
        for j in range(5):
            a[i][j]=b[i][j]
    print(a,end='\n')

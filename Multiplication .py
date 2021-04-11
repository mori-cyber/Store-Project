import random


n = int(input('enter first num:'))
m = int(input('enter second num: '))
k = int(input('enter third num: '))

a =  [[1 for i in range(m)] for j in range(n)]
b = [[1 for i in range(k)] for j in range(m)]
X = [[0 for i in range(k)] for j in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(1,9)
        
for i in range(m):
    for j in range(k):
        b[i][j] = random.randint(1,9)

i=0      
while i<n:
    for j in range(k):
        for k in range(m):
            X[i][j] += (a[i][k] * b [k][j]) 
    i+=1    
print('x = ', a)
print('y = ', b)
print('this is mutiplication result : ', X)
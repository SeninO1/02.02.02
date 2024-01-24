N = int(input())
mass = [] 
if 1 <= N <= 10 ** 5:
    for i in range(N):
        a = int(input())
        mass.append(a) 
mass.reverse()
print(mass)


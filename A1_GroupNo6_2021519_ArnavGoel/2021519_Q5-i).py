import math
import matplotlib.pyplot as plt

def u(n):
    if n < 0:
        return 0
    else:
        return 1

def x(n):
    pow = (math.e)**(-(0.3*(n-10)))
    add1 = 10*pow*(u(n-10)-u(n-20))
    add2 = n*(u(n)-u(n-10))
    return add1+add2

lst = []
for i in range(0,21,1):
    lst.append(i)

res = []
for i in range(len(lst)):
    res.append(x(lst[i]))

plt.stem(lst, res)
print("The input values are:")
print(lst)
print("The corresponding output values for the same are:")
print(res)
plt.xticks(ticks=lst)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.show()
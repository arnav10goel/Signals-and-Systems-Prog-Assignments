import math
import matplotlib.pyplot as plt

def u(n):
    if n < 0:
        return 0
    else:
        return 1

def y(n):
    add1 = math.cos(0.03*(math.pi)*n)
    add2 = u(n)
    return add1 + add2

lst = []
for i in range(0,51,1):
    lst.append(i)

res = []
for i in range(len(lst)):
    res.append(y(lst[i]))

lst2 = []
for i in range(0,51,5):
    lst2.append(i)

plt.stem(lst, res)
print("The input values are:")
print(lst)
print("The corresponding output values for the same are:")
print(res)
plt.xticks(ticks=lst2)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.show()


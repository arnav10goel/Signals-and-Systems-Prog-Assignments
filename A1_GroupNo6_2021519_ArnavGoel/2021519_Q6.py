import math
import matplotlib.pyplot as plt

def u(n):
    if n < 0:
        return 0
    else:
        return 1

def z(n):
    return u(n)-u(n-10)

lst1 = []
for i in range(-20,21):
    lst1.append(i)

res1 = []
for i in range(len(lst1)):
    res1.append(z(lst1[i]))

def z_even(n):
    return (z(n) + z(-1*n))/2

def z_odd(n):
    return (z(n) - z(-1*n))/2

res2 = []
for i in range(len(lst1)):
    res2.append(z_odd(lst1[i]))


plt.show()

res3 = []
for i in range(len(lst1)):
    res3.append(z_even(lst1[i]))

print("For the given input range", lst1)
print("Outputs of z[n] are:", res1)
print("Outputs of z_odd[n] are:", res2)
print("Outputs of z_even[n] are:", res3)

fig,plot = plt.subplots(3)
plt.subplots_adjust(hspace = 0.8)
plot[0].set_title("Function: z[n]")
plot[0].stem(lst1, res1)
plot[0].set(xlabel = 'n', ylabel = 'z[n]')
plot[1].set_title("Odd Part of z[n]")
plot[1].stem(lst1, res2)
plot[1].set(xlabel = 'n', ylabel = 'z_odd[n]') #Odd part
plot[2].set_title("Even Part of z[n]")
plot[2].stem(lst1, res3)
plot[2].set(xlabel = 'n', ylabel = 'z_even[n]') #Even part
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0, 3*np.pi , 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

#Create the scond subplot
# plt.subplot(2, 1, 1)
# plt.plot(x, y_sin)

# plt.subplot(2,1,2)
# plt.plot(x, y_cos)
# plt.xlabel("X axis label")
# plt.ylabel("Y axis label")
# plt.title("Sine and Cosine")
# #plt.legend(["Sine","Cosine"])
# plt.show()
# print(" I an Here")

x= np.linspace(-20,20, 1000)

def func(x):
    y= []
    for elem in x:
        #result= elem**2
        result = -5*(elem ** 2) + 4*elem +1
        y.append(result)
    return y

y = func(x)
plt.plot(y)
plt.show()
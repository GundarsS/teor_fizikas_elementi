import numpy as np
from matplotlib import pyplot as plt

data01=np.loadtxt("aluminium.txt")
data02=np.loadtxt("titanium.txt")
data03=np.loadtxt("niobium.txt")
data04=np.loadtxt("havar.txt")

plt.plot(data01[:,0],data01[:,1])
plt.plot(data02[:,0],data02[:,1])
plt.plot(data03[:,0],data03[:,1])
plt.plot(data04[:,0],data04[:,1])
plt.show()

r1=270e3
r2=63e3
r3=85e3
r4=42e3
#tensile strength

alpha=1
t1=data01[:,0]
x1=data01[:,1]/np.power(r1,alpha)
t2=data02[:,0]
x2=data02[:,1]/np.power(r2,alpha)
t3=data03[:,0]
x3=data03[:,1]/np.power(r3,alpha)
t4=data04[:,0]
x4=data04[:,1]/np.power(r4,alpha)

plt.plot(t1,x1)
plt.plot(t2,x2)
plt.plot(t3,x3)
plt.plot(t4,x4)
plt.xlim([0,800])
plt.ylim([0,0.1])
plt.show()

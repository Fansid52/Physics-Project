import matplotlib.pyplot as plt
import math
import numpy as np

dt=0.001
t=0
omega=0
ang0=1
ang=ang0
alpha=10
x=[]
y=[]
x1=[]
y1=[]
while t<=2+dt:
    y.append(ang/ang0)
    x.append(t)
    y1.append(math.cos(alpha*t))
    t+=dt
    dw=-(alpha**2*math.sin(ang)*dt)
    omega+=dw
    dang=omega*dt
    ang+=dang
    
plt.plot(x,y,marker="o", markeredgecolor="red", markerfacecolor="none", markersize=2)

plt.plot(x,y1,label="cos(x)",color="orange")
plt.legend()
plt.show()

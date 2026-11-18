import matplotlib.pyplot as plt
import math
def plot_func (ang0,ang,alpha,x,y):
    dt=0.001
    t=0
    omega=0
    while t<=2+dt:
        y.append(ang/ang0)
        x.append(t)
        t+=dt
        dw=-(alpha**2*math.sin(ang)*dt)
        omega+=dw
        dang=omega*dt
        ang+=dang
x1=[]
y1=[]
ang0_1=1
ang_1=ang0_1
alpha1=10
plot_func(ang0_1,ang_1,alpha1,x1,y1)
plot=plt.plot(x1,y1,marker="o", markeredgecolor="red", markerfacecolor="none", markersize=6)

x2=[]
y2=[]
ang0_2=0.5
ang_2=ang0_2
alpha2=10
plot_func(ang0_2,ang_2,alpha2,x2,y2)
plot=plt.plot(x2,y2,marker="o", markeredgecolor="orange", markerfacecolor="none", markersize=6)
plt.show()

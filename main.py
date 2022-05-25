from random import * 

import numpy as np
import matplotlib.pyplot as pl

def f(x): 
    return -x**2+2*x+3

def main(a,b, ym): 
    n = 100000; ni = 0; xi = []; yi = []; xs=[];ys=[]
    for i in range(0,n+1):
        x = uniform(a,b); 
        y = uniform(0,ym); 

        if y <= f(x):
            ni+=1;
            xi.append(x)
            yi.append(y)

        else: 
            xs.append(x)
            ys.append(y)

    A = (ym*(b-a)*ni)/n; print(round(A,2))

    xf = np.linspace(a-1,b+1);yf = -xf**2+2*xf+3
    pl.grid(which="major")
    pl.xlim(-10,10);pl.xticks(np.linspace(-10,10,11, endpoint=True))
    pl.ylim(-10,10); pl.yticks(np.linspace(-10,10,11,endpoint=True))

    pl.plot(xf,yf,linestyle="solid")
    pl.scatter(xi,yi,color="yellow")
    pl.scatter(xs,ys,color="black")
    pl.show()

main(-2,2, 4)

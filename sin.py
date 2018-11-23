from pylab import plot, show
plot, show
import random, math


length = 100
granularity = 25

def _plot(length, granularity):
    cx = []
    cy = []
    for i in range(0,length*granularity):
       cx.append(i/granularity)
       cy.append(math.sin(i/granularity))
    
   # print(cx,cy)
    plot(cx,cy)
    show()

_plot(length, granularity)

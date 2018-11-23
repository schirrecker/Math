from pylab import plot, show
plot, show
import random

x=[1]
y=[1]
length = 60

def _plot(x,y,length,size_amp,send_back,absolute):
    cx = [x[0]]
    cy = [y[0]]

    if send_back == True:
        for i in range(0,length*2):
            cx.append(i)
        for i in range(0,length):
            cy.append((cy[i] * random.choice([0.7,0.8,0.9,1,1.1,1.2,1.3]))/size_amp)
            cy.append(1)
    else:
        for i in range(0,length):
            cx.append(i)
        for i in range(0,length):
            cy.append((cy[i] * random.choice([0.7,0.8,0.9,1,1.1,1.2,1.3]))/size_amp)

    
    print(cx,cy)
    if absolute == True:
        plot(abs(cx),abs(cy))
    else:
        plot(cx,cy)
    show()

_plot(x,y,length,1,True,True)

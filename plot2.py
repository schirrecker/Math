import matplotlib.pyplot as plt

##nyc_temp=[4.3, 3.2, 5.4, 10, 4, 6.4, 5.6, 7.1, 2.0, 9.1]
##year = range(2000, 2010)
##plt.plot(year, nyc_temp, marker='o')
##plt.show()
##plt.savefig("graph.png")


def graph(x,y, label_x, label_y, title):
    plt.plot(x,y,marker='o')
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(title)
    plt.show()

def f(x):
    y = x ** 2
    return y

def generate(f, x_range):
    xlist = []
    ylist = []
    for x in x_range:
        xlist.append(x)
        ylist.append(f(x))
    return (xlist, ylist)

x, y = generate(f, range(-20, 20))
graph(x, y, "x", "x square", "Graph")


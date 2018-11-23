def median(l):
    size = len(l)
    print ("Length="+ str(size))
    l.sort()
    print ("Sorted list: " + str(a))
    print(l)
    if size % 2 == 0:   #even
        print("This is an even list")
        return (l[int(size/2)-1] + l[int(size/2)])/2
    else:
        print ("This is an odd list")
        return l[int(size/2)]


a =[7, 1, -3, 0, 4, -1, 2, 5, 7, 7, 3, -2, -4, -5]

print(median(a))

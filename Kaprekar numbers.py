## n = input("Enter a four-digit number: ")

def padding(txt):
    if len(txt) == 1:
        new_txt = "000" + txt
    elif len(txt) == 2:
        new_txt = "00" + txt
    elif len(txt) == 3:
        new_txt = "0" + txt
    else:
        return txt
    return new_txt
    
def digits(txt):
    l_str = list(txt)
    l_int = []
    for i in l_str:
        l_int.append(int(i))
    return l_int

def transform(txt):
    l = digits(txt)
    l_max_str = sorted(l)
    l_min_str = sorted(l, reverse = True)
    l_max = int(''.join(map(str, l_max_str)))
    l_min = int(''.join(map(str, l_min_str)))
    diff = str(l_min - l_max)
    return padding(diff)

iterations = {}

for n in range(1, 10000):
    t = padding(str(n))
    m = ""
    count = 0
    while m != "6174" and m != "0000":
        count += 1
        m = transform(t)
        t = m
    iterations[n] = count
    print("Iterations: " + str(count))

print("Max iterations: " + str(max(iterations.values())))

      






      

    

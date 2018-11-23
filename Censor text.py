def censor(text, word):
    list = text.split()
    newlist = []
    for w in list:
        if w == word:
            newlist.append(len(w)*"*")
        else:
            newlist.append(w)
    return " ".join(newlist)
    
print (censor("Hi there Ismene", "Ismene"))

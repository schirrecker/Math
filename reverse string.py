def reverse(text):
    rev = ""
    for l in range(len(text)-1, -1, -1):
        rev += text[l]
    return rev
        
print (reverse("alois"))

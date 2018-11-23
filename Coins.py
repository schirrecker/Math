T = "T"   # T moves right only
H = "H"   # H moves left only
S = "_"   # Space
left = "left"
right = "right"

def pprint(l):
    txt = ""
    for item in l:
        txt = txt + item
    print (txt)

def shift(l, direction):
    if direction == "right":
        for i in range (1, len(l)):
            if l[i] == S and l[i-1] == T:
                l[i] = T
                l[i-1] = S
                print("Shifting right")
                return True
        return False
    if direction == "left":
        for i in range (0, len(l)-1):
            if l[i] == S and l[i+1] == H:
                l[i] = H
                l[i+1] = S
                print("Shifting left")
                return True
        return False

def jump(l, direction):
    if len(l) < 3:
        return False
    else:
        i = row.index(S)
        if direction == "right":
            if i < 2:
                return False
            elif l[i-1] == H and l[i-2] == T:
                l[i-2] = S
                l[i] = T
                print("Jumping right")
                return True
            else:
                return False
        if direction == "left":
            if i > len(l)-3:
                return False
            elif l[i+1] == T and l[i+2] == H:
                l[i+2] = S
                l[i] = H
                print("Jumping left")
                return True
            else:
                return False

def move(l, move_choice):   
    if move_choice[0] == "shift":
        return shift(l, move_choice[1])
    if move_choice[0] == "jump":
        return jump(l, move_choice[1])

def solved(l):   # check if the row has been succesfully re-ordered
    for i in range(0, int(len(l)/2)):
        if l[i] != H or l[len(l)-1] != T:
            return False
    print("Solved!")
    return True

def solve(row):
    moves = []
    moves_tried = []
    stuck = False
    possible_moves = (("shift", "left"), ("shift", "right"), ("jump", "left"), ("jump", "right"))
    shifts, jumps = 0, 0

    while not solved(l):
        # try new move
        if not stuck:  # pick a move and add it to the list of moves
            stuck = True
            for move_choice in possible_moves:
                if move(l, move_choice):
                    stuck = False
                    moves.append(move_choice)
                    moves_tried.append(....)
        else:    # go back to previous move and try another one
            for move_choice in possible_moves:
                if move(l, move_choice) and move_choice != moves_tried{.....]:
                    moves.remove(moves[-1])
                    moves.append(move_choice)
                    stuck = False      
                

row = [T, T, S, H, H]
print(row)
solve(row)


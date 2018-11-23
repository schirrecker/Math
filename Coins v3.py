'''----------------------------------------------------------------------------- 
    Possible moves: ((shift, left), (shift, right), (jump, left), (jump, right))
    History = [ record, record, ...]   Stack
    record:
        record.move
        record.row
    Possivle moves will function as a queue: we will test them in order
    0, 1, 2, 3 iterating using nextPossibleMove and checking for lastPossibleMove
    We could also use Iterations?
    We could also define these as "choices" and create a new Class
    Question: should we stack them all, then test them? \b0
-------------------------------------------------------------------------------- '''

import datetime, sys
sys.setrecursionlimit(2000)
R, L, S = "R", "L", "S"   
LEFT, RIGHT, SHIFT, JUMP, STUCK = "left", "right", "shift", "jump", "stuck"
possibleMoves = ((JUMP, LEFT), (JUMP, RIGHT),(SHIFT, LEFT), (SHIFT, RIGHT))
maxMoves = len(possibleMoves)   

def lastPossibleMove(move):
    if possibleMoves.index(move) == len(possibleMoves)-1:
        return True
    else:
        return False
    
def nextPossibleMove(move):
    i = possibleMoves.index(move)
    if i < len(possibleMoves)-1:
        return possibleMoves[i+1]
    else:
        return move

'''-------------------------------------------------------------------------
	History is a class inherited from the Class list
	Check how we need to init History (super) 
	History functions like a Stack. Each item of the stack is a Record
	A Record has 2 attributes: row (status) and the move that was applied
	History.current_row is the current status
	History.initial_row is the starting point (we need to restore if the Stack becomes empty
-----------------------------------------------------------------------------'''

class History(list):
    backtracks = 0
    trials = 0
    class Record():
        def __init__(self, row, move):
            self.move = move
            self.row = row

        def __repr__(self):
            txt = ""
            for l in self.move:
                txt += l
                txt += " "
            txt += "\t"
            for l in self.row:
                if l == "S":
                    txt += "_"
                else: 
                    txt += l
                txt += " " 
            return  txt

    def __init__(self, size):
        self.size = size
        self.current_row = Row(size)
        self.initial_row = Row(size)
        self.tryMove(possibleMoves[0])

    def tryMove(self, move):
        self.trials += 1
        if self.current_row.solved():
            print ()
            print ("SOLVED")
            print ()
        else:
            if self.current_row.moving(move):
                new_row = Row(self.size)
                new_row.copyRow(self.current_row)
                self.append(self.Record(new_row, move))
                self.pprint()
                self.tryMove(possibleMoves[0])
            elif lastPossibleMove(move):
                self.backtracks += 1
                last_move = self.getLastMove()  
                self.popRecord()
                print("Backtracking")
                print("")
                self.pprint()
                self.tryMove(nextPossibleMove(last_move))     
            else:
                self.tryMove(nextPossibleMove(move))

    def getLastRow(self):
        if len(self) == 0:
            return list(self.initial_row)
        else:
            return self[-1].row

    def getLastMove(self):
        try:
            return self[-1].move
        except:
            return possibleMoves[0]

    def popRecord(self):
        self.pop()
        self.current_row.copyRow(self.getLastRow())
        

    def pprint(self):
        i = 0
        for record in self:
            i += 1
            print(str(i) + " " + str(record))
        # print ("Current state: " + str(self.current_row))
        print()

    def printSummary(self):
        print()
        print ("Trials: " + str(self.trials))
        print ("Backtracks: " + str(self.backtracks))
        
class Row(list):
    def __init__(self, size):
        for i in range(0, int(size/2)):
            self.append(R) 
        self.append(S)
        for i in range(0, int(size/2)):
            self.append(L)

    def copyRow(self, otherRow):
        self.clear()
        for i in otherRow:
            self.append(i)
            
    def moving(self, move):   
        if move[0] == SHIFT:
            return self.shift(move[1])
        if move[0] == JUMP:
            return self.jump(move[1])

    def solved(self):   # check if the row has been succesfully re-ordered
        for i in range(0, int(len(self)/2)):
            if self[i] != L or self[len(self)-1] != R:
                return False
        return True

    def shift(self, direction):
        if direction == RIGHT:
            for i in range (1, len(self)):
                if self[i] == S and self[i-1] == R:
                    self[i] = R
                    self[i-1] = S
##                    print()
##                    print("SHIFTING RIGHT")
##                    print()
                    return True
            return False
        if direction == LEFT:
            for i in range (0, len(self)-1):
                if self[i] == S and self[i+1] == L:
                    self[i] = L
                    self[i+1] = S
##                    print()
##                    print("SHIFTING LEFT")
##                    print()
                    return True
            return False

    def jump(self, direction):
        if len(self) < 3:
            return False
        else:
            i = self.index(S)
            if direction == RIGHT:
                if i < 2:
                    return False
                elif self[i-1] == L and self[i-2] == R:
                    self[i-2] = S
                    self[i] = R
##                    print()
##                    print("JUMPING RIGHT")
##                    print()
                    return True
                else:
                    return False
            if direction == LEFT:
                if i > len(self)-3:
                    return False
                elif self[i+1] == R and self[i+2] == L:
                    self[i+2] = S
                    self[i] = L
##                    print()
##                    print("JUMPING LEFT")
##                    print()
                    return True
                else:
                    return False

'''----------------------------------
    Main Program
-------------------------------------'''

n = 5
t1 = datetime.datetime.now().replace(microsecond=0)
history = History(n)
t2 = datetime.datetime.now().replace(microsecond=0)
print ("System recursion limit: " + str(sys.getrecursionlimit()))
print ("Solved with " + str(n) + " coins") 
print ("Time: " + str(t2-t1))
history.printSummary()


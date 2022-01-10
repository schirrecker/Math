# --------------------------------
# Cellular Automata
# from Eli Lebow class
# FireCracker Math, May 2, 2016
# --------------------------------

# initialization
# --------------
size = 10         	# number of cells in a row
Nb_steps = 16     	# number of transformation steps  
row  = []           	# a row is a list of cells
down = ' '        	# student sitting
up = 'X'          	# student standing

for i in range (size):  # initial situation 
    row.append(down)    # everyone sitting 
row[0] = up             # except the first one

# display function
# ----------------
def display(step, row):
    txt = ''
    for i in row:
        txt = txt + ' ' + i
    txt = 'Step ' + str(step) + '     ' + txt
    print (txt)

# one-step transformation
# -----------------------
def transform(row):
    new_row = [] 				    # initialize new_row and keep it empty for now
    for i in range(len(row)):			    # use the simple rule from the class: 
        new_row.append(down)                        # if person on the left standing and you are sitting, then stand
    # do the first item in the row first            # if person on the left sitting you are sitting, then stay sitting
    if row[0] == up and row[len(row)-1] == up:      # if person on the left sitting you are standing then stay standing
        new_row[0] = down                           # if person on the left standing you are standing then sit
    elif row[0] == up and row[len(row)-1] == down:
        new_row[0] = up
    elif row[0] == down and row[len(row)-1] == up:
        new_row[0] = up
    else:
        new_row[0] = down
    for i in range (1, len(row)):		    # then iterate on all others
        if row[i] == up and row[i-1] == up:         # use the simple rule from the class
            new_row[i] = down
        elif row[i] == up and row[i-1] == down:
            new_row[i] = up
        elif row[i] == down and row[i-1] == up:
            new_row[i] = up
        else:
            new_row[i] = down
    return new_row

# Display and transform row
# -------------------------

for i in range (Nb_steps+1):
    display(i, row)
    row = transform(row)


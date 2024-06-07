

def findNonAttackingPosition(i, j, placed, oldDiag):
    print(f'call i: {i}, j: {j}')
    if i == 7 and j == 7:
        print('end')
        return
    elif i == 7:
        return findNonAttackingPosition(i, j+1, placed, oldDiag)
    elif j == 7:
        return findNonAttackingPosition(i+1, j, placed, oldDiag)
    
    p = placed[-1]

    if p[1] == j: # in same row
        return findNonAttackingPosition(i, j+1, placed, oldDiag)
    elif p[1] == j: # in same col
        return findNonAttackingPosition(i, j+1, placed, oldDiag)
    elif p[0]+1 == oldDiag[0] and p[1]+1 == oldDiag[1]:
        return findNonAttackingPosition(i, j+1, placed, oldDiag)
    return (i, j)

def main():
    global oldDiag
    global placed
    oldDiag = (0, 0)
    placed = [(0, 0)]
    print('8 queen problem')
    s = {row: 0, col: 0} # fst
    t = (0, 1) # sec
    found = False
    fRC = None
    founds = []
    for k in range(0, 8): # total queens to be found.
        for f in founds: # check new finding against each already founded. (to be ctd..)
            for row in range(0, 8):
                for col in range(0, 8):
                    if s.row == row and s.col == col: # overlap
                        continue # skip for next col
                    if s.row == row: # in same row
                        break # goto next row
                    elif s.row + 1 == row and s.col + 1 == col: # daigonal
                        continue # skip for next col
                    # if reached here, means everything is ok for the (row, col)
                    found = True
                    fRC = (row, col)
                if found:
                    break # break out of the row loop
            if found:
                founds.append(fRC)
                print(f'Found at k: {k} => {fRC}')
            else:
                print(f"Not found at k: {k}")

                    

    for i in range(0,8):
        p = findNonAttackingPosition(placed[-1][0], placed[-1][1], placed, oldDiag)
        print(p)
        placed.append(p)
        oldDiag = p
        if len(placed) == 8:
            break
    print(placed)
    

if __name__  == '__main__':
    main()

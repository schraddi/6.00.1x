def printMove(pileOrign, pileAim):
    print pileOrign + " -> " + pileAim
    
def reOrderStack(size, pileOrign, pileAim, pile3):
    if size == 1:
        printMove(pileOrign, pileAim)
    else:
        reOrderStack(size-1, pileOrign, pile3, pileAim)
        reOrderStack(1, pileOrign, pileAim, pile3)
        reOrderStack(size-1, pile3, pileAim, pileOrign)
        
size = int(raw_input("Stack Size: "))

moves = 2**size-1

jesNo = 'J'
limit = 20000

if moves > 20 and moves < limit:
    jesNo = raw_input("It will take " + str(moves) + " moves to do that. Do you want to continue? <j,n> ").upper()
if jesNo == 'J' and moves < limit:
    reOrderStack(size, 'A', 'B', 'C')
    print str(moves) + " moves"
elif jesNo == 'J':
    print "Sorry, I can't do that. It would take " + str(moves) + " moves."
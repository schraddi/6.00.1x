case_select = 'l'
low = 0
high = 100
guess = 50
print "Please think of a number between 0 and 100!"
while case_select != 'c':

    print "Is your secret number " + str(guess) + "?"
    
    case_select = raw_input("Enter 'h' to indicate the guess is too high.\
        Enter 'l' to indicate the guess is too low.\
        Enter 'c' to indicate I guessed correctly. ")
        
    if case_select == 'c':
        print "Game over. Your secret number was: " + str(guess)
    elif case_select == 'l':
        low = guess
    elif case_select == 'h':
        high = guess
    else:
        print "Sorry, I did not understand your input."
    guess = (low + high) / 2
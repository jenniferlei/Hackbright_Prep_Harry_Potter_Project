from replit import clear

def press_return_to_cont(cont=True):
    '''
    asks user to press return to clear screen and continue to next step
    '''
    print()
    if cont is True:
        input("Press RETURN to continue")
    else:
        input("Press RETURN to restart game")
    clear()
    return cont
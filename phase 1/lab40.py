while True:
    my_float = input("Number to square please: ")
    try:
        number = float(my_float)
    except  ValueError :
        print("Please try again.")
    else:
        digits = input("""How many digits to the right of the decimal place would
you like to have displayed?""" )
    try:
        number2 = int(digits)
    except ValueError :
        print("Please try again.")
    else:
        print ( f"{ number } squared is "
                f"{ number * number :.{ digits }f}.")
        
    
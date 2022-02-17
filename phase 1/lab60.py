#1

favorites =  ("ham", "poached", "home fried", "English muffin")

def DoBreakfast (*favorites):
    for item in favorites:
        print(item)
DoBreakfast(*favorites)  


#2


#!/ usr/bin/env python3
"""
Function that shows how to isolate " scissors " into the identifier
to_cut }
and put the rest into meaningless identifiers , as few as possible ?

And demonstrate what happens when there are no identifiers left fo
r the *.
"""
def DoLab ():
    tools = " hammer ", " wrench ", " scissors ", " pliers ", " ruler "
    to_hit , to_torque , to_cut , * rest = tools
    print ( f"a: to_cut = { to_cut }")

    to_hit , to_torque , to_cut , to_pinch , to_measure , * rest = tools
    print ( f"b: rest = { rest }")

def main ():
    DoLab ()

main ()

#3

#!/ usr/bin/env python3
"""
lab60_3 .py - a a MakePizza () function . It takes in any number of
arguments . The first two are the main ingredients and are required
.
"""
def MakePizza ( first , second , * rest ):
    print ( f" Here 's your { first } and { second } pizza , with ", end ='')
    for ingredient in rest :
        print ( f" { ingredient }", end ='')
    print ("\ nEnjoy !")

def main ():
    ingredients = " anchovies ", " garlic ", " oregano ", " tomato ", "pep
                    pers "
    MakePizza (* ingredients )
    MakePizza (" cheese ", * ingredients )

main ()


    

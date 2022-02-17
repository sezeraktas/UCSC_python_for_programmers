#1 

#!/ usr/bin/env python3
""" Predict the output .
"""
pi = 3 . 14

def Report ( message ):
    print ( f"{ message } pi = {pi }.")

def SetLocal ():
    pi = " yellow "

def SetGlobal ():
    global pi

    pi = " red "

def Crash ():
    pi += " orange "
    
def main ():
    Report (" Starting :")
    SetLocal ()
    Report (" After SetLocal (): ")
    SetGlobal ()
    Report (" After SetGlobal (): ")
    Report ("\ nBefore Crash (): ")
    Crash ()

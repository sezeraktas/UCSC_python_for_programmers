
#1a

def JudgeNumber(number):
    try:
        return "Good number " "{:.1f}".format(number)
    except ValueError:
        return "not a number!"

print(JudgeNumber(32.22))


#1b

def Sentence(noun, verb):
    print ( f' "All of our { noun } wanted to { verb }."')
    
    
    
#2a

def CentigradeToFahrenheit(centigrade):
    fahrenheit = round((9/5)*centigrade + 32)
    return fahrenheit


def FahrenheitToCentigrade(fahrenheit):
    centigrade = round((fahrenheit - 32)*(5/9))
    return centigrade



#2b



def ShowConversion():
    print("C ->  F")
    for centigrade in range(0, 101, 10):
        print( f"{centigrade} -> { CentigradeToFahrenheit (centigrade) }")
    print("----")
    for fahrenheit in range(0, 221, 10):
        print( f"{fahrenheit} -> { FahrenheitToCentigrade (fahrenheit) }")
        
ShowConversion()
        
def VerifyConversion():
    for f in range(0, 1000,10):
        print( f"{f} -> { abs(f - CentigradeToFahrenheit(FahrenheitToCentigrade (f))) }")
        

VerifyConversion()  
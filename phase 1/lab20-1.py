#1
print(tuple(range(3, 13, 3)))
print(tuple(range(-10, 211, 110)))
print(tuple(range(-1, -8, -2)))


#2
for num in range(10, 0, -1):
    print(num, end = " ")
print("BLASTOFF!")

#4
for thing in (("Hi ya Manny!"),("Hi ya Moe!"),("Hi ya Jack!")):
    print(thing)

#5???
num = 19
for i in range(1, num+1, 2):
    print(" "*(num - i) + "* " * i)


#6
binary_string = 1011
print("decimal equivalent: ", int(str(binary_string),2))


      

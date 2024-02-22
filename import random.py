import random

userInput = int(input("How many times?"))
startingNumber = int(input("Starting number?"))


counter = startingNumber
song = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"

counter = 1
for x in range(userInput):
    song = ""
    for x in range(random.randint(3,6)):
        song += alphabet[random.randint(0,24)]
    name = str(counter+startingNumber)+'.txt'  # Name of text file coerced with +.txt
    try:
        file = open(name,'w+')   # Trying to create a new file or open one
    except:
        print('Something went wrong! Cant tell what?')
    file.write(str(song))
    file.close()
    print(f"{counter}/{userInput}")
    counter+=1
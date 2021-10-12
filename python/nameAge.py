import time

print("what is your name?")
myName = input()

print("Hello " + myName + " Thats a cool name.  How old are you?")
myAge = input()
print(myAge + ' Thats funny, Im only a few seconds old.')

time.sleep (4)


print("I wish I was " + str(int(myAge) * 2) + " years old.")

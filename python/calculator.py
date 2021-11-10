import time

print("What is your name?")
yName = input()

print("Hello " + yName)

time.sleep(4)

def start():
    print("Welcome!")
    time.sleep(2)
    print("This is a simple calculator program")
    time.sleep(2)
    print("Are you ready to begin?")
    time.sleep(4)

    begin = input("""Please enter Y or N""")
    if begin.upper() == 'Y':
       calculator()
    elif begin.upper() == 'N':
       print("Goodbye!  Have a nice day! ")
    else:
        start()
    
def calculator():
    calculation = input("""Please enter the type of calculation you would like to perform:
        1 for addition,
        2 for subtraction,
        3 for multiplication,
        4 for division""")

    firstChoice = float(input('Please enter a number: '))
    secondChoice = float(input('Please enter your next number: '))

    if calculation == '1':
        print('The numbers you entered are {} + {} '.format(firstChoice,secondChoice))
        print(firstChoice + secondChoice)

    elif calculation == '':
            print('The numbers you entered are {} - {} '.format(firstChoice,secondChoice))
            print(firstChoice - secondChoice)

    elif calculation == '3':
            print('The numbers you entered are {} * {} '.format(firstChoice,secondChoice))
            print(firstChoice * secondChoice)

    elif calculation == '4':
            print('The numbers you entered are {} / {} '.format(firstChoice,secondChoice))
            print(firstChoice / secondChoice)

    else:
            print("You have not entered a valid operator, please try again. ")

    go_again()

def go_again():

    #get user input
    another_calculation=input("Do you want to make another calculaion?  Enter Y or N ")

    if another_calculation == "Y":
        calculator()

    elif another_calculation == "y":
        calculator()

    elif another_calculation == "N":
        print("Have a nice day!")

    elif another_calculation == "n":
        print("Have a nice day!")

    else:
        go_again()

start()

# Import the libraries for the time of day and the alarm sound
from datetime import datetime   
from playsound import playsound    

#Validate the user input of the time of day
def properTimeLength(timeOfAlarm):
    if len(timeOfAlarm) != 11:
        return "Your format is incorrect. Please enter your time in this format: hh:mm:ss am/pm."
    else:
        if int(timeOfAlarm[0:2]) > 12:
            return "You have entered and invalid HOUR format! Please try again."
        elif int(timeOfAlarm[3:5]) > 59:
            return "You have entered and invalid MINUTE format! Please try again."
        elif int(timeOfAlarm[6:8]) > 59:
            return "You have entered an invalid SECOND format! Please try again."
        else:
            return "OK. The format is correct."

#Time input being true code
while True:
    timeOfAlarm = input("Please enter your alarm time in the following format: HH:MM:SS am/pm.")
    
    validate = properTimeLength(timeOfAlarm.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"You alarm will be set for {timeOfAlarm}.")
        break

#Set alarm splices
alarm_hour = timeOfAlarm[0:2]
alarm_min = timeOfAlarm[3:5]
alarm_sec = timeOfAlarm[6:8]
alarm_period = timeOfAlarm[9:].upper()

#Etablishing the current time
while True:
    now = datetime.now()

    present_hour = now.strftime("%I")
    present_min = now.strftime("%M")
    present_sec = now.strftime("%S")
    present_period = now.strftime("%p")

#Compare alarm time to present time 
    if alarm_period == present_period:
        if alarm_hour == present_hour:
            if alarm_min == present_min:
                if alarm_sec == present_sec:
                    print("Good Morning Sunshine!")
                    playsound('C:\it3038c-scripts\python\alarm-deep_groove.wav')
                    break
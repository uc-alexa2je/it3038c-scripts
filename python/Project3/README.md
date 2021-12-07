This is a simplified alarm clock program written in python.
It is designed with a fault text tolerance so the time cannot be incorrectly entered.

```
if int(timeOfAlarm[0:2]) > 12:
            return "You have entered and invalid HOUR format! Please try again."
        elif int(timeOfAlarm[3:5]) > 59:
            return "You have entered and invalid MINUTE format! Please try again."
        elif int(timeOfAlarm[6:8]) > 59:
            return "You have entered an invalid SECOND format! Please try again."
        else:
            return "OK. The format is correct."
```
It also error checks to be sure of the correct time format, which is 11 digits including the am/pm entry

```
properTimeLength(timeOfAlarm):
    if len(timeOfAlarm) != 11:
        return "Your format is incorrect. Please enter your time in this format: hh:mm:ss am/pm."
```
Once the time is entered correctly, the alarm time is ran in a nested loop to compare the actual time and when all entries match up, the message 'Good Morning Sunshine!' appears.  I could not get the wav soundbite to play the music but I did include the path with for those who do have to proper media players able to play it.  This is also preceded with a message stating you alarm will ring in 6 seconds if you have the correct media player installed.

Otherwise, it will throw a code and end.  

Although I have change some variables and the structure a little, this is a borrowed program.
from datetime import datetime

currentDay = datetime.now()
date = currentDay.strftime("%d-%m-%Y") + '.txt'
# Create a file to write error message
global f
f = open(date, 'a')

def WriteToFile(message):
    time = datetime.now().strftime("%H:%M:%S")
    f.write(time + '\n')
    f.write(message +'\n')
import smtplib, ssl
from datetime import date
import calendar

port = 465  # For SSL

my_date = date.today()
current_day = calendar.day_name[my_date.weekday()]
print('Current day : ' + current_day)

if(current_day=='Saturday'):
    sender_email = "crazyydeveloper@gmail.com"
    receiver_email = ['yatribhatt15@gmail.com',
                  'karan2399@gmail.com',
                  'parikhhenil@gmail.com',
                  'sharvil12345patel@gmail.com',
                  'shivanisahasrabudhe.17@gmail.com',
                  'ts6202@gmail.com',
                  'riddz.jash@gmail.com',
                  'pankit540@gmail.com']
    message = """\
Subject: Tasks for Sunday

Hello Fellow User,\nThis is crazy developer speaking.\n"""

    message += "Welcome to another awesome saturday.\n\n"

    message += "Below is the task distribution for another fine Sunday: \n\n"
    file = open('tasks.txt')
    names = []
    tasks = []
    for lines in file:
        tempName,tempTask = lines.split(',')
        names.append(tempName)
        tasks.append(tempTask[:-1])

    tasks = [tasks[-1]] + tasks[:-1]


    file.close()

    file = open('tasks.txt','a')
    file.truncate(0)
    for i in range(len(names)):
        message += names[i]+ " => " + tasks[i] + "\n"
        file.write(names[i]+','+tasks[i]+'\n')

    message += "\n\nWe expect your keen cooperation. \n\nThanks & Regards\n"
    message += "Your Own Mr Raval"
    file.close()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, "Qwert@321")
        server.sendmail(sender_email,receiver_email,message)
        print(f"Email sent to {receiver_email}")

    print(message)

import smtplib, ssl
from datetime import date
import calendar

port = 465  # For SSL

my_date = date.today()
current_day = calendar.day_name[my_date.weekday()]
print('Current day : ' + current_day)
sender_email = "crazyydeveloper@gmail.com"
userEmail = {
    'Karan': 'karan2399@gmail.com',
    'Sharvil': 'sharvil12345patel@gmail.com',
    'Henil': 'parikhhenil@gmail.com',
    'Shivani': 'shivanisahasrabudhe.17@gmail.com',
    'Yatri': 'yatribhatt15@gmail.com',
    'Dhaneshwar':'dhaneshwarkoshti@gmail.com',
    'Vishal':'vishalprajapati3535@gmail.com',
    'Zaid':'patelzaid98@gmail.com',
    'Nishi':'nishi.vora@icloud.com'
    }

def sendMail(freq, user, task):
    subject = ""
    content = ""
    if freq == 'w':
        subject = "Your Task for this week!"
        content = "Your this week's task is as follows:"
    elif freq == 'd':
        subject = "Your Task for the day!"
        content = "Your today's task is as follows:"
    message = """\
Subject: {}

Hello {},\nThis is crazy developer speaking.\n""".format(subject, user)

    message += content + "\n"
    message += "\n-------------------------\n" + task + "\n-------------------------\n\n\n"

    message += "We expect your keen cooperation. \n\n\nThanks & Regards\nYour Own Mr Raval"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, "filbojzgnkavvqgi")
        server.sendmail(sender_email,userEmail[user],message)
        print(f"Email sent to {user} at {userEmail[user]}")

    print(message)
    

file = open('tasks.txt')
lines = file.readlines()

weekly_tasks_1 = lines[0].replace("\n","").split(",")
weekly_users_1 = lines[1].replace("\n","").split(",")

weekly_tasks_2 = lines[3].replace("\n","").split(",")
weekly_users_2 = lines[4].replace("\n","").split(",")

daily_tasks_1 = lines[6].replace("\n","").split(",")
daily_users_1 = lines[7].replace("\n","").split(",")

file.close()

print(weekly_tasks_1)
print(weekly_users_1)
print(weekly_tasks_2)
print(weekly_users_2)
print(daily_tasks_1)
print(daily_users_1)


if current_day == 'Saturday':
    weekly_assign = {}

    for i in range(len(weekly_tasks_1)):
        weekly_assign[weekly_users_1[i]] = weekly_tasks_1[i]

    for i in range(len(weekly_tasks_2)):
        for j in range(len(weekly_users_2)):
            if(weekly_users_2[j] not in weekly_assign.keys()):
                weekly_assign[weekly_users_2[j]] = weekly_tasks_2[i]
                break

    for key in weekly_assign.keys():
        sendMail('w', key, weekly_assign[key])

    weekly_users_1 = [weekly_users_1[-1]] + weekly_users_1[:-1]
    weekly_users_2 = [weekly_users_2[-1]] + weekly_users_2[:-1]

daily_assign = {}

for i in range(len(daily_tasks_1)):
    daily_assign[daily_users_1[i]] = daily_tasks_1[i]

for key in daily_assign.keys():
        sendMail('d', key, daily_assign[key])



daily_users_1 = [daily_users_1[-1]] + daily_users_1[:-1]

file = open('tasks.txt','a')
file.truncate(0)

file.write(",".join(weekly_tasks_1))
file.write("\n")
file.write(",".join(weekly_users_1))
file.write("\n")
file.write("\n")
file.write(",".join(weekly_tasks_2))
file.write("\n")
file.write(",".join(weekly_users_2))
file.write("\n")
file.write("\n")
file.write(",".join(daily_tasks_1))
file.write("\n")
file.write(",".join(daily_users_1))
file.write("\n")
file.close();

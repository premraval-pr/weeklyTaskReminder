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
    print(names[i]+"-"+tasks[i])
    file.write(names[i]+','+tasks[i]+'\n')

file.close()

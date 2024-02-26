import csv

with (open('students.csv',encoding= 'utf8') as file):
    answer = list(csv.reader(file,delimiter= ','))[1:]


    sum_class = {}
    count_class = {}


    for id,name,titleProject_id,_class,score in answer:
        if 'Хадаров Владимир' in name:
            print(f'Ты получил: {score} за проект - {titleProject_id}')
            break


    for elem in answer:
        if elem[-1] != 'None':
            sum_class[elem[-2]] = sum_class.get(elem[-2],0) + int(elem[-1])
        count_class[elem[-2]] = count_class.get(elem[-2],0) + 1

# заменяем None на среднее значение по классу

    for elem in answer:
        if elem[-1] == 'None':
            elem[-1] = round(sum_class[elem[-2]]/count_class[elem[-2]],3)

# new file
with open('student_new.scv','w',encoding = 'utf8',newline = '') as file:
    writer = csv.writer(file, delimiter = ',')
    writer.writerow(['id','name','titleProject_id','_class','score'])
    writer.writerows(answer)

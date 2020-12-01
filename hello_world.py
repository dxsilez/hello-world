# while (True):
#     text = input()
#     if (len(text) < 5):
#         print('message is too short for me')
#     else:
#         print('Thanks! text is: ', text)
#         print('Bye!')
#         break

students = ['23','654','65']
students.append('ghja')
students+=['hjklsty']
students+=('prte')
students.insert(2, 'PORTER')
students.remove('23')
del students[2]
for elem in students:
    print(elem + ', length ' + str(len(elem)))
for elem in students:
    print(elem)
if '65' in students:
    print('65 is in students.list')
    print(students.index('PORTER'))
sorted_students = sorted(students) #сортировка
print(sorted_students)
rev_students = sorted_students[::-1] #реверс
print(rev_students)

list1 = [i*i for i in range(50)] #лист квадратов
print(list1)

list2 = [int(i) for i in input().split()] #ввод списка
print(list2)

list3 = [int(i) for i in input().split()]
summary = 0
for i in list3:
    summary += i
print(summary)

# сумма соседей
list4 = [int(j) for j in input().split()]
for i in range(len(list4)):
    if len(list4) == 1:
        print(list4[0])
        break
    elif i == 0:
        print(list4[-1] + list4[1])
    elif i == len(list4)-1:
        print(list4[-2] + list4[0])
    else:
        print(list4[i-1] + list4[i+1])

# встречаются более одного раза
list5 = [int(j) for j in input().split()]
list5.sort()
i_printed = False
prev_elem = list5[0]
for i in range(1,len(list5)):
    if (not i_printed) & (list5[i] == prev_elem):
        print(list5[i])
        i_printed = True
    elif i_printed & (list5[i] == prev_elem):
        continue
    else:
        prev_elem = list5[i]
        i_printed = False


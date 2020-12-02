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

#генерирум матрицу 5*5 из нулей
n = 5
a = [[0 for j in range(n)] for i in range(n)]

#когда сумма введённых чисел будет равна нулю вывести сумму квадратов всех введенных чисел
inpLine = []
i = 0
summa = 0
while True:
    inpLine.append(int(input()))
    summa += inpLine[i]
    if summa == 0:
        for elem in inpLine:
            summa += elem*elem
        print(summa)
        break
    else:
        i += 1

#вывод N символов последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 и тд
N = int(input())
list6 = [1]
for i in range(2, N):
    for _j in range(i): # подчеркивание при _j - т.к. j дальше нигде не используется
        list6.append(i)
    if len(list6) > N:
        break
print(*list6[0:N]) # Звездочка - вывод элементов списка через пробел


#поиск числа в списке и вывод его позиций
list7 = [int(j) for j in input().split()]
x = int(input())
flag = False
i = 0
for elem in list7:
    if elem == x:
        print(i, end=' ')
        flag = True
        i += 1
    else:
        i += 1
        continue
if not flag:
    print('Отсутствует')
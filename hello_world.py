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
sorted_students = sorted(students)
print(sorted_students)


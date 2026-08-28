student = {'name': 'John', 'age': 25, 'courses': ['Physics', 'CompSci']}

'''
print(student)
#print(student['courses'])
#print(student['phone'])
print(student.get('name'))
print(student.get('phone', 'Not Found'))
'''
student['phone'] = '555-555-5555'
student['name'] = 'Jane'

student.update({'name': 'Jane', 'age': 26, 'courses': ['Physics', 'CompSci'], 'phone': '555-555-5555'})
print(student)
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

    
billy = {
    'name' : 'Billy',
    'grades' : [100, 80, 67, 100, 89],
    'attendance': [True, True, True, True, True]
}

sarah = {
    'name' : 'Sarah',
    'grades': [0, 99 , 0, 100, 0],
    'attendance': [True, False, True, False, True]
}

ben = {
    'name' : 'Ben',
    'grades': [60, 82 , 71, 92, 100],
    'attendance': [False, False, False, False, False]
}

students = {'1': billy, '2': sarah, '3': ben}
# Get Number of students keys
print(len(students))

# Get all students id
print(students.keys())

#iterate over students
for k in students:
    print('key',  k)

#Get billy's attendance
billy = students['1']
print(billy['attendance'])

#Get sarah's attendance
sarah = students['2']
print(sarah.get('grades'))

#Get ben's attendance
ben = students['3']
items = ben.items()

for k, val in items:
    print('key',  val)

#get average student grade for all assignments
grades = []
items = students.items()
for key,val in items:
    for g in val['grades']:
        grades.append(g)

#avarage grade
print(round(sum(grades)/ len(grades)))

#another way to do this
grades_concatenated = []
items = students.items() # key pairs for studants
for key, val in items:
    grades_concatenated += val['grades'] #concatenate list of grades

#avarage grade
print(round(sum(grades_concatenated)/ len(grades_concatenated)))
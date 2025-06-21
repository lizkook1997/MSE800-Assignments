names=['v', 'jk', 'rm', 'jin', 'suga', 'jhope', 'jiminaa']
ages= [30,27,29,32,30,29,28]
grades = ['A', 'A', 'A+', 'A', 'B+', 'B', 'C']


paired = dict(zip(names,ages))
print(paired)

students = dict(zip(names, zip(ages, grades)))

for name, (age, grade) in students.items():
    print(f"{name} - Age: {age}, Grade: {grade}")
#   print(list(students.keys()))
# for i, name in enumerate(names):
#     print(i, name)
# %%


# %%
# extract information with age greater than 25 from the following list of dictionaries
data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]

for person in data:
    if person['age'] > 25:
        print(person)


# %%
# use list comprehension to flatten the matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [num for row in matrix for num in row]

print(flat)


# %%


# %%
# use enumerate() for looping to add 5 extra point to each grade in the list, the 5th one add 10 
grades = [88, 92, 78, 65, 50, 94]

for i, grade in enumerate(grades):
    if i == 4:
        grades[i] = grade + 10
    else:
        grades[i] = grade + 5

print(grades)


# %%


# %%


# %%
# filter out elements depend on their index: 
# use list comprehension and enumerate() to get elements with even index
data = [100, 200, 300, 400, 500]

result = [value for index, value in enumerate(data) if index % 2 == 0]

print(result)


# %%


# %%


# %%
# create a dictionary from lists using zip()
keys = ['name', 'age', 'grade']
values = ['Alice', 25, 'A']

result = dict(zip(keys, values))

print(result)

# %%


# %%


# %%
# sort the dictionary based on the ages using lambda
students = [
    {'name': "John", 'grade': "A", 'age': 20}, 
    {'name': "Jane", 'grade': "B", 'age': 21}, 
    {'name': "Joss", 'grade': "A+", 'age': 19}, 
    {'name': "Jack", 'grade': "A-", 'age': 16}, 
    {'name': "Dave", 'grade': "C", 'age': 25}, 
]

sorted_students = sorted(students, key=lambda x: x['age'])

print(sorted_students)

# %%


# %%


# %%
# Sort by age, then by salary if ages are the same
# use lambda
employees = [
    {'name': 'Alice', 'age': 30, 'salary': 80000},
    {'name': 'Bob', 'age': 25, 'salary': 50000},
    {'name': 'Charlie', 'age': 35, 'salary': 120000},
]

sorted_employees = sorted(employees, key=lambda x: (x['age'], x['salary']))

print(sorted_employees)

# %%


# %%


# %%
# Generators are highly useful in data-heavy applications:

# Reading Large Files: Use generators to read large files line by line without loading the entire file into memory.
# Data Streaming: Stream data entries for real-time data processing.
# Large Calculations: Break down massive calculations into smaller, more manageable chunks.

# %%


# %%


# %%


# %%


# %%




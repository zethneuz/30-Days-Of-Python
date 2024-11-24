## 💻 Exercises: Day 8
#1. Create  an empty dictionary called dog
dog = {}
#2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Whitey'
dog['color'] = 'Black'
dog['breed'] = 'Aspin'
dog['legs'] = '8'
dog['age'] = '99'
print(dog)
#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student['first_name'] = 'Student A'
student['last_name'] = 'Pedro'
student['gender'] = 'Male'
student['age'] = '99'
student['marital_status'] = 'Single'
student['skills'] = 'Eating'
student['country'] = 'Ph'
student['city'] =  'Makati'
student['address'] =  'Tinio St.'
print(student)
#4. Get the length of the student dictionary
print(len(student))
#5. Get the value of skills and check the data type, it should be a list
print(type(student['skills']))
#6. Modify the skills values by adding one or two skills
student['skills'] = ['Eating', 'Sleeping', 'Coding']
print(student['skills'])
#7. Get the dictionary keys as a list
print(list(student.keys()))
#8. Get the dictionary values as a list
print(list(student.values()))
#9. Change the dictionary to a list of tuples using _items()_ method
list = list(student.items())
print(list)
#10. Delete one of the items in the dictionary
student.pop('skills')
#11. Delete one of the dictionaries
student.pop('address')
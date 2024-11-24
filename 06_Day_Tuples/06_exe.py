### Exercises: Level 1

#1. Create an empty tuple
tuple1 = ()
#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
tuple2 = ('Emily', 'Sarah', 'Michael', 'William')
#3. Join brothers and sisters tuples and assign it to siblings
brothers = ('Michael', 'William')
sisters = ('Emily', 'Sarah')
siblings = brothers + sisters
print(siblings)
#4. How many siblings do you have?
print(len(siblings))
#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('John', 'Mary')
print(family_members)

### Exercises: Level 2

#1. Unpack siblings and parents from family_members
#(siblings, parents)  = family_members
#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'potato', 'onion')
animal_products = ('milk', 'eggs', 'meat')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
#3. Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt[1:3])
#5. Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[:3])
#6. Delete the food_staff_tp tuple completely
del food_stuff_tp
#7. Check if an item exists in  tuple:
print('apple' in food_stuff_tp)

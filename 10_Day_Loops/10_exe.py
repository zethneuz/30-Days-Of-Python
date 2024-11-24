### Exercises: Level 1

#1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
   print(i)
#2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
   print(i)
   
exit
#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
   #```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   #```

def print_triangle(size):
    for i in range(size):
        print('*' * (i+1))

# Call the function with an argument of 7 to print the same triangle
print_triangle(7)

#4. Use nested loops to create the following:
#   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
#   ```


# Number of rows
rows = 8
# Number of columns
columns = 13

# Outer loop for each row
for i in range(rows):
    # Inner loop for each column
    for j in range(columns):
        # Print '#' followed by a space, without a newline
        print('#', end=' ')
    # Print a newline after each row
    print()
#5. Print the following pattern:

 #  ```sh
"""    0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100 """
  # ```

for i in range(11):
    print(f"{i} x {i} = {i * i}")

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.#
var = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in var:
    print(i)

"""7. Use for loop to iterate from 0 to 100 and print only even numbers"""
for i in range(101):
    if i % 2 > 0 :
      continue
    print(i)

"""8. Use for loop to iterate from 0 to 100 and print only odd numbers"""
for i in range(101):
    if i % 2 > 0 :
      print(i)
    

### Exercises: Level 2
    
""" 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers."""

"""  
```sh
   The sum of all numbers is 5050.
```
"""
var=0
for i in range(101):
    var=var+i

print(var)


"""1. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

    ```sh
    The sum of all evens is 2550. And the sum of all odds is 2500. 
    ```
"""
#even
var=0
for i in range(101):
    if i % 2 > 0 :
      continue
    var=var+i
print(var)

#odd
var=0
for i in range(101):
    if i % 2 > 0 :
      var=var+i    
print(var)

### Exercises: Level 3

#1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.

#1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits=['banana', 'orange', 'mango', 'lemon']
for i in reversed(fruits):
   print(i)

#2. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file. 
    #1. What are the total number of languages in the data
    #2. Find the ten most spoken languages from the data
    #3. Find the 10 most populated countries in the world
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


#Exercises: Level 1
#Find the length of the set it_companies
print(len(it_companies))
#Add 'Twitter' to it_companies
print(it_companies)
it_companies.add('Twitter')
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
it_companies.update({'Tesla', 'Amazon', 'Microsoft', 'Google', 'Facebook'})
print(it_companies)
#Remove one of the companies from the set it_companies
print(it_companies)
it_companies.remove('Google')
print(it_companies)
#What is the difference between remove and discard
#Remove will raise an error if the item is not in the set, discard will not

#Level 2
#1 Join A and B
mekus = A.union(B)
print(mekus)

#2 Find A intersection B
intersect = A.intersection(B)     # {'o', 'n'}
print(intersect)

#3 Is A subset of B
v_subset = A.issubset(B)     # {'o', 'n'}
print(v_subset)


#4 Are A and B disjoint sets
v_disjoint = A.isdisjoint(B)     # {'o', 'n'}
print(v_subset)

#5 Join A with B and B with A
mekus = A.union(B)
mekus_mekus = B.union(A)
print(mekus)
print(mekus_mekus)

#6 What is the symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print(sym_diff)


#7 Delete the sets completely

del A
del B
del it_companies
del age

# LIST COLLECTION ARRAY

animals_con = ['dog', 'cat', 'dog', 'fish', 'rabbit']
print(animals_con[4])  # INDEX

# LIST ARE CHANGABLE
animals_con[1] = 'turkey'
print(animals_con)  # ['dog', 'turkey', 'dog', 'fish', 'rabbit']

animals_con.append('horse')  # append adds to the list
print(animals_con)
# slicing -- printing a particular amount
print(animals_con[1:4])  # the end is not included ie rabbit wont be included
print(animals_con[:3])  # 0 to 2 dog, turkey, dog
print(animals_con[2:])  # 2 to last dog, fish, rabbit, horse
print(len(animals_con))  # prints length

# negative indexing
print(animals_con[-4:])
stored = animals_con[-4:-2]  # we need to use the stored method
print(stored)

print(type(animals_con))  # <class 'list'>
animals_con.clear()  # clears the list
print(animals_con)  # []
animals_con.extend(['dog', 'cat', 'dog', 'fish', 'rabbit'])  # adds to the list
copy_list = animals_con.copy()  # copies the list
print(copy_list)  # ['dog', 'cat', 'dog', 'fish', 'rabbit']
animals_con.extend(copy_list)  # adds the copy list to the original list
# ['dog', 'cat', 'dog', 'fish', 'rabbit', 'dog', 'cat', 'dog', 'fish', 'rabbit']
print(animals_con)
# counts the number of times dog appears in the list
stored_count = animals_con.count('dog')
print(stored_count)
animals_con.remove('dog')  # removes the first instance of dog
# ['cat', 'dog', 'fish', 'rabbit', 'dog', 'cat', 'dog', 'fish', 'rabbit']
print(animals_con)
animals_con.pop(1)  # removes the second element in the list
# ['cat', 'fish', 'rabbit', 'dog', 'cat', 'dog', 'fish', 'rabbit']
print(animals_con)
position = animals_con.index("rabbit")  # returns the index of rabbit
print('The first position ', position)  # 2
animals_con.insert(2, 'goat')  # inserts goat at index 2
# ['cat', 'fish', 'goat', 'rabbit', 'dog', 'cat', 'dog', 'fish', 'rabbit']
print(animals_con)

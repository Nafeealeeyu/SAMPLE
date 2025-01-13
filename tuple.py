#TUPLE METHODS 
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found

new_list = []
fruit_tuple = ('apple', 'banana', 'mango', 'guava', 'mango', 'pineapple', False, True)
print(fruit_tuple[1])
# convert from tuple to a list
convert_list = list(fruit_tuple)
convert_list[3] = 'melon'
# converting from list to tuple
fruit_tuple = tuple(convert_list)
print('new result : ', fruit_tuple, 'length of my tuple is : ', len(fruit_tuple))
print('mango' in fruit_tuple)
print('mango' not in fruit_tuple)
if 'mango' in fruit_tuple:
    print('yes mango is a member of fruit')
else:
    print('mango is not a member of fruit')
if 'apple' in fruit_tuple:
    fruit_tuple = list(fruit_tuple)
    change_false = int(fruit_tuple[6])
    change_true = int(fruit_tuple[7])
    print(change_false, change_true)  # prints 0, 1

    if 'apple' in fruit_tuple:
        fruit_tuple = list(fruit_tuple)
        change_false = int(fruit_tuple[6])
        change_true = int(fruit_tuple[7])
        fruit_tuple[6] = change_false
        fruit_tuple[7] = change_true
        fruit_tuple = tuple(fruit_tuple)
        print(fruit_tuple)
else:
    print(False)
print(fruit_tuple.count("mango"))
print(fruit_tuple.index("pineapple"))

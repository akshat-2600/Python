# Set Based Practice Problem :
'''Q1 Create a set with integers from 1 to 5.'''

my_set = set()
for i in range(1,6) :
    my_set.add(i)
print("Set with integers from 1 to 5 :", my_set)
Set with integers from 1 to 5 : {1, 2, 3, 4, 5}
'''Q2 Add an element to a set.'''

my_set = eval(input("Enter a set :"))
element = eval(input("Enter a element to add in set :"))
my_set.add(element)
print("Set after adding element :", my_set)
Set after adding element : {'Berlin', 'Rio', 'Tokyo', 'Paris'}
'''Q3 Remove an element from a set.'''

my_set = eval(input("Enter a set :"))
element = eval(input("Enter a element to remove from set :"))
my_set.remove(element)
print("Set after removing element :", my_set)
Set after removing element : {'Berlin', 'Tokyo', 'Paris'}
'''Q4 Check if an element exists in a set.'''

my_set = eval(input("Enter a set :"))
element = eval(input("Enter an element to check it's existence :"))
if element in my_set :
    print(f"{element} exists in set")
else :
    print(f"{element} does not exist in set")
Tokyo exists in set
'''Q5 Find the length of a set without using the `len()` function.'''

my_set = eval(input("Enter a set :"))
count = 0
for i in my_set :
    count += 1
print("Length of set :", count)     
Length of set : 4
'''Q6 Clear all elements from a set.'''

my_set = eval(input("Enter a set :"))
my_set.clear()
print("Set after clearing all elements :", my_set)
Set after clearing all elements : set()
'''Q7 Create a set of even numbers from 1 to 10.'''

my_set = set()
for i in range(1,11) :
    if i%2 == 0 :
        my_set.add(i)
print("Set of even numbers from 1 to 10 :", my_set)
Set of even numbers from 1 to 10 : {2, 4, 6, 8, 10}
'''Q8 Create a set of odd numbers from 1 to 10.'''

my_set = set()
for i in range(1,11) :
    if i%2 != 0 :
        my_set.add(i)
print("Set of odd numbers from 1 to 10 :", my_set)
Set of odd numbers from 1 to 10 : {1, 3, 5, 7, 9}
'''Q9 Find the union of two sets.'''

my_set_1 = eval(input("Enter 1st set :"))
my_set_2 = eval(input("Enter 2nd set :"))
union = my_set_1.union(my_set_2)
print("Union of two sets :", union)
Union of two sets : {1, 2, 3, 4, 5, 6, 7}
'''Q10 Find the intersection of two sets.'''

my_set_1 = eval(input("Enter 1st set :"))
my_set_2 = eval(input("Enter 2nd set :"))
intersection = my_set_1.intersection(my_set_2)
print("Union of two sets :", intersection)
Union of two sets : {2, 4, 5, 6}
'''Q11 Find the difference between two sets.'''

my_set_1 = eval(input("Enter 1st set :"))
my_set_2 = eval(input("Enter 2nd set :"))
difference = my_set_1.difference(my_set_2)
print("Union of two sets :", difference)
Union of two sets : {3}
'''Q12 Check if a set is a subset of another set.'''

my_set_1 = eval(input("Enter a set :"))
my_set_2 = eval(input("Enter another set :"))
if my_set_1.issubset(my_set_2) :
    print(f"{my_set_1} is a subset of {my_set_2}")
elif my_set_2.issubset(my_set_1) :
    print(f"{my_set_2} is a subset of {my_set_1}")
else :
    print("No set is a subset of another")
{3, 4, 5} is a subset of {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
'''Q13 Check if a set is a superset of another set.'''

my_set_1 = eval(input("Enter a set :"))
my_set_2 = eval(input("Enter another set :"))
if my_set_1.issuperset(my_set_2) :
    print(f"{my_set_1} is superset of {my_set_2}")
elif my_set_2.issuperset(my_set_1) :
    print(f"{my_set_2} is superset of {my_set_1}")
else :
    print("No set is superset of another")
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} is superset of {3, 4, 5}
'''Q14 Create a set from a list.'''

lst = eval(input("Enter a list :"))
my_set = set(lst)
print("Conversion of list to set :", my_set)
Conversion of list to set : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
'''Q15 Convert a set to a list.'''

my_set = eval(input("Enter a set :"))
lst = list(my_set)
print("Conversion of set to list :", lst)
Conversion of set to list : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''Q16 Remove a random element from a set.'''

import random

my_set = eval(input("Enter a set :"))
element = random.choice(list(my_set))
my_set.remove(element)
print("Set after removing random element :", my_set)
Set after removing random element : {1, 2, 3, 4, 6, 7, 8, 9, 10}
'''Q17 Pop an element from a set.'''

my_set = eval(input("Enter a set :"))
element_popped = my_set.pop()
print("Popped element :", element_popped)
print("Set after popping out an element :", my_set)
Popped element : 1
Set after popping out an element : {2, 3, 4, 5, 6, 7, 8, 9, 10}
'''Q18 Check if two sets have no elements in common.'''

my_set_1 = eval(input("Enter 1st set :"))
my_set_2 = eval(input("Enter 2nd set :"))
result = my_set_1.intersection(my_set_2)
            
if result :
    print("Both sets have some common elements")
else :
    print("Both sets have no common elements")
Both sets have no common elements
'''Q19 Find the symmetric difference between two sets.'''

my_set_1 = eval(input("Enter 1st set :"))
my_set_2 = eval(input("Enter 2nd set :"))
sym_diff = my_set_1.symmetric_difference(my_set_2)
print("Symmetric difference :", sym_diff)
Symmetric difference : {1, 2, 4, 6, 8, 9, 10}
'''Q20 Update a set with elements from another set.'''

my_set_1 = eval(input("Enter 1st set :"))
my_set_2 = eval(input("Enter 2nd set :"))
my_set_1.update(my_set_2)
print(f"Set after updation {my_set_1}")
Set after updation {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15}
'''Q21 Create a set of the first 5 prime numbers.'''

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1) :
        if num % i == 0 :
            return False
    return True

n = int(input("Enter number of first prime numbers you want(max 100) :"))
prime_num_lst = [num for num in range(2, 100) if check_prime(num)][:n]

print("Tuple of the first 5 prime numbers:", set(prime_num_lst))
Tuple of the first 5 prime numbers: {2, 3, 5, 7, 11}
'''Q22 Check if two sets are identical.'''

my_set_1 = eval(input("Enter 1st set :"))
my_set_2 = eval(input("Enter 2nd set :"))
if my_set_1 == my_set_2 :
    print("Both sets are identical")
else :
    print("Both sets are not identical")
Both sets are identical
'''Q23 Create a frozen set.'''

lst = eval(input("Enter a list :"))
frozen_set = frozenset(lst)
print("Frozen Set :", frozen_set)
Frozen Set : frozenset({2, 4, 6, 8, 10})
'''Q24 Check if a set is disjoint with another set.'''

my_set_1 = eval(input("Enter 1st set :"))
my_set_2 = eval(input("Enter 2nd set :"))
if my_set_1.isdisjoint(my_set_2) :
    print("Given sets are disjoint")
else :
    print("Given sets are not disjoint")
Given sets are disjoint
'''Q25 Create a set of squares of numbers from 1 to 5.'''

my_set = set(map(lambda i : i**2 , (j for j in range(1,6))))
print("Set of squares of numbers from 1 to 5 :", my_set)
Set of squares of numbers from 1 to 5 : {1, 4, 9, 16, 25}
'''Q26 Filter out all even numbers from a set.'''

my_set = eval(input("Enter a set :"))
even_set = set()
for i in my_set :
    if i%2 == 0 :
        even_set.add(i) 

print("Set of even numbers :", even_set)
Set of even numbers : {2, 4, 6, 8, 10}
'''Q27 Multiply all elements in a set by 2.'''

my_set = eval(input("Enter a set :"))
mult_set = set(map(lambda i : i*2 , my_set))
print("Set after updation :", mult_set)
Set after updation : {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
'''Q28 Create a set of random numbers.'''

import random 

my_set = set()
n = int(input("Enter length of set which you want :"))
for i in range(n) :
    my_set.add(random.randint(1,100))

print("Set of random numbers :", my_set)
Set of random numbers : {32, 28, 89, 92, 25}
'''Q29 Check if a set is empty.'''

my_set = eval(input("Enter a set :"))
if len(my_set) == 0 :
    print("Set is empty")
else :
    print("Set is not empty")
Set is empty
'''Q30 Create a nested set (hint: use frozenset).'''

my_set_1 = eval(input("Enter 1st set"))
my_set_2 = eval(input("Enter 2nd set"))

frozen_set_1 = frozenset(my_set_1)
frozen_set_2 = frozenset(my_set_2)
nested_set = {frozen_set_1, frozen_set_2}

print("Nested set:", nested_set)
Nested set: {frozenset({2, 4, 6, 8, 10}), frozenset({1, 2, 3, 4, 5})}
'''Q31 Remove an element from a set using the discard method.'''

my_set = eval(input("Enter a set :"))
element = int(input("Enter element which you want to discard :"))
my_set.discard(element)
print("Set after removing an element :", my_set)
Set after removing an element : {1, 2, 3, 4, 6, 7, 8, 9, 10}
'''Q32 Compare two sets.'''

my_set_1 = eval(input("Enter 1st set :"))
my_set_2 = eval(input("Enter 2nd set :"))

check_subset = my_set_1.issubset(my_set_2)
check_superset = my_set_1.issuperset(my_set_2)
check_intersection = my_set_1.intersection(my_set_2)
union = my_set_1.union(my_set_2)
difference_1 = my_set_1.difference(my_set_2)
difference_2 = my_set_2.difference(my_set_1)

print("Set 1:", my_set_1)
print("Set 2:", my_set_2)
print("Is set 1 a subset of set 2?", check_subset)
print("Is set 2 a subset of set 1?", check_superset)
print("Intersection:", check_intersection)
print("Union:", union)
print("Elements in set 1 but not in set 2:", difference_1)
print("Elements in set 2 but not in set 1:", difference_2)
Set 1: {1, 2, 3, 4, 6}
Set 2: {1, 2, 3, 4, 5}
Is set 1 a subset of set 2? False
Is set 2 a subset of set 1? False
Intersection: {1, 2, 3, 4}
Union: {1, 2, 3, 4, 5, 6}
Elements in set 1 but not in set 2: {6}
Elements in set 2 but not in set 1: {5}
'''Q33 Create a set from a string.'''

string = input("Enter a string :")
print("Conversion of string to set :", set(string))
Conversion of string to set : {'t', '.', 's', 'k', 'M', 'a', 'n', 'i', 'y', 'h', 'S', ' ', 'm', 'A', 'e', 'x'}
'''Q34 Convert a set of strings to a set of integers.'''

str_set = eval(input("Enter a set of strings :"))
set_int = set(map(lambda i : int(i) , list(str_set)))
print("Conversion of set of strings to set of integers :", set_int)
Conversion of set of strings to set of integers : {1, 2, 3, 4}
'''Q35 Convert a set of integers to a set of strings.'''

int_set = eval(input("Enter a set of integers :"))
set_str = set(map(lambda i : str(i) , list(int_set)))
print("Conversion of set of integers to set of strings :", set_str)
Conversion of set of integers to set of strings : {'4', '1', '2', '3'}
'''Q36 Create a set from a tuple.'''

tup = eval(input("Enter a tuple :"))
my_set = set(tup)
print("Set from a tuple :", my_set)
Set from a tuple : {1, 2, 3, 4, 5}
'''Q37 Convert a set to a tuple.'''

my_set = eval(input("Enter a set :"))
tup = tuple(my_set)
print("Tuple from a set :", tup)
Tuple from a set : (1, 2, 3, 4, 5, 6)
'''Q38 Find the maximum value in a set.'''

my_set = eval(input("Enter a set :"))
lst = list(my_set)
max_num = max(lst)
print("Maximum value in set :", max_num)
Maximum value in set : 89
'''Q39 Find the minimum value in a set.'''

my_set = eval(input("Enter a set :"))
lst = list(my_set)
min_num = min(lst)
print("Minimum value in set :", min_num)
Minimum value in set : 1
'''Q40 Create a set from user input.'''

my_set = eval(input("Enter a set :"))
print("Set :", my_set)
Set : {1, 3, 4, 5, 6, 7, 23, 89}
'''Q41 Check if the intersection of two sets is empty.'''

my_set_1 = eval(input("Enter 1st set :"))
my_set_2 = eval(input("Enter 2nd set :"))
if my_set_1.intersection(my_set_2) :
    print("Inbtersection of two sets is not a empty set")
else :
    print("Inbtersection of two sets is a empty set")
Inbtersection of two sets is a empty set
'''Q42 Create a set of the first 5 Fibonacci numbers.'''

n = int(input("Enter number of Fibonacci numbers you want in set (n +1) :"))
x , y = 0 , 1  # initializing first two fibonacci numbers
fib_set = set()
for i in range(n) :
    fib_set.add(x)
    x , y = y , x+y

print(f"Set of first {n} Fibonacci numbers : {fib_set}")    
Set of first 6 Fibonacci numbers : {0, 1, 2, 3, 5}
'''Q43 Remove duplicates from a list using sets.'''

lst = eval(input("Enter a list :"))
dup_set = set(lst)
remove_duplicated_lst = list(dup_set)
print("List after removing duplicate values :", remove_duplicated_lst)
List after removing duplicate values : [1, 2, 3, 5, 6, 7, 8, 55]
'''Q44 Check if two sets have the same elements, regardless of their count.'''

my_set_1 = eval(input("Enter 1st set :"))
my_set_2 = eval(input("Enter 2nd set :"))

sorted_lst_1 = sorted(list(my_set_1))
sorted_lst_2 = sorted(list(my_set_2))


if sorted_lst_1 == sorted_lst_2 :
    print("Both sets have the same elements")
else:
    print("Both sets do not have the same elements")
Both sets have the same elements
'''Q45 Create a set of the first `n` powers of 2.'''

n = int(input("Enter number of powers of n you want :"))
my_set = set()
for i in range(n) :
    my_set.add(2**i)
print(f"Set of first {n} powers of 2 : {my_set}")
Set of first 10 powers of 2 : {32, 1, 2, 64, 4, 128, 256, 512, 8, 16}
'''Q46 Find the common elements between a set and a list.'''

my_set = eval(input("Enter a set :"))
lst = eval(input("Enter a list :"))
print("Common elements between set and list :")
for i in my_set :
    for j in lst :
        if i == j :
            print(i)            
Common elements between set and list :
3
5
7
9
'''Q47 Create a set of the first `n` triangular numbers.'''

def triangular_numbers(n) :
    return [i * (i+1) // 2 for i in range(1,n+1)]

n = int(input("Enter number of first n triangular numbers you want :"))
lst = triangular_numbers(n)
print(f"Set of the first {n} triangular numbers : {set(lst)}")
Set of the first 6 triangular numbers : {1, 3, 6, 10, 15, 21}
'''Q48 Check if a set contains another set as a subset.'''

my_set_1 = eval(input("Enter a set :"))
my_set_2 = eval(input("Enter another set :"))
if my_set_1.issubset(my_set_2) :
    print(f"{my_set_1} is a subset of {my_set_2}")
elif my_set_2.issubset(my_set_1) :
    print(f"{my_set_2} is a subset of {my_set_1}")
else :
    print("No set is a subset of another")
{2, 3, 4} is a subset of {1, 2, 3, 4, 5, 6, 7, 8}
'''Q49 Create a set of alternating 1s and 0s of length `n`.'''

n = int(input("Enter length of set you want :"))
my_set = set()
for i in range(n) :
        my_set.add(1)
        if len(my_set) == n :
            break
        else :
            my_set.add(0)

print(f"Set of alternating 1s and 0s of length {n} : {my_set}")
Set of alternating 1s and 0s of length 10 : {0, 1}
'''Q50 Merge multiple sets into one.'''

my_set_1 = eval(input("Enter 1st set :"))
my_set_2 = eval(input("Enter 2nd set :"))
my_set_3 = eval(input("Enter 3rd set :"))

merge = my_set_1.union(my_set_2 , my_set_3)
print("Merged sets :", merge)
Merged sets : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

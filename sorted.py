#Sorting any sequence is very easy in Python using bulit-in method sorted()
#Sorted() sorts any sequence(list, tuple) and always
# returns a list with the elements in sorted manner,
#without modifying the original sequence.
#sorted(iterable, key（optional）, reverse(optional))
#iterable: sequence(list, tuple, string) or collection(dictionary, set, frozenset) or any other
#iterator needs to be sorted
#key(optional): a funtion that would server as a key or a basis of sort comparison
#reverse(optional): if set true, then the iterable would be sorted in reverse order, by default false.


#List
x = ['w', 'o', 'a', 'i', 'n', 'i']
print(sorted(x))

#Tuple
x = ('w', 'o', 'a', 'i', 'n', 'i')
print(sorted(x))

#String
x = "python"
print(sorted(x))

#Dictionary
x = {'w':1, 'o':2, 'a':3, 'i':4, 'n':5, 'i':6}
print(sorted(x))

#Set
x = {'w', 'o', 'a', 'i', 'n', 'i'}
print(sorted(x))

L = ["cccc", "b", "dd", "aaa"]

print(sorted(L))
print(sorted(L, key=len))

a=['Pineapple','pen']
b=['apple','PEN']
print(a)
print(b)
c = a+b
print(c)
print(sorted(c,reverse=True))

print(c)

print(sorted(c, key=lambda x: x[::-1]))


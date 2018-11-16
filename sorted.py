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

#capitial char bigger than lowercase char
a=['Pineapple','pen']
b=['apple','PEN']
print(a)
print(b)
c = a+b
print(c)
print(sorted(c,reverse=True))
print(c)
print(sorted(c, key=lambda x: x[::-1]))

#check if two strings are anaram or not
def check(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

rst = check("listen", "silent")
print(str(rst))

#sort student by age
student_tuples = [
    ('join', 'A', 25),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

print(sorted(student_tuples, key=lambda x: x[2]))

#sort student by age then by name
student_tuples = [
    ('join', 'A', 25),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ('ava', 'B', 10),
]

def f(logs):
    return (logs[2], logs[0])

print(sorted(student_tuples, key=f))








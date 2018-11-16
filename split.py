#str.split(separator, maxsplit)
#split() Parameters
#The split() method takes maximum of 2 parameters:
#separator (optional)- is a delimiter(分隔符，界定符).
# The string splits at this specified separator.
#If is not provided then any white space is a separator.

#maxsplit: it is a number, which tells us to split the string into maximum of provided number of times.
#If it is not provided then there is no limit

#returns a list of strings after breaking the given string by the specified separator.

# The join() method is a string method and
# returns a string in which the elements of sequence have
#been joined by str separator.
#stringf_name.join(iterable)
#It is the name of string in which joined elements of iterable will be stored
import re
text = "qin ai de "
print(text.split())

words = "qin, ai, de"
print(words.split(","))

logs = "QinAiDe"
log = re.findall('[A-Z][a-z]*', logs)
print(" ".join(log))

print(text.split(" ", 0))
print(text.split(" ", 1))
print(text.split(" ", 2))






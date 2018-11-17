#re---regular expression
#the re module provide regular expression matching operations
#Both pattens and strings to be searched can be Unicode strings as well as 8-bit strings

#re.findall(pattern, string, flags=0)
#Returns all non-overlapping matches of pattern in string, as a list of strings.
#The string is scanned left-to-right, and matches are returned in the order found.
#If one or more groups are present in the pattern, return a list of groups
#this is will be a list of tuples if the pattern has more than one group
#empty matches are incuded in the results.
#'^' matches the start of the string, and in MULTILINE mode also matches immediately after each newline
#'|' A|B, where A and B can be arbitrary REs, creates a regular expression that will match either A or B.
#'\w' letters(Match alphanumberic charachter, including "_")
#'[]'used to indicate a set of characters. in a set:
#1. characters can be listed individually, [amk] will match 'a', 'm', or 'k'.
#2. Ranges of characters can be indicated by giving two characters and separating them by a '-',
#[a-z] will match any lowercase ASCII letter
#[0-9] will match any numer
#if it's placed as the first or last character[a-] it will match a literal '-'
#[^5] will match any character excepted '5'
#?
#+ match 1 or more repetition of the preceding RE

import re
print(re.findall(r'^|\w+', 'guru99,education is fun'))
print(re.findall('[A-Z][a-z]*', 'AmIAiNi'))
courses = "Python Training Course for Beginners: 15/Aug/2011 - 19/Aug/2011;Python Training Course Intermediate: 12/Dec/2011 - 16/Dec/2011;Python Text Processing Course:31/Oct/2011 - 4/Nov/2011"
print(re.findall("[A-Z][a-z]*ing", courses))

a = '1253abcd4567efgh8910ijkl'
print(re.findall('(\d+[A-Za-z]+)', a))
print(re.findall('\d+',a))
print(re.findall('[A-Za-z]+', a))

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher blah leet-code@leetcode.com blah liuna.lina@gmail.com'
print(re.findall("[\w\.\-]+@[\w\.]+", str))




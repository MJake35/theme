# This program is uses list slicing to slice out
# the full string to get a new one
"""
create a variable and assign a string
use list slicing to slice out 3 new strings
create a new variable to and the 3 new strings
print out the 3 new added string
return output
""" 
message = ("python is an interpreted, interactive, object-oriented programming language that combines remarkable power with ver clear syntax")
slice1 = message[39:67]
slice2 = message[107:112]
slice3 = message[0:7]
string = slice1 + slice2 + slice3
print(string)

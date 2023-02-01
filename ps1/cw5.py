# this is a python program to print out the first 2,
#  second 2 and middle 2 characters of a string
"""
create a variable for a string
print the first two characters
print the last two characters
print the middle characters
return outputs
"""
msg = 'Enzo Fernandez'
print("First 2:", msg[0:2])
print("Last 2:", msg[-2:])
mid = len(msg)//2
print("Middle elements:", msg[mid:mid+2])

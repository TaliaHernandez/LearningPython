'''
File: Introduction.py
The purpose of this file is to learn how to take in 
input from the cmd line and get to introduce yourself to them!
'''


'''
OUTLINE 
Print some greeting that says hello and your name and print to screen
Now, "what's your name?"
'''

greeting = "Hello! My name is Talia, and I hope you like my program!"
print(greeting)
name = raw_input("What's your name?")
print("Hello %s") %name  

'''
take in num 
add something to it and print 
'''

print("Let's do math")
number = raw_input("what number do you want?")
h = 5
print("Let's add five")
math = h + int(number)
print(math)
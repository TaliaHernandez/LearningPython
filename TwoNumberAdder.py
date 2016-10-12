'''
Take in 2 numbers, save them independently one at a time, add the 
numbers and return answer
'''

'''
greeting = "We are going to do some math together!"
print(greeting)

number = raw_input("Pick the first number: ")
two = raw_input("Pick your second number: ")

print("We will add them together")
addition = int(number) + int(two)
print(addition)
'''


'''
Make a hello greeting, a few questions, and then do some math together
What if I want to set up a split, if yes, then do quesiton 1, if no then question 2
Can I add a pause? like a conversational pause
'''

print("Hello! My name is Mags! I'd like to get to know you better!")
greeting = raw_input("What's your name? ")
	


#Major Questions
raw_input("What is your Major?: ")
major = raw_input("Do you like that major?: ")
print(major)

if major == "yes":
	print "I'm glad to hear that!"

if major == "no" or "NO" or "No" or "nah":
	print "I'm sorry to hear that."

raw_input("What do you like to do in your free time?: ")
print("That sounds really fun :) ")

#Math Game inquiry
print("Do you want to play a game with me? All I can do is math though.") 

#the quesiton
response = raw_input("Is that OK? (TYPE yes OR no):")
if response == "yes" or "Yes" or "yeah":
	print "Great!"
	primary = raw_input("Pick a number: ")
	secondary = raw_input("Pick a second number: ")
	math = int(primary) + int(secondary)
	print("And your fortune is...")
	print(math)
if response == "no" or "NO" or "No":
	print("Let's try again.")

#The stutter
redo = raw_input("Do you want to play a game?:")
if redo == "no": 
	print("I assume you meant yes and missed.")
	primary = raw_input("Pick a number: ")
	secondary = raw_input("Pick a second number: ")
	math = int(primary) + int(secondary)
	print("And your fortune is...")
	print(math)
if redo == "yes":	
	print("Glad to hear it!")
	primary = raw_input("Pick a number: ")
	secondary = raw_input("Pick a second number: ")
	math = int(primary) + int(secondary)
	print("And your fortune is...")
	print(math)	




'''

if statments 
if greeting == "Test":
	print "Compare worked"
	
	if res == yes 
		print ya
	else if res == no
		print sorry
	else 
		repront question and wait for inout
		
'''


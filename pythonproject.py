#This project was completed by Lauren Hernly and Rishabh Mohindroo. 
# This is going to be our code that shows our proposal for our nonflatable basketball.
#we have used multiple comments throughout 
# if statement
nondeflatable_basketball = "Enhanced Performance on the Court"
if nondeflatable_basketball == "Enhanced Performance on the Court":
    print ("Best Basketball on the Market")
print("\n")

# when people used our basketballs their shooting percentages changed by 15%
# variables and constants
X = .15
x = 'shot percentage'

print("\n")

#operators
x = 15
y = 0
print(x > y)

print("\n")

# performing calulations
# if the basketball player's shooting percentage used to be 40 percent, with the new nondeflatable baskeball it could now be atleast what percentage?
print (.40 + .15)
print ('This is the amount the players shooting percentage ends up being with our new and improved basketball.')

print("\n")

#while loop
#while the shot percentages equals one or less than 100 it shows the repetition of increasing possible shot percentages with the deflatable ball. 
condition = 1
while condition < 100:
    print(condition)
    condition += 1
    
print("\n")

#user input and reading input
x = int(input("Your shooting percentage with a standard ball: "))
y = int(input("Your shooting percentage with our Basketball: "))
z = x + y // 2
print(z)

print("\n")


#condtional operator
#syntax
#var=a if condition else b

a=int(input("enter speed of old ball when dribbling: "))
b=int(input("enter speed of nondeflatable ball when dribbling: "))
'''if (a>b):
	print(a,"is greater")
else:
	print(b,"is greater")'''
max=a if a>b else b
print(max,"is greater")

print("\n")
   
#if else statement
new = int(input("Please enter your final score with the new ball after playing a game.: ")) 

print(new) 

old = int(input("Please enter your final score using a regular basketball.: "))
print(old)

if new > old:
	print ("The new ball worked")
else:
	print ("The old ball is better. No new technology needed")
 



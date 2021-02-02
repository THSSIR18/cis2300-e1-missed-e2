################################################################################
# Question 1: First, change MY_WORD to the 7 letter unique word you picked and 
# MY_NUM to the 5 digit number you picked at the beginning of the semester. 
# Then change the code to print a single output that shows MY_NUM followed
# by MY_WORD followed again by MY_NUM with no spaces in between.
# For e.g. for Jane Doe, MY_WORD = 'orchids' and MY_NUM=98712, her output
# should be: 98712orchids98712
################################################################################
MY_WORD = "ferrari"
MY_NUM = 22022
print(str(MY_NUM)+MY_WORD+str(MY_NUM)) 


#check all work in end with other projects

################################################################################
# Question 2: Set X to the same value of MY_NUM from Question 1
# Modify the code below and use conditional branching (if, else, etc.)
# to print the following:
# if X is between 0 and 33333 then print the word: red
# if X is between 33334 and 66666 then print the word: blue
# if X is between 66667 and 99999 then print the word: green
# if none of the above condition matches then print the word: white
# HINT: X = MY_NUM is perfectly ok to set X to the value of MY_NUM
# HINT: You should use a chain of if statements
################################################################################
X = MY_NUM
if 0<=X<=33333:
    print("red")
elif 33334<=X<=66666:
    print("blue")
elif 66667<=X<=99999:
    print("green")
else:
    print("white")


################################################################################
# Question 3: If you mod any number by 2 and get 0 as result, that number is 
# even. Thus, if p contains an int value, and if (p%2) is 0, then p is an
# even number -- otherwise it is an odd number.
# Write code below that prints the count of odd numbers between 0 and your 
# 5 digit number (MY_NUM).
# HINT: You should use a for loop with if statement(s)  nested within
# HINT: You are free to add more variables, if needed.
################################################################################
even_counts = 0
odd_counts = 0

for p in range(0,22023):
    if (p % 2 == 0):
        even_counts+=1 
    else:
        odd_counts+=1
        
print(odd_counts)


################################################################################
# Question 4: Set P to the largest digit in your 5 digit number. For example,
# if your 5 digit number is 88412, then P should be set to 8.
# Calculate and print the value of (P+1) multiplied by itself (P+3) 
# times. As an example if your 5 digit number is 88412, you should print
# the result of multiplying 9 with itself 12 times -- this is also known as
# 9 to the power of 12.
################################################################################
P = 8
print((P+1)**(P+3))



################################################################################
# Question 5: The following code is supposed to find the product of all
# odd numbers between 1 and Q, where Q is your 5 digit number. The code is 
# faulty in various ways. Fix the code, such that the correct result is printed
# out. 
# HINT: you need if statement(s) within your for loop. 
# HINT: You are free to add more variables, if needed.
# HINT: is the range correct and including the full range?
# HINT: is it really calculating product?
################################################################################
product = 1
Q = 84838
for num in range(1,Q):
   if (num % 2 == 0):
        even_counts+=1 
   else:
        odd_counts+=1
        product*=num
    
print(product)

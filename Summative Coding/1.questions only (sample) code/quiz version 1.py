# Introduction, greeting
print (" Welcome to python general knowledge quiz created by Yuto Lam.") # print function to send a message to the user
print (" This is a sample code/ quiz with 5 random questions. You will either to have answer a true or false question or a multiple question. Please enter in the letter corresponding to the answer or the correct answer itself. Enter in t for true and f or false") # print function to send a message to the user
print ("Good Luck") # print function to send a message to the user

# Defining Score variables
x = 0 # variable 's' is the current score for the user
score = x # score = s will be used later in the section at the bottom to report score

# Question One
print("What is 22 + 6 + 4") # prints out the question
answer_1 = input("a)31\nb)32\nc)33\nd)43\n:")
if answer_1.lower() == "c" or answer_1 == "33":
# the 'input' function allows the user to enter in an answer. The asnwer_1 is a string that I defined on my own. 
 #if answer_1.lower() == "c" or answer_1 == "33": # check the user input. Also, the .lower() function makes the user's input a lower case letter.
    #For example if they entered C , it will be inetrepeted as che user can enter the numeric value in this case.
    print("Correct") # this is indented to show that if the user enters either C c or 33, then it will print correct 
    x = x + 1 # since the question is correct the variable will add by one. Since this is the first question, the s= 0 +1 = 1. Now the user's score is 1 if they got the question correct
else:
    print("Incorrect, 12 + 21 is 33") # the else function in this tells the computer to print this line if they entered in something else. For example if they entered a, it is incorrect and this print
    #function will tell the user that they are wrong and the correct answer

# Since this code is meant for readability, and the skeleton is same for each question.  the questions are marked with a comment

# Question Two
print("True or False... The current Prime Minister of Canada is Pierre Elliot Tredeau?")
answer_2 = input(":")
if answer_2.lower() == "false" or answer_2.lower() == "f": # in this case, unlike the first question is a true or false question. instead of the number, there is false value that the person would enter.
    #additionally, there is a .lower() function for both answers incase the user enters F or False
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The current Prime Minster of Canada is Justin Tredeau")

# Question Three
print("Who won Superbowl 42?")
answer_3 = input("a)New England Patriots\nb)New York Giants\nc)Pittsburgh Steelers\nd)Tampa Bay Buccaneers")
if answer_3.lower() == "New York Giants" or answer_3.lower() == "b":
    print("Correct")
    s = s + 1
else:
    print("Incorrect the New York Giants wons Superbowl 42")  

# Question Four
print("Who owns youtube")
answer_4 = input("a)Google\nb)Netflix\nc)The US\nd)It is a private company\n:")
if answer_4.lower() == "a" or answer_4 == "Google":
    print("Correct")
    s = s + 1
else:
    print("Incorrect, Google owns youtube")

# Question Five

print("What is the name of the Spanish islands that lie off the Northwest coast of Africa?")
answer_5 = input("a)Mauritius\nb)Canary Island\nc)The US\nd)It is a private company\n:")
if answer_5.lower() == "a" or answer_5 == "Canary Island":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Google owns youtube")

# Question Six

print("Name the world's largest ocean/sea ?")
answer_5 = input("a)Pacific Ocean\nb)Atlantic Ocean\nc)Arctic Sea\nd)Balkan Sea\n:")
if answer_5.lower() == "a" or answer_5 == "Pacific Ocean":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, the Pacific Ocean is the biggest")

# Question Seven
print("Howm nay Oscars did Katherine Hupburn earn?")
answer_5 = input("a)3\n b)5\nc)4\nd)2\n:")
if answer_5.lower() == "c" or answer_5 == "4":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, she won 4 Oscars")

# Question Eight
print("What color jersey is worn by the winners of each stage of the Tour De France?")
answer_5 = input("a)Bluenb)Goldnc)Red\nd)Yellow\n:")
if answer_5.lower() == "d" or answer_5 == "Yellow":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, the winner wears a yellow jersey")

#Question Nine
print("True or False... Shylock is a character created by William shakespeare")
answer_5 = input(":")
if answer_5.lower() == "t" or answer_5.lower() == "true":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, the Pacific Ocean is the biggest")

#Question Ten
print("On Blue Peter, what was John Noake's dog called?")
answer_5 = input("a)Doggo\nb)Flowers\nc)Shep\nd)Woof\n:")
if answer_5.lower() == "c" or answer_5 == "Shep":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, the John Noake's dog was called Shep")

#Question Eleven
print("What flavour is Cointreau?")
answer_5 = input("a)Orange\nb)AYellow\nc)Clear\nd)Blue\n:")
if answer_5.lower() == "a" or answer_5 == "Orange":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Cointreau are orange in color")

#Question Twelve
print("Na stands for sodium on Periodic Table of Elements")
answer_5 = input(":")
if answer_5.lower() == "t" or answer_5.lower() == "true":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Na stands for sodium")

#Question Thirteen
print("The captial of the state of New Mexico is Albaquerque")
answer_5 = input(":")
if answer_5.lower() == "f" or answer_5.lower() == "false":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, it is Albuquerque")

#Question Fourteen
print("Who is the oldest president to be elected?")
answer_5 = input("a)George W.Bush \nb)Marvin Harrison\nc)Donald Trump\nd)George Washington\n:")
if answer_5.lower() == "c" or answer_5 == "Donald Trump":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Donald Trump was the oldest to be elected as president")
    
#Question Fifteen
print("What electronic camera was created in 1975?")
answer_5 = input("a)Kodak\nb)Canon\nc)Nokia\nd)Bellicose\n:")
if answer_5.lower() == "a" or answer_5 == "Kodak":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Kodak was the first camera to be created, in 1975")


#Total Score
score = float(x / 15) * 100 # this calculate the total score. the score is the variable from before and it has been counting the number of questions correct. the number correct will be
#multiplied by 100 and over 100 to calculate the percentage. the float is there is show that the number might be a decimal.
print(x,"out of 15, that is",score, "%") # at the end, this will print at the score. x = number correct and socre = the percentage. 

print (" Welcome to python general knowledge quiz created by Yuto Lam.")# print out message

print ("Good Luck") # print out message 
print ("At the beginning, you will asked to enter in your last name and the number of times you have played this game so that your source and uniquely be recorded each time in the score.txt file to see you has gotten the highest score and your own history.") 
print ("In this quiz, you will be given 15 questions to answer. You will either have a multiple choice question or you will have a true or false question.")
print ("When you are asked the question, there will be letters in front of each answer. Please enter in that letter in front of the answer of which you think is correct. You can either enter in the uppercase letter or the lowercase letter.  ")

# print out message(s)
name = input("Please Enter your Last Name") # print out message, ask for user last name
regNo = input ("Please enter your registration Number") #print out message, ask for user last name

fileQues = open("questions(s).txt", mode="r", encoding = "utf-8") # ask to open file textfile in same folder. r means to just read the file. # utf-8 used to switch between python and textfile, coverter 
myqbank = fileQues.readlines() # each line will be read from the textfile.
qbank =[] # qbank of question from the texfile will go in here
score = 0 # variable score start at 0
numofQuestions = len(myqbank) # the  number of questions will eual the length of qbank, which is 15. b.c. 15 questions
print ("Hi", name, "Registration #", regNo) # print out message, introduction saying hi
print("You will either to have answer a true or false question or a multiple question")  # print out message
print("Enter ONLY the ALPHABET for the answer")   # print out message


for b in range(len(myqbank)): # b instead of i. find the length of each of the questions and return
    question = myqbank[b].split(";") # the question will be split up with the semicolon
    qbank.append(question) # the questions in qbank from the textfile will be added to the question in the line above 

 

def checkAnswer(xxx,yyy): # the function,  xxx represents the user answer, yyy represents the answer
    answer = yyy[len(question)-1].strip()[0] # the real answer will be stripped from the print statement with the strip # -1 for b.c. list starts at 0
    global score # global variable used throughout the code
    if xxx.lower() == answer: # if the answer is lower
        print("Correct", "\n") # correct is correct
        score = score + 1 # adds one to score if answer is correct
    else: # otherwise
        print("Incorrect! The correct answer is ",yyy[len(question)-1],"\n") # not correct, will print correct answer # lists starts at 0
    
# already explained from version2
for x in range (len(qbank)): # for  loop - as long as their is lenght of questions in qbank do stuff below
    print("Q",x+1) # print the Q for question and x+1 for the question number
    question = qbank[x] # will print questions from  the qbank and the options
    # Select the questions and the options
    for y in range(len(question)-1): # for loop - if , return the length of the real answer # list starts at 0
        print(question[y])    # print out the question
    answer = input(":") # input from the user is placed here
    while len(answer) != 1:# while the length of the asnswer inputted is longer than 1 letter
        print("Wrong Input, select only an alphabet") # ask only for corresponding alphabet as answer
        answer = input(":") # input from the user is placed here    
    checkAnswer(answer,question) # check user input against the real answer
        
fileQues.close() # closes the function 
#Total Score
totalScore = float(score / numofQuestions) * 100 # prints out total score and float shows the decimal percentage calculations
print(score,"out of", numofQuestions, "that is",totalScore, "% correct") # prints out total score with %

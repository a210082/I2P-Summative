import time # import time, sued later 

print (" Welcome to python general knowledge quiz created by Yuto Lam.")
print ("Good Luck")
print (" Welcome to python general knowledge quiz created by Yuto Lam.") #print out message
print ("Good Luck") #print out message
print ("At the beginning, you will asked to enter in your last name and the number of times you have played this game so that your source and uniquely be recorded each time in the score.txt file to see you has gotten the highest score and your own history.") 
print ("In this quiz, you will be given 15 questions to answer. You will either have a multiple choice question or you will have a true or false question.")
print ("When you are asked the question, there will be letters in front of each answer. Please enter in that letter in front of the answer of which you think is correct. You can either enter in the uppercase letter or the lowercase letter.  ")




        

# print out message
name = input("Please Enter your Last Name") # print out message ,with input
regNo = input ("Please enter your registration Number") # print out message, with input

fileQues = open("questions(ss).txt", mode="r", encoding = "utf-8", newline='')
# ope nteh questions(ss) file, mode is r to read and utf-8 is the converter
#between the textfile and the python file
myqbank = fileQues.readlines() # each line will be read from the textfile

qbank =[] #qbank of question from the textfile will go in here
score = 0 # variable score will start at 0
play = True # can start alying as it is equal to true
numofQuestions = len(myqbank) # the number of questions equal the number of 
def checkAnswer(xxx,yyy): # function with xxx = user input yyy= answer key answer
        answer = yyy[len(question)-1].strip()[0] #check
        global score # global variable used all over the code
        if xxx.lower() == answer: # if xxx is correct. lower() because upper and lower case allowed
                # as answer,
            print("Correct", "\n") # then it is correct
            score = score + 1 # add 1 to score if correct
        else: # if not, 
            print("Incorrect! The correct answer is ",yyy[len(question)-1],"\n") # print incorrect and the real answer -1 becuase list start with 0 

print ("Hi", name, "Registration #", regNo) # print out message, with inputs printed
print("You will either to have answer a true or false question or a multiple question") # print out message
print("Enter ONLY the ALPHABET for the answer")# print out message

for b in range(len(myqbank)): # b instead of trad. i find the lengths of each questions and return
        question = myqbank[b].split(";") # tell that questions are split with ; in the txt file
        qbank.append(question) # add the quesiton to the qbank empty set

while play: # when the play is true aka in action and on going do this stuff:
    startTime = time.ctime() # stat time and record as needed later in the leader.txt file
    start = time.time() # start recording time
    for x in range (len(qbank)):# for loop- as long as their is length of questions
        print("Q",x+1) # print Q  and the question number
        question = qbank[x] # will print question from the 1bank and the options
        # Select the questions and the options
        for y in range(len(question)-1): # if, return the length of the real answer
            print(question[y])     # print out the question
        answer = input(":") # # print out message, suer input asked for
        while len(answer) != 1: # if the input is not one character in lenght,
            print("Wrong Input, select only an alphabet") ## print out message
            answer = input(":")     # ask for user input  again
        checkAnswer(answer,question) #check question against the anwer key 
    #Total Score
    end = time.time()# calcualtue the time after answering the last question
    duration = round(end - start) # calulate the time it took 
    totalScore = round((score / numofQuestions) * 100) # calculate total score
    print("***********RESULT**************") # print out message
    print("Name:",name,"RegNo:",regNo)# print out message w/ variables
    print("Start Time:", startTime)# print out message w/ variables
    print("Total Time:", duration, "secs")# print out message w/ variables
    print(score,"out of", numofQuestions, "that is",totalScore, "% correct")# print out message w/ variables
    output = name +"   " + regNo + "   " +startTime + "   " +str(duration)+"-secs" + "   " +str(totalScore)+" %\n"# print out message w/ variables
    result = open("score.txt",mode="a", encoding = "utf-8")# print out message w/ variables #Appending mode, which is used to add new data to the end of the file;
    #that is new information is automatically amended to the end 
    result.write(output) # write in leadertxt
    result.close()#closer leader .txt

    print("\n","*************************************")# print out message 
    print("Do you want to try again? yes or no")# print out message  
    playAgain =  input(":") # ask for input
    if playAgain.lower() == "yes": # if yes
        play = True# loop back to while play Ture
    else:# simple yes or no question
        play = False   #$ if false 
        print("Thank you for participating in this short exam") # say bi

#harderbit with ordering on the leaderboard coding for the leaderboard
fileScore = open("score.txt", mode="r", encoding = "utf-8", newline='') # read data from score.txt # r = read
scorelist = fileScore.readlines() # read the list of the score
finalscorelist = [] # create place to store score
fileScore.close() # close the score file

for xxx in range(len(scorelist)): # lseparate the items in each student score to token in a list. Everyhting is added to the finalscorelist 
        templist = scorelist[xxx].split() 
        finalscorelist.append(templist)
# srots the list with studen'ts score. 8 shows hte postiion of the score on the list
sortlist = sorted(finalscorelist, key=lambda s: s[8], reverse=True) # lamba because there we use unanmed function for a short period of time
leaderboard = open("leader.txt",mode="w", encoding = "utf-8") # writes in the leader text file # w = write
for xxx in range(len(scorelist)): #writes info in specific format
        temp = "   ".join(sortlist[xxx])
        temp = temp + "\n\n"       
        leaderboard.write(temp) 
leaderboard.close() # closer the leader.txt







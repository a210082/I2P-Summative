print (" Welcome to python general knowledge quiz created by Yuto Lam.") # print function to print out message
print (" This is a sample code/ quiz with 5 random questions. You will either to have answer a true or false question or a multiple choice question") #print out messages
# print function to print out message
print ("Good Luck") # print function to print out message

name = input("Please Enter your Last Name:") #input function that asks for the user's name. The name is a variable that will be defined with the user's name. 

qbank = [["What is 22 + 6 + 4","a)31", "b)32","c) 33" ,"d) 43", "c"], # one example equation seprated with commas
         ["The current Prime Minister of Canada is Pierre Elliot Tredeau?","a) True", "b) False", "b"]] # qbank, more condense questions
# this is a list with the questions. qbank variable is defined as the questions. There are only two questions here becuase it is a test file to test the function code. 
def checkAnswer(xxx,yyy): # this is a function and this will check the answer. the xxx and yyy represent the answer
    if xxx.lower() == yyy[len(question)-1]: #this if function makes the xxx value which is the input by the user a lowercase word and the yyy and len returns the length of the object , which in this case is the question
        # if and else function kind of similar to the first code with inocrrect or correct statements 
        print("Correct", "\n") # print out message correct
    else: # if not,
        print("Incorrect! The correct answer is ",yyy[len(question)-1],"\n") # print out the correct answer
    

for x in range (len(qbank)): # for loop - as long as their is length of questions in qbank do stuff below
    print("Q",x+1) # will keep printing Q and the question number
    question = qbank[x] # will print questions separated by [] in the qbank  and the options
    # Select the questions and the options
    for y in range(len(question)-1): # will check against the real answer and -1 is used because lists start with 0
        print(question[y]) #print the quustion fron the qbank
    answer = input(":") # user input for the answer
    checkAnswer(answer,question) # check the user input upon the answer key
        
    
  

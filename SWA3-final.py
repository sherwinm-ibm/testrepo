#Author: Martin Sherwin
#Date: Nov, 2018
#Version: 1.0
#
#Times Table Quiz
#Allow students to test their times tables knowledge

import random

#declare variables
QuestionIsCorrect = 0
QuestionIsIncorrect = 0
lstCorrect = []
lstIncorrect = []
timesTableNumber = 5

def displayWelcome():
# this welcomes the student to the project and gets their name and provides an explanation of what they can expect
    print("Welcome to Time Table Quest\n")
    global studentName
    studentName = input("what's your name? ")
    print(studentName + ", you will be asked 10 random times tables questions.\n")
    print("If you guess the correct answer, you'll be asked another from a higher times tables. ")
    print("If you guess incorrectly, you'll get another question, but from a lower timers table\n")
    print("Good Luck " + studentName + "!!\n")

def Get_Random_Times_Table_Number():
#generates a random number between 0 and 12 for the seed of the time tablke question
    LowerRange = 1
    UpperRange = 12
    Random_Times_Table_Number = random.randint(LowerRange,UpperRange)
    return Random_Times_Table_Number

def RecordAnswer(AnswerType,Question):
#this function performs a number of tasks, whcih maybe should be split into multiple tasks (TODO)
#first off, checks whether the student has either answered correctly of incorrectly
#depending on this will determine whether the times table number and number of correctly answered questions is increased or decreased by 1
    global timesTableNumber
    global QuestionIsCorrect
    global QuestionIsIncorrect
    if AnswerType == "Correct":
        global lstCorrect
        # increment timesTableNumber
        timesTableNumber += 1
        # Increment Number of correct questions
        QuestionIsCorrect += 1
        #record Correct Score
        lstCorrect.append(Question)
    else:
        #decrease timesTableNumber
        timesTableNumber -= 1
        #reduce Number of correct questions
        QuestionIsIncorrect += 1
        #record Incorrect Score
        lstIncorrect.append(Question)

def ShowScore(QuestionNo, ScoreType):
#function to display the students score
    print("Your score #Questions: " + str(QuestionNo) + " #Correct: " + str(QuestionIsCorrect) + " #Incorrect: " + str(QuestionIsIncorrect) )
    if ScoreType == "final":
        print("Correct: \n")
        print(*lstCorrect, sep="\n")
        print("\nIncorrect: \n")
        print(*lstIncorrect, sep="\n")

def DoTimesTables():
    #set up the main loop to ask 10 random times table questions
    for i in range(1, 11):
        #get the random number and record the correct answer
        randomNumber = Get_Random_Times_Table_Number()
        CorrectAnswer = (randomNumber * timesTableNumber)
        questionNumber = ("Question number: " + str(i))
        questionText = (questionNumber + ", What is " + str(randomNumber) + " times " + str(timesTableNumber) + "?")
        questionFull = (questionText + " Answer: " + str(CorrectAnswer))

        # ask a random times table question
        StudentAnswer = int(input("What is " + str(randomNumber) + " times " + str(timesTableNumber) + "?"))
        if StudentAnswer == CorrectAnswer:
            RecordAnswer("Correct", questionFull)
        else:
            RecordAnswer("Incorrect", questionFull)

    ShowScore(i, "final")
    return

#welcome the student
displayWelcome()
DoTimesTables()

#Ask whether the student wqould like another go
TryAgain = str(input("Would you like another attempt? (Enter 'y' to try again) "))
if TryAgain == 'y':
    DoTimesTables()
else:
    'Thank you for trying!'


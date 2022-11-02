


def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1


    for key in questions:
        print("..........................................")
        print(key)
    
        for i in options[question_num-1]:
            print(i)
        guess = input("(A B C or D):").upper()
        guesses.append(guess)


        correct_guesses += check_answer(questions.get(key),guess)
        question_num+=1

    display_score(correct_guesses,guesses)

def check_answer(answer , guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0

def display_score(correct_guesses,guesses):
    print("..........................................")
    print("RESULT")
    print("..........................................")
    print("Answers:", end="")

    for i in questions:
        print(questions.get(i),end = " ")
    print()

    print("Guesses:", end="")
    for i in guesses:
        print(i,end = " ")
    print()
    
    score = int((correct_guesses/len(questions))*100)

    print("Your total score is :"+str(score)+"%")


def play_again():
    response = ("DO you want to play again(Yes/no)?::").lower()
    if response =="yes":
        return True
    else:
        return False



questions = {
    "Who invented zero?":"A",
    "Python is tributed to which comedy group?":"C",
    "Is earth round?":"B",
    "Who created python?":"D"
}

options = [["A. Aryabhatta","B. Backbenchers" , "C. Ramanujan" , "D. Rahul Gandhi"],
        ["A. lonly Island","B. Hera Pheri" , "C. Monty Python" , "D. SNL"],
        ["A. False","B. True" , "C. What's earth" , "D. Depends on climate"],
        ["A. Adani","B. Bill gates" , "C. Bhagwaan" , "D. Guido Van Rossum"]
]


new_game()

while play_again():
    new_game()

print("Bye!!! Have a great day....")

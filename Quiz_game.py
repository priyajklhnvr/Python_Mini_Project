print("Let's Start The Game")

game = input("Are You Ready To Take a Quiz?? (Yes/No) ")
if game == "Yes":
    print("Let's Start The Game\n")
  
    import random
    import time

    def quiz_game(Questions):
    
        random.shuffle(Questions)
        score = 0
        for question in Questions:
            print(question["Prompt"])
        
            for option in question["Options"]:
                print(option)   
        
            answer = input("Enter The Given option Which is correct = ").upper()
            while answer not in ['A', 'B', 'C', 'D']:
                answer = input("Invalid input. Please enter A, B, C, or D: ").upper()
    

            if answer == question["Answer"]:
               print("Correct!!")
               score += 1
            else:
                print("Incorrect! The Correct answer was = ", question["Answer"])
            time.sleep(1)     
        print(f"You got {score} out of {len(Questions)} questions correct.")
        print("Thanks for playing!")
        

    Questions = [
    {
        "Prompt" : "Which movie features the song 'Let It Go'?",
        "Options": ["A. Tangle","B. Frozen""C. Moana""D. Toy Story"],
        "Answer": "B"
    },
    {
        "Prompt" : "How many continents are there in the world?",
        "Options":  ["A. 5","B. 6","C. 7","D. 8"],
        "Answer" : "C"
                     
    },
    {
        "Prompt" : " What does 'HTTP' stand for in a website address?",
        "Options":  ["A. Hyper Text Protocol","B. Hyper Text Programming","C. Hyper Text Publishing","D. HyperText Transfer Protocol"],
        "Answer" : "D"
    },
    {
        "Prompt" : "Which JavaScript function is used to display a message box to the user?",
        "Options":   ["A. alert()","B. confirm()","C. prompt()","D. console"],
        "Answer" : "A"
    },
    {
        "Prompt" : "What is the minimum number of moves required to win a Tic-Tac-Toe game?",
        "Options":    ["A. 1","B. 2","C. 3","D.5"],
        "Answer" : "D"
    }
]

    quiz_game(Questions)
else:
    print("Cyaa...!!")
    



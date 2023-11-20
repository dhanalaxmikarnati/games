
def quiz_game():
    crct_ans = []
    score = 0
    question_num = 0

    questions = (
        "what does dog say?: ",
        "What does cat say?: ",
        "What does snake say?: ",
        "which animal is most beautiful?: ",
        "Which is tallest animal in the world?: "
    )

    options = (
        ("A. meow", "B. bow", "C. buuss", "D. owww"),
        ("A. meow", "B. bow", "C. buuss", "D. owww"),
        ("A. meow", "B. bow", "C. buuss", "D. owww"),
        ("A. tiger", "B. dog", "C. snake", "D. giraffe"),
        ("A. lion", "B. tiger", "C. giraffe", "D. elephant")
    )

    answers = ("B", "A", "C", "B", "C")

    for question in questions:
            print("----------------------")
            print(question)
            for option in options[question_num]:
                print(option)

            crct_as = input("Enter (A, B, C, D): ").upper()
            crct_ans.append(crct_as)
            if crct_as == answers[question_num]:
                score += 1
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"{answers[question_num]} is the correct answer")
            question_num += 1
    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in crct_ans:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print(f"Your score is: {score}%")

    
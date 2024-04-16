
questions = ("What is Rust?: ",
             "When did Rust first appear?: ",
             "Who sponsored Rust's development?: ",
             "Who created Rust?: ")

choices = (("A. Soda", "B. Corrosion", "C. Programming-language", "D. Animal"),
           ("A. May 15, 2015", "B. May 18, 2015", "C. October 3, 2015", "D. July 4, 1776"),
           ("A. Google", "B. Mozilla", "C. Amazon", "D. Wal-Mart"),
           ("A. Bill Gates", "B. Graydon Hoare", "C. Steve Jobs", "D. Elon Musk"))


guesses = []

answerKey = ("C", "A", "B", "B")

total = 0
choiceNum = 0

for question in questions:
    print("==========================")
    print(question)
    for choice in choices[choiceNum]:
        print(choice)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if answerKey[choiceNum] == guess:
        total += 1
        print("Right!")
    else:
        print("Wrong!")
        print(f"{answerKey[choiceNum]} is the correct answer")
    choiceNum += 1

print("============================\n       RESULTS        \n============================")

print("answers: ", end="")

for answer in answerKey:
    print(answer, end=" ")

print()
print("guesses: ", end="")

for guess in guesses:
    print(guess, end=" ")

result = int(total/len(questions) * 100)

print("\nYour score is:", result, "%")

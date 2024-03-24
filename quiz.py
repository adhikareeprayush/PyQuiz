print("Welcome to PyQuiz")
play = input("DO you want to Play the Quiz? (Y/N): ")
if play != "Y":
    quit()
points = 0
print("Lets Get Started")
print("Total Points :" + str(points))
questions = [
    {
        'question': 'What is the capital of France?',
        'answers': ['Paris', 'London', 'Berlin', 'Madrid'],
        'correct_answer': 'PARIS',
    },
    {
        'question': 'Who wrote the play "Romeo and Juliet"?',
        'answers': ['William Shakespeare', 'Charles Dickens', 'Jane Austen', 'F. Scott Fitzgerald'],
        'correct_answer': 'WILLIAM SHAKESPEARE',
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'answers': ['Jupiter', 'Saturn', 'Neptune', 'Earth'],
        'correct_answer': 'JUPITER',
    },
    {
        'question': 'Which famous scientist developed the theory of relativity?',
        'answers': ['Albert Einstein', 'Isaac Newton', 'Stephen Hawking', 'Galileo Galilei'],
        'correct_answer': 'ALBERT EINSTEIN',
    },
]

for question in questions:
    print(question['question'])
    print("Options are: " + str(question['answers']))
    answer = input("Please Enter Your Answer : ").upper()
    if(answer == question['correct_answer']):
        print("Correct")
        points +=1
    else:
        print("Incorrect")

print("Your final Score is : " + str(points) + ".")
print("Thanks for Playing")
quit()







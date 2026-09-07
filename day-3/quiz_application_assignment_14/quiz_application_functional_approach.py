'''
14. Quiz Application 
Represent questions: 
questions = [ 
{ 
"question": "What is Python?", 
"options": ["Language", "Database", "OS", "Browser"], 
"answer": 1 
} 
] 
Implement: 
display_question() 
get_answer() 
check_answer() 
calculate_score() 
At the end: 
Total Questions: 10 
Correct: 8 
Wrong: 2 
Score: 80% 
Handle invalid answers.
'''

'''
Functional Approach
'''

questions = [
    {
        "question": "What is Python?",
        "options": ["Language", "Database", "OS", "Browser"],
        "answer": 1
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["func", "def", "function", "define"],
        "answer": 2
    },
    {
        "question": "Which data type is used to store multiple values?",
        "options": ["List", "Integer", "Float", "Boolean"],
        "answer": 1
    }
]


def display_question(question):
    print("\n" + question["question"])
    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")


def get_answer():
    while True:
        try:
            answer = int(input("Enter your answer: "))
            if answer < 1 or answer > 4:
                raise ValueError("Answer must be between 1 and 4.")
            return answer
        except ValueError as error:
            print("Invalid answer:", error)


def check_answer(question, user_answer):
    return user_answer == question["answer"]


def calculate_score(correct, total_questions):
    return (correct / total_questions) * 100


correct = 0
wrong = 0
for question in questions:
    display_question(question)
    user_answer = get_answer()
    if check_answer(question, user_answer):
        print("Correct!")
        correct += 1
    else:
        print("Wrong!")
        wrong += 1


total_questions = len(questions)
score = calculate_score(correct, total_questions)
print("Result:")
print("Total Questions:", total_questions)
print("Correct:", correct)
print("Wrong:", wrong)
print("Score:", score, "%")


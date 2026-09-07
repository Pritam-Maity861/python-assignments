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
class based Approach
'''

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.correct = 0
        self.wrong = 0

    def display_question(self, question):
        print("\n" + question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

    def get_answer(self):
        while True:
            try:
                answer = int(input("Enter your answer: "))

                if answer < 1 or answer > 4:
                    raise ValueError("Answer must be between 1 and 4.")

                return answer
            except ValueError as error:
                print("Invalid answer:", error)

    def check_answer(self, question, user_answer):
        return user_answer == question["answer"]

    def calculate_score(self):
        total_questions = len(self.questions)
        return (self.correct / total_questions) * 100

    def start_quiz(self):
        for question in self.questions:
            self.display_question(question)
            user_answer = self.get_answer()
            if self.check_answer(question, user_answer):
                print("Correct!")
                self.correct += 1
            else:
                print("Wrong!")
                self.wrong += 1

        total_questions = len(self.questions)
        score = self.calculate_score()

        print("Result:")
        print("Total Questions:", total_questions)
        print("Correct:", self.correct)
        print("Wrong:", self.wrong)
        print("Score:", score, "%")


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


quiz = Quiz(questions)
quiz.start_quiz()

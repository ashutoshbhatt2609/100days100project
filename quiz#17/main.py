from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for i in range (len(question_data)):
    question=question_data[i]
    text=question["text"]
    ans=question["answer"]
    question_new=Question(text,ans)
    question_bank.append(question_new)

quiz=QuizBrain(question_bank)
while quiz.still_has_question()==True:
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was : {quiz.score}/{quiz.question_no}")
    

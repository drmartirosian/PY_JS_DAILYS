from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# print(question_data[1]['text'])

#1. Make data bank of questions/answers using Question class
question_bank = []

# for q in question_bank:
#     question_text = q['text']
#     question_answer = q['answer']
#     new_question = Question(question_text,question_answer)
#     question_bank.append(new_question)

#OR...

for q in question_data:
    question_bank.append(Question(q['text'],q['answer']))

# print(question_bank)

#2. Import question generator (QuizBrain class)

quiz = QuizBrain(question_bank)
quiz.next_question()
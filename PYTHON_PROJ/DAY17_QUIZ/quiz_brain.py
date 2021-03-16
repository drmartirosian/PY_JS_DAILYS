class QuizBrain:
    def __init__(self,q_list):
        self.q_num = 0
        self.q_list = q_list

    def next_question(self):
        #grab current q from q bank
        current_q = self.q_list[self.q_num]
        #increment q number
        self.q_num += 1
        #get user answr for q's
        user_response = input(f"Q.{self.q_num} => {current_q.text} (True/False)? ")
        if user_response == current_q.answer and self.q_num <= 12:
            print("CORRECT!")
            self.next_question()
        else:
            print("Wrong...")
            print(f"SCORE: {self.q_num}")
            return False
            


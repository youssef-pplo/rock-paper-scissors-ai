import random

class RockPaperScissorsAI:
    def __init__(self):
        self.history = []
        self.transitions = {
            "rock": {"rock": 0, "paper": 0, "scissors": 0},
            "paper": {"rock": 0, "paper": 0, "scissors": 0},
            "scissors": {"rock": 0, "paper": 0, "scissors": 0}
        }

    def update_history(self, user_choice):
        if len(self.history) > 0:
            last_choice = self.history[-1]
            self.transitions[last_choice][user_choice] += 1
        self.history.append(user_choice)

    def predict_next_move(self):
        if len(self.history) == 0:
            return random.choice(["rock", "paper", "scissors"])

        last_choice = self.history[-1]
        next_move_predictions = self.transitions[last_choice]
        predicted_move = max(next_move_predictions, key=next_move_predictions.get)

        return predicted_move

    def get_ai_choice(self):
        predicted_user_move = self.predict_next_move()
        counter_move = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }
        return counter_move[predicted_user_move]

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if choice == "1" :
        choice = "rock"
    elif choice == "2" :
        choice = "paper"
    elif choice == "3" :
        choice = "scissors"
        
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice

def determine_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and ai_choice == "scissors") or \
         (user_choice == "scissors" and ai_choice == "paper") or \
         (user_choice == "paper" and ai_choice == "rock"):
        return "You win!"
    else:
        return "AI wins!"

def play_game():
    ai = RockPaperScissorsAI()
    while True:
        user_choice = get_user_choice()
        ai_choice = ai.get_ai_choice()
        ai.update_history(user_choice)
        print(f"AI chose: {ai_choice}")
        result = determine_winner(user_choice, ai_choice)
        print(result)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_game()

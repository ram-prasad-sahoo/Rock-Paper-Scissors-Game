import random
import tkinter as tk
from tkinter import Toplevel

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    result_window = Toplevel()
    result_window.title("Result")
    result_window.config(bg="lightblue")

    result_message = f"User choice: {user_choice}\nComputer choice: {computer_choice}\n"
    if winner == 'tie':
        result_message += "It's a tie!"
        color = "gray"
    elif winner == 'user':
        result_message += "You win!"
        color = "green"
    else:
        result_message += "Computer wins!"
        color = "red"

    tk.Label(result_window, text=result_message, font=("Arial", 16, 'bold'), bg=color, fg="white", padx=20, pady=20).pack(pady=10)
    tk.Button(result_window, text="OK", command=result_window.destroy, font=("Arial", 15), bg="lightgray", fg="black").pack(pady=10)

def update_score(winner):
    global user_score, computer_score
    if winner == 'user':
        user_score += 1
    elif winner == 'computer':
        computer_score += 1
    score_label.config(text=f"Scores - You: {user_score}, Computer: {computer_score}")

def on_choice(user_choice):
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, winner)
    update_score(winner)

def create_main_window():
    global score_label

    window = tk.Tk()
    window.title("Rock-Paper-Scissors Game")
    window.config(bg="lightblue")

    tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Arial", 16, 'bold'), bg="lightblue").pack(pady=10)

    button_frame = tk.Frame(window, bg="lightblue")
    button_frame.pack(pady=10)

    rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 15, 'bold'), command=lambda: on_choice('rock'), bg="lightgray", fg="black")
    paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 15, 'bold'), command=lambda: on_choice('paper'), bg="lightgray", fg="black")
    scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 15, 'bold'), command=lambda: on_choice('scissors'), bg="lightgray", fg="black")

    rock_button.grid(row=0, column=0, padx=10, pady=10)
    paper_button.grid(row=0, column=1, padx=10, pady=10)
    scissors_button.grid(row=0, column=2, padx=10, pady=10)

    score_label = tk.Label(window, text="Scores - You: 0, Computer: 0", font=("Arial", 14), bg="lightblue")
    score_label.pack(pady=10)

    window.mainloop()

user_score = 0
computer_score = 0

create_main_window()

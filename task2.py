import tkinter as tk
from tkinter import messagebox
import random

# Function to determine winner
def determine_winner(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win! Computer chose " + computer_choice
    else:
        result = "You lose! Computer chose " + computer_choice
    
    messagebox.showinfo("Result", result)

# Function to handle button clicks
def rock_clicked():
    determine_winner('rock')

def paper_clicked():
    determine_winner('paper')

def scissors_clicked():
    determine_winner('scissors')

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create buttons
rock_button = tk.Button(root, text="Rock", width=10, command=rock_clicked)
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", width=10, command=paper_clicked)
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", width=10, command=scissors_clicked)
scissors_button.pack(pady=10)

# Run the main event loop
root.mainloop()
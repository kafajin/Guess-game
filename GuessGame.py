import tkinter as tk
from tkinter import messagebox
import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Function to handle the guess
def check_guess():
    try:
        user_guess = int(entry.get())  # Get the user's input
        if user_guess == random_number:
            messagebox.showinfo("Result", "🎉 Correct! You guessed the random number!")
            root.destroy()  # Close the application
        elif user_guess < random_number:
            feedback_label.config(text="📉 Too low, try again!", fg="#ff5733")
        else:
            feedback_label.config(text="📈 Too high, try again!", fg="#ff5733")
    except ValueError:
        feedback_label.config(text="❌ Invalid input. Please enter a valid number.", fg="#ff0000")

# Function to handle quitting
def quit_game():
    result = messagebox.askyesno("Quit", "Are you sure you want to quit?")
    if result:
        root.destroy()

# Initialize Tkinter window
root = tk.Tk()
root.title("🎯 Guess the Number Game")

# Set the size and center the window
window_width, window_height = 400, 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = (screen_height // 2) - (window_height // 2)
position_right = (screen_width // 2) - (window_width // 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
root.configure(bg="#f7f7f7")  # Light background

# Set up the GUI layout
instructions_label = tk.Label(
    root,
    text="🎲 Guess the random number (1-100):",
    font=("Arial", 14),
    bg="#f7f7f7",
    fg="#333333"
)
instructions_label.pack(pady=15)

entry = tk.Entry(root, width=10, font=("Arial", 14), justify="center", bd=2, relief="ridge")
entry.pack(pady=5)

guess_button = tk.Button(
    root,
    text="Guess",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=check_guess,
    width=12,
    relief="raised",
    bd=2
)
guess_button.pack(pady=10)

feedback_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "italic"),
    bg="#f7f7f7",
    fg="#333333"
)
feedback_label.pack(pady=10)

quit_button = tk.Button(
    root,
    text="Quit",
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    command=quit_game,
    width=12,
    relief="raised",
    bd=2
)
quit_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

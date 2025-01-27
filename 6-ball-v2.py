import random
import tkinter as tk
from tkinter import simpledialog, messagebox
from time import sleep

# Create the main application window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Generate a random number
chanse = random.randint(1, 6)

# Get the user's name
name = simpledialog.askstring("Input", "What is your name?")
if not name:  # If the user cancels or provides no input
    messagebox.showinfo("Goodbye", "No name entered. Exiting...")
    exit()

# Get the user's question
question = simpledialog.askstring("Input", "What is your question about your future? (Write in full sentence form)")
if not question:  # If the user cancels or provides no input
    messagebox.showinfo("Goodbye", "No question entered. Exiting...")
    exit()

# Create a "thinking" delay
messagebox.showinfo("Processing", "Thinking about your question...")
sleep(3)

# Generate the answer
answer = ""
if chanse == 1:
    answer = "100%"
elif chanse == 2:
    answer = "Very likely"
elif chanse == 3:
    answer = "Likely"
elif chanse == 4:
    answer = "Unlikely"
elif chanse == 5:
    answer = "Very unlikely"
elif chanse == 6:
    answer = "0%"

# Display the answer
messagebox.showinfo("Answer", f"Hello {name}, the answer to your question '{question}' is: {answer}")

# Say goodbye
messagebox.showinfo("Goodbye", "Cya Later!")
import tkinter as tk
from random import randint

def roll_dice():
    rolls = int(entry.get())
    results.delete(1.0, tk.END)
    for _ in range(rolls):
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        results.insert(tk.END, f'Dice 1: {dice1}, Dice 2: {dice2}\n')

root = tk.Tk()
root.geometry('300x400')
root.title('Dice Roller')

frame = tk.Frame(root)
frame.pack(pady=20)

entry = tk.Entry(frame, width=10)
entry.pack(pady=20)

roll_button = tk.Button(frame, text='Roll Dice', command=roll_dice)
roll_button.pack(pady=10)

results = tk.Text(root, width=30, height=10)
results.pack(pady=10)

root.mainloop()

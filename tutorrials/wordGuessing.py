import tkinter as tk
from random import shuffle, choice

# list of words
words = ['apple', 'banana', 'grape', 'strawberry', 'orange', 'pineapple', 'blueberry', 'raspberry', 'mango', 'papaya'] * 10
shuffle(words)

def scramble(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

def start_game():
    global words_to_guess
    words_to_guess = int(word_count.get())
    next_word()

def next_word():
    global words_to_guess
    if words_to_guess > 0:
        word = choice(words)
        words.remove(word)
        scrambled_word.set(scramble(word))
        correct_word.set(word)
        words_to_guess -= 1
    else:
        scrambled_word.set('')
        correct_word.set('')
        message.set('Game Over!')

def check_guess():
    if guess.get().lower() == correct_word.get().lower():
        message.set('Correct!')
        guess.set('')
        next_word()
    else:
        message.set('Try again!')

def skip():
    guess.set('')
    next_word()

root = tk.Tk()
root.title('Word Scramble Game')

scrambled_word = tk.StringVar()
correct_word = tk.StringVar()
guess = tk.StringVar()
message = tk.StringVar()

word_count = tk.Entry(root)
word_count.pack()
tk.Button(root, text='Start Game', command=start_game).pack()

tk.Label(root, text='Guess the word:').pack()
tk.Label(root, textvariable=scrambled_word, font=('Helvetica', 20)).pack()
tk.Entry(root, textvariable=guess).pack()
tk.Button(root, text='Guess', command=check_guess).pack()
tk.Button(root, text='Skip', command=skip).pack()
tk.Label(root, textvariable=message).pack()

root.mainloop()

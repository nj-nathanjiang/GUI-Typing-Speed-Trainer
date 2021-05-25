import tkinter as tk
import random


list_of_texts = ['Once upon a time']


def get_highscore():
    global highscore_label_text, highscore
    with open("highscore.txt", "r") as file:
        score = file.readline()
        highscore = int(score)
        highscore_label_text.set(f"Highscore: {highscore}")


def start_test():
    global test_on, welcome_label_text, text_label_text, analyze_text_task
    test_on = True

    text_label_text.set(random.choice(list_of_texts))

    analyze_text_task = window.after(1000, analyze_text)
    welcome_label_text.set("Test Incomplete")


def end_test():
    global test_on, welcome_label_text, highscore, wpm
    test_on = False

    if highscore < wpm:
        with open("highscore.txt", "w") as file:
            file.write(str(round(wpm)))
    set_welcome_label_original()


def set_welcome_label_original():
    welcome_label_text.set("Welcome to the Typing Speed Trainer")


def exit_app():
    window.quit()


def analyze_text():
    global text, wpm, instructions_label_text, stopwatch, stopwatch_label_text, typing_speed_label_text, analyze_text_task
    window.after_cancel(analyze_text_task)
    text = textbox.get(1.0, tk.END)
    analyze_text_task = window.after(1000, analyze_text)
    if text[:-1] in text_label.cget("text"):
        instructions_label_text.set("Everything is correct so far.")
    else:
        instructions_label_text.set("Something is spelled incorrectly.")

    stopwatch += 1
    stopwatch_label_text.set(f"{stopwatch} seconds")

    num_words = text.split(" ")
    wpm = len(num_words) / (stopwatch / 60)
    typing_speed_label_text.set(f"Typing WPM: {round(wpm)}")
    if text[:-1] == text_label.cget("text"):
        welcome_label_text.set("Test Completed")
        window.after_cancel(analyze_text_task)
        window.after(1000, end_test)
        window.after(6000, set_welcome_label_original)


# Window
window = tk.Tk()
window.title("Typing Speed Trainer")
window.minsize(500, 500)


# Welcome Label
welcome_label_text = tk.StringVar()
set_welcome_label_original()
welcome_label = tk.Label(window, textvariable=welcome_label_text)
welcome_label.grid(row=0, column=1, padx=10, pady=10)


# Highscore Label
highscore = 0
highscore_label_text = tk.StringVar()
get_highscore()
highscore_label = tk.Label(window, textvariable=highscore_label_text)
highscore_label.grid(row=0, column=2, padx=10, pady=10)


# Given Text Label
text_label_text = tk.StringVar()
text_label_text.set("Text Sample")
text_label = tk.Label(window, textvariable=text_label_text, wraplength=750)
text_label.grid(row=1, column=1, padx=10, pady=10)


# Stopwatch Label
stopwatch = 0
stopwatch_label_text = tk.StringVar()
stopwatch_label_text.set(f"{stopwatch} seconds")
stopwatch_label = tk.Label(window, textvariable=stopwatch_label_text)
stopwatch_label.grid(row=1, column=0, padx=10, pady=10)


# Typing Speed Label
wpm = 0
typing_speed_label_text = tk.StringVar()
typing_speed_label_text.set(f"Typing WPM: {wpm}")
typing_speed_label = tk.Label(window, textvariable=typing_speed_label_text)
typing_speed_label.grid(row=1, column=2, padx=10, pady=10)


# Instructions Label
instructions_label_text = tk.StringVar()
instructions_label_text.set("Enter your text below:")
instructions_label = tk.Label(window, textvariable=instructions_label_text)
instructions_label.grid(row=2, column=1, padx=10, pady=10)


# Textbox
text = ""
textbox = tk.Text(height=5, width=30, yscrollcommand=True)
textbox.focus()
textbox.grid(row=3, column=1, padx=10, pady=10)


# Start Button
test_on = False
start_button = tk.Button(window, command=start_test, text="Start Test", height=2, width=15, bg="black")
start_button.grid(row=3, column=0, padx=10, pady=10)


# Exit Button
exit_button = tk.Button(window, command=exit_app, text="Exit App", height=2, width=15, bg="black")
exit_button.grid(row=3, column=2, padx=10, pady=10)

analyze_text_task = None
window.mainloop()

import tkinter as tk
from tkinter import messagebox


current_turn = "x"
game_is_finished = False

board_array = [
    "0", "1", "2",
    "3", "4", "5",
    "6", "7", "8"
]
buttons = []

def evaluate_board():
    global game_is_finished

    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for a, b, c in wins:
        if board_array[a] == board_array[b] == board_array[c]:
            game_is_finished = True
            messagebox.showinfo("Game Over", f"{board_array[a].upper()} won!")
            return

    if all(cell in ["x", "o"] for cell in board_array):
        game_is_finished = True
        messagebox.showinfo("Game Over", "It's a draw!")

def on_button_click(index):
    global current_turn, game_is_finished

    if game_is_finished:
        return 

    if board_array[index] in ["x", "o"]:
        return

    board_array[index] = current_turn

    buttons[index].config(text=current_turn.upper())

    evaluate_board()

    if not game_is_finished:
        if current_turn == "x":
            current_turn = "o"
        else:
            current_turn = "x"

    label_turn.config(text=f"{current_turn.upper()}'s turn")

def reset_game():
    global current_turn, game_is_finished, board_array
    current_turn = "x"
    game_is_finished = False

    board_array = [
        "0", "1", "2",
        "3", "4", "5",
        "6", "7", "8"
    ]

    for btn in buttons:
        btn.config(text="")
        label_turn.config(text="X's turn")


root = tk.Tk()
root.title("X-O")

label_turn = tk.Label(root, text="X's turn", font=("Poppins", 16))
label_turn.grid(row=0, column=0, columnspan=3)

for i in range(9):
    btn = tk.Button(root, text="", font=("Poppins", 20), width=5, height=2, command=lambda i=i: on_button_click(i))
    btn.grid(row=1 + i // 3, column=i % 3)
    buttons.append(btn)

reset_btn = tk.Button(root, text="Reset", font=("Poppins", 14), command=reset_game)
reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()





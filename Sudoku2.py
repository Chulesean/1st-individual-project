<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox
import random
import time

def generate_puzzle():
    board = [[0] * 9 for _ in range(9)]
    
    for _ in range(20): 
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if board[row][col] == 0 and is_valid(board, row, col, num):
            board[row][col] = num
    return board

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def validate_board():
    for row in range(9):
        for col in range(9):
            num = entries[row][col].get()
            if num == "":
                messagebox.showinfo("Incomplete", "Please fill all cells!")
                return
            num = int(num)
            if not is_valid(grid, row, col, num):
                highlight_invalid_cells()
                return
    messagebox.showinfo("Congratulations", "Congratulations! You solved it correctly.")

def highlight_invalid_cells():
    invalid_cells = []
    for row in range(9):
        for col in range(9):
            num = entries[row][col].get()
            if num != "" and int(num) != grid[row][col] and not is_valid(grid, row, col, int(num)):
                invalid_cells.append(entries[row][col])
    for _ in range(3):
        for cell in invalid_cells:
            cell.config(bg="red")
        root.update()
        time.sleep(0.3)
        for cell in invalid_cells:
            cell.config(bg="white")
        root.update()
        time.sleep(0.3)

def load_puzzle():
    for row in range(9):
        for col in range(9):
            entry = entries[row][col]
            entry.config(state="normal") 
            entry.delete(0, tk.END)  
            entry.config(bg="white") 
            
            num = grid[row][col]
            if num != 0:  
                entry.insert(0, str(num))  
                entry.config(state="disabled", bg="#E0E0E0") 
            else:
                entry.config(state="normal", bg="white")


def new_game():
    global grid
    grid = generate_puzzle()
    load_puzzle()

root = tk.Tk()
root.title("Sudoku Game")

entries = [[None for _ in range(9)] for _ in range(9)]
for row in range(9):
    for col in range(9):
        e = tk.Entry(root, width=2, font=('Arial', 18), justify='center')
        e.grid(row=row, column=col, padx=2, pady=2)
        entries[row][col] = e

grid = generate_puzzle()
load_puzzle()

validate_button = tk.Button(root, text="Check Solution", command=validate_board)
validate_button.grid(row=9, column=0, columnspan=4, sticky="we")

new_game_button = tk.Button(root, text="New Game", command=new_game)
new_game_button.grid(row=9, column=5, columnspan=4, sticky="we")

root.mainloop()
=======
import tkinter as tk
from tkinter import messagebox
import random
import time

def generate_puzzle():
    board = [[0] * 9 for _ in range(9)]
    
    for _ in range(20): 
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if board[row][col] == 0 and is_valid(board, row, col, num):
            board[row][col] = num
    return board

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def validate_board():
    for row in range(9):
        for col in range(9):
            num = entries[row][col].get()
            if num == "":
                messagebox.showinfo("Incomplete", "Please fill all cells!")
                return
            num = int(num)
            if not is_valid(grid, row, col, num):
                highlight_invalid_cells()
                return
    messagebox.showinfo("Congratulations", "Congratulations! You solved it correctly.")

def highlight_invalid_cells():
    invalid_cells = []
    for row in range(9):
        for col in range(9):
            num = entries[row][col].get()
            if num != "" and int(num) != grid[row][col] and not is_valid(grid, row, col, int(num)):
                invalid_cells.append(entries[row][col])
    for _ in range(3):
        for cell in invalid_cells:
            cell.config(bg="red")
        root.update()
        time.sleep(0.3)
        for cell in invalid_cells:
            cell.config(bg="white")
        root.update()
        time.sleep(0.3)

def load_puzzle():
    for row in range(9):
        for col in range(9):
            entry = entries[row][col]
            entry.config(state="normal") 
            entry.delete(0, tk.END)  
            entry.config(bg="white") 
            
            num = grid[row][col]
            if num != 0:  
                entry.insert(0, str(num))  
                entry.config(state="disabled", bg="#E0E0E0") 
            else:
                entry.config(state="normal", bg="white")


def new_game():
    global grid
    grid = generate_puzzle()
    load_puzzle()

root = tk.Tk()
root.title("Sudoku Game")

entries = [[None for _ in range(9)] for _ in range(9)]
for row in range(9):
    for col in range(9):
        e = tk.Entry(root, width=2, font=('Arial', 18), justify='center')
        e.grid(row=row, column=col, padx=2, pady=2)
        entries[row][col] = e

grid = generate_puzzle()
load_puzzle()

validate_button = tk.Button(root, text="Check Solution", command=validate_board)
validate_button.grid(row=9, column=0, columnspan=4, sticky="we")

new_game_button = tk.Button(root, text="New Game", command=new_game)
new_game_button.grid(row=9, column=5, columnspan=4, sticky="we")

root.mainloop()
>>>>>>> 4a25440654ad022d00888688255665fa0fa5a0e9

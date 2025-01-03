import tkinter as tk
import random
from controllers.Match import Match
from controllers.Board import OutOfBoundsError, CellOccupiedError

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Matrix Tic-Tac-Toe")
        master.configure(bg="black")

        self.match = Match()
        self.cell_size = 150
        self.matrix_green = "#117412"  # Verde mais claro
        self.board_size = 3
        self.canvas_width = self.cell_size * self.board_size
        self.canvas_height = self.cell_size * self.board_size
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="black", highlightthickness=0)
        self.canvas.pack()

        self.animate_background()
        self.draw_grid()
        self.text_ids = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.canvas.bind("<Button-1>", self.handle_click)

    def animate_background(self):
        self.background_lines = []
        num_lines = 100
        for _ in range(num_lines):
            x = random.randint(0, self.canvas_width)
            y = random.randint(-200, 0)
            length = random.randint(5, 15)
            binary_string = "".join(random.choice(["0", "1", "@", "#", "$", "%", "A", "*","B"]) for _ in range(length))
            text = self.canvas.create_text(x, y, text=binary_string, fill=self.matrix_green, font=("Courier", 12), anchor=tk.NW, tags="background")
            self.background_lines.append({
                "id": text,
                "x": x,
                "speed": random.randint(2, 6),
                "update_frequency": 2,
            })
        self.move_lines()

    def move_lines(self):
        for line_data in self.background_lines:
            line_id = line_data["id"]
            speed = line_data["speed"]
            x = line_data["x"]
            y = self.canvas.coords(line_id)[1]
            self.canvas.move(line_id, 0, speed)
            if y > self.canvas_height:
                length = random.randint(1, 5)
                binary_string = "".join(random.choice(["0", "1", "@", "#", "$", "%", "&", "*"]) for _ in range(length))
                self.canvas.itemconfig(line_id, text=binary_string)
                self.canvas.coords(line_id, x, -random.randint(50, 200))
        self.canvas.after(20, self.move_lines)

    def draw_grid(self):
        for i in range(1, self.board_size):
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.canvas_height, width=2, fill=self.matrix_green)
            self.canvas.create_line(0, i * self.cell_size, self.canvas_width, i * self.cell_size, width=2, fill=self.matrix_green)

    def animate_text(self, i, j, final_text):
        symbols = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "+", "=", "[", "]", "{", "}", ";", ":", ",", ".", "/", "<", ">", "?", "|", "0","1"]
        text_id = self.text_ids[i][j]

        def change_text(count):
            if count < 5:
                random_text = "".join(random.choice(symbols) for _ in range(1))
                self.canvas.itemconfig(text_id, text=random_text)
                self.canvas.after(30, change_text, count + 1)
            else:
                self.canvas.itemconfig(text_id, text=final_text)
        change_text(0)

    def handle_click(self, event):
        if self.match.winner is not None:  # Verifica se o jogo já terminou
            return

        x = event.x // self.cell_size
        y = event.y // self.cell_size

        try:
            self.match.board.make_move(y, x)
            if self.text_ids[y][x] is None:
                text_id = self.canvas.create_text(x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2, text="", fill=self.matrix_green, font=("Courier", 40), tags="text")
                self.text_ids[y][x] = text_id
            self.animate_text(y, x, self.match.board.mat[y][x])
            self.match.winner = self.match.board.check_victory()

            if self.match.winner:
                self.end_game(self.match.winner)

            self.canvas.update()

        except OutOfBoundsError as e:
            print(e)
        except CellOccupiedError as e:
            print(e)

    def end_game(self, winner):
        self.canvas.unbind("<Button-1>")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if winner == "Empate":
            self.canvas.create_text(width / 2, height * 3/4, text="Empate!", fill="white", font=("Courier", 20), anchor=tk.CENTER)
        else:
            self.canvas.create_text(width / 2, height * 3/4, text=f"Jogador {winner} Venceu!", fill="white", font=("Courier", 20), anchor=tk.CENTER)

def main():
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox
import os
import traceback  # Importe traceback para rastreamento de pilha
from controllers.Match import Match
from controllers.Board import OutOfBoundsError, CellOccupiedError

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Jogo da Velha")

        self.match = Match()

        self.cell_size = 100
        self.line_width = 5
        self.grid_color = "black"

        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            x_path = os.path.join(current_dir, "images", "X.png")
            o_path = os.path.join(current_dir, "images", "O.png")
            self.x_image = tk.PhotoImage(file=x_path).subsample(2,2)
            self.o_image = tk.PhotoImage(file=o_path).subsample(2,2)
        except tk.TclError as e:
            messagebox.showerror("Erro", f"Não foi possível carregar as imagens: {e}")
            exit()
        except FileNotFoundError:
            messagebox.showerror("Erro", "Pasta 'images' não encontrada")
            exit()

        canvas_width = self.cell_size * 3
        canvas_height = self.cell_size * 3
        self.canvas = tk.Canvas(master, width=canvas_width, height=canvas_height, bg="white", highlightthickness=0)
        self.canvas.pack()

        self.draw_grid()
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_grid(self):
        for i in range(1, 3):
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.cell_size * 3, width=self.line_width, fill=self.grid_color)
            self.canvas.create_line(0, i * self.cell_size, self.cell_size * 3, i * self.cell_size, width=self.line_width, fill=self.grid_color)

    def handle_click(self, event):
        x = event.x // self.cell_size
        y = event.y // self.cell_size

        try:
            self.match.board.make_move(y, x)
            self.update_board()
            self.match.winner = self.match.board.check_victory()
            if self.match.winner:
                self.end_game(self.match.winner)
        except OutOfBoundsError as e:
            messagebox.showerror("Erro", str(e))
        except CellOccupiedError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro Inesperado", f"Ocorreu um erro inesperado: {e}")
            traceback.print_exc() # Imprime o traceback completo no console

    def update_board(self):
        self.canvas.delete("X", "O")
        for i in range(3):
            for j in range(3):
                if self.match.board.mat[i][j] == 'X':
                    x0 = j * self.cell_size + self.cell_size // 2
                    y0 = i * self.cell_size + self.cell_size // 2
                    self.canvas.create_image(x0, y0, image=self.x_image, tags="X")
                elif self.match.board.mat[i][j] == 'O':
                    x0 = j * self.cell_size + self.cell_size // 2
                    y0 = i * self.cell_size + self.cell_size // 2
                    self.canvas.create_image(x0, y0, image=self.o_image, tags="O")

    def end_game(self, winner):
        if winner == "Empate":
            messagebox.showinfo("Fim de Jogo", "Empate!")
        else:
            messagebox.showinfo("Fim de Jogo", f"Jogador {winner} venceu!")
        self.canvas.unbind("<Button-1>")

def main():
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
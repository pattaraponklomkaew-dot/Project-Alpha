import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.width = 400
        self.height = 400
        self.cell_size = 20
        self.direction = 'Right'
        self.running = True
        self.score = 0
        self.snake = [(5, 5), (4, 5), (3, 5)]  # initial snake
        self.food = None
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg='black')
        self.canvas.pack()
        # Button frame
        self.button_frame = tk.Frame(self.root)
        self.start_btn = tk.Button(self.button_frame, text="Start", font=("Arial", 12), command=self.start_game, state='disabled')
        self.reset_btn = tk.Button(self.button_frame, text="Reset", font=("Arial", 12), command=self.reset_game, state='disabled')
        self.start_btn.pack(side='left', padx=10)
        self.reset_btn.pack(side='left', padx=10)
        self.button_frame.pack(pady=5)
        self.root.bind('<Up>', lambda e: self.change_direction('Up'))
        self.root.bind('<Down>', lambda e: self.change_direction('Down'))
        self.root.bind('<Left>', lambda e: self.change_direction('Left'))
        self.root.bind('<Right>', lambda e: self.change_direction('Right'))
        self.spawn_food()
        self.update()

    def change_direction(self, new_dir):
        opposites = {'Up':'Down', 'Down':'Up', 'Left':'Right', 'Right':'Left'}
        if new_dir != opposites.get(self.direction):
            self.direction = new_dir

    def spawn_food(self):
        while True:
            x = random.randint(0, (self.width // self.cell_size) - 1)
            y = random.randint(0, (self.height // self.cell_size) - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'Up':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'Down':
            new_head = (head_x, head_y + 1)
        elif self.direction == 'Left':
            new_head = (head_x - 1, head_y)
        else:
            new_head = (head_x + 1, head_y)
        self.snake = [new_head] + self.snake[:-1]

    def grow_snake(self):
        self.snake.append(self.snake[-1])

    def check_collisions(self):
        head = self.snake[0]
        # Wall collision
        if not (0 <= head[0] < self.width // self.cell_size and 0 <= head[1] < self.height // self.cell_size):
            return True
        # Self collision
        if head in self.snake[1:]:
            return True
        return False

    def update(self):
        if not self.running:
            return
        self.move_snake()
        if self.snake[0] == self.food:
            self.grow_snake()
            self.spawn_food()
            self.score += 1
        if self.check_collisions():
            self.running = False
            self.canvas.create_text(self.width//2, self.height//2, fill='red', font=('Arial', 24), text='Game Over')
            self.start_btn.config(state='normal')
            self.reset_btn.config(state='normal')
            return
        self.draw()
        self.root.after(100, self.update)
    def start_game(self):
        self.direction = 'Right'
        self.running = True
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.spawn_food()
        self.start_btn.config(state='disabled')
        self.reset_btn.config(state='disabled')
        self.update()

    def reset_game(self):
        self.score = 0
        self.start_game()

    def draw(self):
        self.canvas.delete('all')
        # Draw food
        x, y = self.food
        self.canvas.create_rectangle(x*self.cell_size, y*self.cell_size,
                                     (x+1)*self.cell_size, (y+1)*self.cell_size,
                                     fill='red', outline='')
        # Draw snake
        for i, (sx, sy) in enumerate(self.snake):
            color = 'green' if i == 0 else '#00cc00'
            self.canvas.create_rectangle(sx*self.cell_size, sy*self.cell_size,
                                         (sx+1)*self.cell_size, (sy+1)*self.cell_size,
                                         fill=color, outline='')
        # Draw score
        self.canvas.create_text(40, 10, fill='white', font=('Arial', 12), text=f'Score: {self.score}')

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

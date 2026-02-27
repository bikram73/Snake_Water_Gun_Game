import tkinter as tk
from tkinter import messagebox
import random

class SnakeWaterGunGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Water Gun Game")
        self.root.geometry("500x550")
        self.root.configure(bg="#2C3E50")

        # Game State
        self.user_score = 0
        self.computer_score = 0
        self.draw_score = 0
        self.choices = {"Snake": "🐍", "Water": "💧", "Gun": "🔫"}
        
        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="🐍 Snake Water Gun 🔫", 
            font=("Helvetica", 24, "bold"),
            bg="#2C3E50", 
            fg="#ECF0F1"
        )
        title_label.pack(pady=20)

        # Score Board
        self.score_label = tk.Label(
            self.root,
            text=f"You: {self.user_score}  |  Draw: {self.draw_score}  |  Computer: {self.computer_score}",
            font=("Helvetica", 16),
            bg="#2C3E50",
            fg="#F1C40F"
        )
        self.score_label.pack(pady=10)

        # Display Area (Choices)
        self.result_frame = tk.Frame(self.root, bg="#2C3E50")
        self.result_frame.pack(pady=20)

        self.user_choice_label = tk.Label(self.result_frame, text="You: ❓", font=("Helvetica", 14), bg="#2C3E50", fg="white")
        self.user_choice_label.grid(row=0, column=0, padx=20)
        
        self.comp_choice_label = tk.Label(self.result_frame, text="Comp: ❓", font=("Helvetica", 14), bg="#2C3E50", fg="white")
        self.comp_choice_label.grid(row=0, column=1, padx=20)

        # Result Message
        self.message_label = tk.Label(
            self.root,
            text="Choose your weapon!",
            font=("Helvetica", 18, "bold"),
            bg="#2C3E50",
            fg="#2ECC71"
        )
        self.message_label.pack(pady=20)

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#2C3E50")
        btn_frame.pack(pady=20)

        # Buttons
        # Note: To use images, replace text=... with image=self.snake_img (after loading PhotoImage)
        self.btn_snake = tk.Button(btn_frame, text="🐍 Snake", font=("Arial", 12), width=10, command=lambda: self.play("Snake"))
        self.btn_snake.grid(row=0, column=0, padx=10)

        self.btn_water = tk.Button(btn_frame, text="💧 Water", font=("Arial", 12), width=10, command=lambda: self.play("Water"))
        self.btn_water.grid(row=0, column=1, padx=10)

        self.btn_gun = tk.Button(btn_frame, text="🔫 Gun", font=("Arial", 12), width=10, command=lambda: self.play("Gun"))
        self.btn_gun.grid(row=0, column=2, padx=10)

        # Restart Button
        restart_btn = tk.Button(
            self.root, 
            text="Restart Game", 
            font=("Arial", 12, "bold"), 
            bg="#E74C3C", 
            fg="white",
            command=self.reset_game
        )
        restart_btn.pack(pady=20)

    def play(self, user_choice):
        options = ["Snake", "Water", "Gun"]
        comp_choice = random.choice(options)

        # Update UI with choices
        self.user_choice_label.config(text=f"You: {self.choices[user_choice]}")
        self.comp_choice_label.config(text=f"Comp: {self.choices[comp_choice]}")

        # Determine Winner
        result = ""
        if user_choice == comp_choice:
            result = "It's a Tie! 😐"
            self.draw_score += 1
            color = "#95A5A6" # Grey
        elif (user_choice == "Snake" and comp_choice == "Water") or \
             (user_choice == "Water" and comp_choice == "Gun") or \
             (user_choice == "Gun" and comp_choice == "Snake"):
            result = "You Win! 🎉"
            self.user_score += 1
            color = "#2ECC71" # Green
        else:
            result = "Computer Wins! 🤖"
            self.computer_score += 1
            color = "#E74C3C" # Red

        # Update Result and Score
        self.message_label.config(text=result, fg=color)
        self.score_label.config(text=f"You: {self.user_score}  |  Draw: {self.draw_score}  |  Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.draw_score = 0
        self.score_label.config(text=f"You: {self.user_score}  |  Draw: {self.draw_score}  |  Computer: {self.computer_score}")
        self.message_label.config(text="Choose your weapon!", fg="#2ECC71")
        self.user_choice_label.config(text="You: ❓")
        self.comp_choice_label.config(text="Comp: ❓")

if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeWaterGunGame(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        
        self.questions = [
            {
                "question": "What is the maximum length of a Python identifier ?",
                "options": ["32", "16", "128", "No Fixed length"],
                "correct_option": 3,
            },
            {
                "question": "How is a code block indicated in Python??",
                "options": ["Brackets", "Identation", "Key", "None of the Above"],
                "correct_option": 1,
            },
            {
                "question": "Which of the following is the proper syntax to check if a particular element is present in a list?",
                "options": ["If else in List", "if not else not in list", "Both A and B", "None of the above"],
                "correct_option": 2,
            },
            
            
            
            
            
            
            
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)
        
        self.radio_var = tk.IntVar()
        self.radio_var.set(-1)
        
        self.option_labels = []
        for i in range(4):
            option_label = tk.Radiobutton(root, text="", font=("Arial", 12), variable=self.radio_var, value=i)
            option_label.pack()
            self.option_labels.append(option_label)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
        
        self.load_question()
    
    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_labels[i].config(text=question_data["options"][i])
        else:
            messagebox.showinfo("Quiz Complete", f"You scored {self.score} out of {len(self.questions)}")
            self.root.quit()
    
    def check_answer(self):
        selected_option = self.radio_var.get()
        if selected_option == self.questions[self.current_question]["correct_option"]:
            self.score += 1
        self.current_question += 1
        self.radio_var.set(-1)
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

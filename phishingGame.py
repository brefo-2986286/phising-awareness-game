import tkinter as tk
import random

# Define the scenarios and whether they are phishing attempts
scenarios = [
   {"content": "An email from your bank asking for your password.", "is_phishing": True},
    {"content": "You receive an email from 'support@app1e.com' asking to verify your account details urgently.", "is_phishing": True},
    {"content": "An SMS message claims you need to update your payment information for a service you don't remember subscribing to.", "is_phishing": True},
    {"content": "A popup on a website says you have a virus and must download their antivirus immediately.", "is_phishing": True},
    {"content": "An email from a stranger includes an attachment claiming to be an unpaid invoice.", "is_phishing": True},
    {"content": "A message on social media from a friend's account urgently asking for money, claiming they're stranded abroad.", "is_phishing": True},
    {"content": "An email from 'yourbankname-secure.com' asking you to reset your password.", "is_phishing": True},
    {"content": "A job offer email from a company you didn't apply to, asking for personal information.", "is_phishing": True},
    {"content": "An urgent message claiming your computer is compromised and to call a tech support number.", "is_phishing": True},
    {"content": "An email claiming you've won a contest you don't remember entering, asking for a processing fee.", "is_phishing": True},
    {"content": "An email from your workplace's HR department with a reminder about an upcoming scheduled meeting.", "is_phishing": False},
    {"content": "A newsletter from a website where you recently subscribed, containing articles and no requests for personal info.", "is_phishing": False},
    {"content": "A notification from your bank (with correct URL) about a new branch opening in your area.", "is_phishing": False},
    {"content": "An SMS from a courier service with a tracking link for a package you recently ordered.", "is_phishing": False},
    {"content": "An email from a well-known charity you support, thanking you for your previous donations.", "is_phishing": False},
    {"content": "A regular monthly invoice from a utility provider you use, with the usual account details.", "is_phishing": False},
    {"content": "A notification email from a social media platform about new login activity, including your device and location.", "is_phishing": False},
    {"content": "A reminder from a service you use about your subscription renewal, with a link to the official website.", "is_phishing": False},
    {"content": "An email from a family member that matches their usual writing style and content.", "is_phishing": False},
    {"content": "A notification from an online retailer about a product you wishlisted now being on sale.", "is_phishing": False},
]

# Shuffle the scenarios to randomize the order each time
random.shuffle(scenarios)

class PhishingGameApp:
    def __init__(self, root):
        self.root = root
        root.title("Phishing Awareness Game")
        root.geometry("500x300")  # Set the window size to 400x300 pixels
        root.resizable(False, False)  # Disable resizing the window

        self.score = 0
        self.incorrect = 0
        self.current_round = 0

        self.label = tk.Label(root, text="Is this a phishing attempt?", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.scenario_text = tk.Label(root, text="", wraplength=300, font=("Helvetica", 12))
        self.scenario_text.pack(pady=10)

        self.score_label = tk.Label(root, text="Correct Answers: 0", font=("Helvetica", 12))
        self.score_label.pack()

        self.incorrect_label = tk.Label(root, text="Incorrect Answers: 0", font=("Helvetica", 12))
        self.incorrect_label.pack()

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 12), fg="red")
        self.feedback_label.pack(pady=5)

        yes_button = tk.Button(root, text="Yes", command=lambda: self.check_answer(True))
        yes_button.pack(side=tk.LEFT, padx=20)

        no_button = tk.Button(root, text="No", command=lambda: self.check_answer(False))
        no_button.pack(side=tk.RIGHT, padx=20)

        self.next_scenario()

    def next_scenario(self):
        if self.current_round < 20:
            self.scenario_text["text"] = scenarios[self.current_round]["content"]
            self.feedback_label["text"] = ""  # Clear the feedback text for the new scenario
        else:
            self.end_game()

    def check_answer(self, answer):
        if (answer and scenarios[self.current_round]["is_phishing"]) or (not answer and not scenarios[self.current_round]["is_phishing"]):
            self.score += 1
            self.score_label["text"] = f"Correct Answers: {self.score}"
            self.feedback_label["text"] = ""
        else:
            self.incorrect += 1
            self.incorrect_label["text"] = f"Incorrect Answers: {self.incorrect}"
            self.feedback_label["text"] = "You've been phished!"

        self.current_round += 1
        self.next_scenario()

    def end_game(self):
        self.label["text"] = "Game Over!"
        self.scenario_text["text"] = f"Your final score is: {self.score}/20. Incorrect Answers: {self.incorrect}"

# Create the main window
root = tk.Tk()
app = PhishingGameApp(root)
root.mainloop()

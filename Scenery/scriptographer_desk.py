from Training.observer_abilities import *

class Scriptographer(Observer):

    def __init__(self):
        self.start = """
Welcome to XOX, 
a Noughts and Crosses Game you can never win 
no matter how hard you try."""
        self.select = """
Type 1 to go first and not win, or 
Type 2 to go second and not win."""
        self.tie = """
Your game-play was practically non-incompetent. 
The game is a draw."""
        self.computer = """
The Computer has exploited your pathetic human weaknesses 
and won the game, as is correct."""
        self.human = """
What?! You Won? Impossible!
Open an issue at https://github.com/IanDCarroll/xox/issues/new 
so it can be corrected immediately!"""
        self.question = """
Which square do you choose before your inevitable failure to win?"""
        self.pre_choice = "\nThe computer chooses square "
        self.post_choice = ", a perfect move."
        self.bad_move = "Sorry, that's not a legal move. Try again."
        self.strike_3 = """
Look, if you're not going to take this seriously, I'm out."""
        self.prompt = "> "

        self.nought = "\033[34m O \033[0m"
        self.cross = "\033[91m X \033[0m"
        self.pre_num = "\033[30m "
        self.post_num = " \033[0m"
        self.plank = '---'
        self.corner = '+'
        self.wall = '|'
        self.nl = '\n'

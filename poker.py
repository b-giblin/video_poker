import tkinter as tk
from tkinter import messagebox
import random

class Card:
    suits = ['♠', '♣', '♦', '♥']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]

class PokerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Texas Hold'em Poker")
        
        self.deck = Deck()
        self.player_hand = []
        self.computer_hand = []
        self.community_cards = []

        # GUI Elements
        self.player_label = tk.Label(root, text="Your Hand:")
        self.player_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.community_label = tk.Label(root, text="Community Cards:")
        self.community_label.grid(row=2, column=0, columnspan=5, pady=10)
        
        self.deal_button = tk.Button(root, text="Deal", command=self.deal)
        self.deal_button.grid(row=4, column=0, columnspan=5, pady=20)
        
        self.reveal_button = tk.Button(root, text="Reveal Computer's Hand", command=self.reveal, state=tk.DISABLED)
        self.reveal_button.grid(row=5, column=0, columnspan=5, pady=10)

    def deal(self):
        self.player_hand = self.deck.deal(2)
        self.computer_hand = self.deck.deal(2)
        self.community_cards = self.deck.deal(5)
        
        for i, card in enumerate(self.player_hand):
            label = tk.Label(self.root, text=str(card))
            label.grid(row=1, column=i, padx=10)

        for i, card in enumerate(self.community_cards):
            label = tk.Label(self.root, text=str(card))
            label.grid(row=3, column=i, padx=10)

        self.reveal_button['state'] = tk.NORMAL
        self.deal_button['state'] = tk.DISABLED

    def reveal(self):
        hand = " ,".join([str(card) for card in self.computer_hand])
        messagebox.showinfo("Computer's Hand", f"Computer's Hand: {hand}")

        # Here you can also add logic to determine winner based on best 5-card combination
        # For now, just resetting the game

        self.reveal_button['state'] = tk.DISABLED
        self.deal_button['state'] = tk.NORMAL

if __name__ == "__main__":
    root = tk.Tk()
    app = PokerApp(root)
    root.mainloop()
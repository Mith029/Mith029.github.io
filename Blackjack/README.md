# BlackJack
This project is a basic text-based implementation of the popular card game, where the user plays against a computer dealer.

## Requirements
Make sure the following package is installed:
- Random

## How to Use
1. Clone or download the project from GitHub.
2. Install the required library.
3. Open the Blackjack.py file in a IDE or text editor.
4. To increase initial chip count, visit "Chips()" class and change "self.total" variable to desired amount.
5. Run the Blackjack.py file.
6. Follow the instructions on the user interface to start the game.
7. To exit, press n when prompted with "Would you like to play another hand?" message.

## How It works
The game is created using python3 with an interactive user interface where the user will submit their turn as they play against the dealer. 
In Blackjack, each player is dealt two cards face up, while the dealer is dealt one card face up and the other face down. The value of the player's hand is 
the sum of the values of the two cards. The value of an Ace is either 1 or 11, depending on which value is more advantageous for the player. 
Face cards (Kings, Queens, and Jacks) have a value of 10, and all other cards have their face value.

After the initial deal, players can choose to "hit" and receive additional cards to improve their hand, or "stand" and keep their current hand. 
Players can continue to hit until they either reach 21 or "bust" (exceed 21), at which point they lose the game.

Once all players have completed their turns, the dealer reveals their face-down card and must hit until their hand reaches a value of 17 or higher. 
If the dealer busts, all remaining players win. If the dealer's hand is closer to 21 than any player's hand, the dealer wins. 
If a player's hand is closer to 21 than the dealer's hand, that player wins. 

To check out a more extensive review of the rules of blackjack, please reference the following link: *https://bicyclecards.com/how-to-play/blackjack/*
    
## How to Contribute
If you would like to contribute, please follow these steps:

1. Fork the project on GitHub.
2. Clone the forked project to your local machine.
3. Make your changes to the code along with comments.
4. Test your changes to ensure that they work as expected.
5. Create a pull request on GitHub with your changes.

Future improvements include adding support for multiplayer and an improved user interface for a friendlier experience. 
Please ensure that your pull request includes a detailed description of the changes you have made and the reasoning behind them.

## Author 
Mithil Patel

Thank you for checking out the BlackJack project! If you have any questions or feedback, please feel free to reach out.

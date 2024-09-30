# UnoGame
Console based Uno game for developers

## Name
console Uno game

## Description
A Python-based implementation of the classic UNO card game, designed for two players: human vs. computer. This console-based game features color-coordinated cards and auto-enforces the official UNO rules, ensuring a smooth and fair experience.

## Features
Two-player mode: Human player vs. Computer.
All 108 cards included: Implemented the entire UNO deck, including number and action cards (Skip, Reverse, Draw Two, Wild, Wild Draw Four).
Auto-enforced rules: The game automatically enforces the rules, such as drawing a card if you attempt to play an invalid one.
Console-based with color coordination: Cards are displayed with color in the terminal to mimic the real UNO card colors (e.g., Red, Green, Yellow, Blue).
Action cards implemented: All action cards perform their intended effects (Skip turns, Reverse order, Draw Two, Wild, Wild Draw Four).
Draw card enforcement: If a player attempts to play an unplayable card, they must draw a card from the deck automatically.


## Game Rules
The objective of the game is to be the first player (human or computer) to discard all of their cards. The main rules include:

Players take turns playing a card that matches the top card of the discard pile by color or number.
Action cards can force the opponent to skip a turn, draw extra cards, or change the active color.
If a player cannot make a valid move, they must draw a card from the deck.
When a player has only one card left, they must declare UNO (automatically in this case).
The game continues until one player has no more cards or the deck runs out.


## Technologies Used
Python – Used for the main game logic and structure.
Random library – Used for shuffling and distributing cards randomly.
Time library – Used for adding delays to enhance the flow of gameplay, such as simulating the computer's turn.

## Acknowledgment
I would like to express my gratitude to the following individuals for their valuable feedback and support during the development of this project:

Sheila Kruger – for her insightful suggestions on improving the game logic and rules.
Vance Muchongo – for thoroughly testing the game and helping identify bugs.
Thandeka Nkosi – for providing helpful feedback on user experience and game flow.

Thank you for your time and effort!

## License
This project is licensed under the MIT License

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

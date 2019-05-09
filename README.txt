# turtleSoccer.py

## Description
	A "1" v. "1" soccer game using turtles! Two players are required, and each player controls three turtles

## Installation

	Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

	```bash
	pip install pynput
	```

	If you found this, you probably found our github but here it is:
		https://github.com/btulabajr/ME369P-Final-Project

	Download the zip and extract the files. Run turtleSoccer.py.

	On Windows? Use this:
		************************************************REPLACE WITH LINK*************************************************

## How to Play

	Red Player Keyboard Commands:
		"W" - Up
		"S" - Down
		"A" - Left
		"D" - Right
		"E" - Switch to next turtle in forward selection order (see below)
		"Q" - Switch to next turtle in reverse selection order (see below)

	Blue Player Keyboard Commands:
		"I" - Up
		"K" - Down
		"J" - Left
		"L" - Right
		"O" - Switch to next turtle in forward selection order (see below)
		"U" - Switch to next turtle in reverse selection order (see below)

	Turtle Selection Order (let turtles be numbered 1, 2, 3 starting from top to bottom)
		*Note: Turtle #2 will be selected by default when the game starts and so selectionorders will start with Turtle #2
		Forward Selection Order: Turtle #2 --> Turtle #1 --> Turtle #3 --> Turtle #2 --> and so on...
		Reverse Selection Order: Turtle #2 --> Turtle #2 --> Turtle #1 --> Turtle #2 --> and so on...

	Goal of the Game:
		Well, it's soccer. Try to score goals and defend your own goal. Switch between turtles to chase the ball, fall back,
		or place turtles in strategic positions.

	Goaltending Prevention:
		Turtles are NOT ALLOWED in the goalie box. This prevents players from lining up all your turtles in front of our goal
		to defend it.

	End of game:
		The game ends when one Player scores three goals.

## Contributing
	Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

	Please make sure to update tests as appropriate.

## License
	[MIT](https://choosealicense.com/licenses/mit/)
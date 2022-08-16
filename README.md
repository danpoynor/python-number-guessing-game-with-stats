# Python Number Guessing Game With Stats

A number guessing game written in Python 3.

## Run the app

```bash
python3 app.py
```

NOTE: Python 3.10 was used to develop and test this app.

---

## Features

- Welcome text header appears when first run
- Player can pick numbers between 1 and 100
- Non-number guesses are handled with a `ValueError` exception
- Player is informed if their number is outside the range 1-100
- Message appears to let user know the answer is higher or lower than their guess
- After each game ends, the number of attempts at guessing is saved to a list
- After each game ends, the player is shown:
  - Number of attempts at guessing
  - Mean of the saved attempts list
  - Median of the saved attempts list
  - Mode of the saved attempts list
- At the start of each game, the player is shown the current best score (least amount of points) so that they know what they're am supposed to beat.
- User can choose to play again after game is over
- When the game ends, an ending message is shown to the player.

---

## Screenshot Gameplay Example

![Screen Shot 2022-08-16 at 2 04 16 PM](https://user-images.githubusercontent.com/764270/184961774-9530f041-e365-4fa9-ae11-06e5b8c21ad1.png)

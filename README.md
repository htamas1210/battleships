# Battleships

This is the classic battleships game, using the terminal and pygame in python.
You use the terminal for inputting the positions, for either firing or creating the layout for your fleet.

The project was made using the latest available python currently (Python 3.13.5). Have not tested on other versions.
It uses the uv package manager.

![preview battleships](/screenshot/preview.png)

## To run the game:
1. Clone the repository with `git clone https://github.com/htamas1210/battleships.git`, or download it as a zip file, by clicking on the green Download button, then clicking Download Zip. Then unzip it.
2. In the folder that you dowloaded, open a terminal window. Then run the command `uv run main.py` in the terminal, this will run the game. You should see a window pop up, and the terminal asking for you to input the position for your fleet, with instructions.
3. If you are done with the game. In the terminal window press Ctrl+C to exit early.

The bottom grid is the player's grid. The yellow dots will show the position of your fleet. Green dots will show where the enemy fired and missed. Red dots will show if the enemy hit your ship.
The top grid is your enemy's grid. Red dots will show if you hit your enemy's ship, and green dot if you missed.

## Last bit of info
This game was made for the boot.dev 2025 summer hackathon. This is my first major project that I have written without any kind of tutorial (or ai). I am happy with what I have achieved,
but not satisfied! I know the code is a mess and there are a lot of things I could have done better. I will fix them later, or just rewrite the whole thing to be better.
Anyways, this was really fun to make, and to those who try out this really basic and simple game, I hope you enjoy it for what it is, and thank you for trying it out even if you do not vote for it. 

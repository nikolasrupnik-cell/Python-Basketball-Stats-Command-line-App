**Basketball Stats Tracker**

* This program lets you enter basketball stats for players and shows their average points, rebounds, and assists.

**What it does:**

* You type in a player's name and their game stats.

* The program saves the stats.

* You can later select a player and see their average stats per game.

**How it works:**

* The program uses a dictionary to store players.
* Each player’s name is a key, and their stats are saved in lists:

players = {
    "Jordan": {"points": [], "rebounds": [], "assists": []}
}


* Every time you add a game, the numbers get added to these lists.
* Averages are calculated using sum / number of games.

**How to run:**

* Run it in a terminal:

* python basketball_stats.py

* Use the menu to add stats or show player averages.

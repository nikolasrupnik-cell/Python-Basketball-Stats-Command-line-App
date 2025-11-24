A simple command line application to track basketball player statistics and calculate per-game averages.

This demonstrates Python concepts such as data structures, loops, user input, and basic computation.

Each player name is a key in the dictionary, and the value is another dictionary holding their stat categories.

Why this works:

Each stat category stores a list of numbers.

Every game result adds another value to the list.

Averages are calculated using:

Sum of the list

Divided by number of games (length of the list)

This allows multiple games per player without overwriting previous results.

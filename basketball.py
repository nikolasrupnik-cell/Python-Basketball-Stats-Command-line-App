# --- Basketball Stats Tracker ---

players = {}  # dictionary to hold player stats

def add_game_stats():
    name = input("Enter player name: ").strip().title()
    points = int(input("Points scored: "))
    rebounds = int(input("Rebounds: "))
    assists = int(input("Assists: "))

    if name not in players:
        players[name] = {"points": [], "rebounds": [], "assists": []}

    players[name]["points"].append(points)
    players[name]["rebounds"].append(rebounds)
    players[name]["assists"].append(assists)
    print(f"Stats added for {name}!\n")

def show_averages():
    name = input("Enter player to view stats: ").strip().title()
    if name not in players:
        print("Player not found.\n")
        return

    p = players[name]
    avg_points = sum(p["points"]) / len(p["points"])
    avg_rebounds = sum(p["rebounds"]) / len(p["rebounds"])
    avg_assists = sum(p["assists"]) / len(p["assists"])

    print(f"Average stats for {name}:")
    print(f"Points/Game:   {avg_points:.2f}")
    print(f"Rebounds/Game: {avg_rebounds:.2f}")
    print(f"Assists/Game:  {avg_assists:.2f}\n")

def main():
    while True:
        print("1. Add game stats")
        print("2. Show averages")
        print("3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_game_stats()
        elif choice == "2":
            show_averages()
        elif choice == "3":
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()

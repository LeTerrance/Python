#This program averages how much a player scores a game.

# Ask how many games the player played.
def games_played():
    games = int(input("How many games did they play? "))
    return games

ppg = games_played()
total_points = 0

def points_per(ppg, games):
    points = float(input("How many points did they score in three games?: "))
    global total_points
    total_points += points
    return ppg

def display_avg():
    avg = total_points / ppg if ppg > 0 else 0
    print(f"The player's average points per game is: {avg}")
    # Main program
    ppg = games_played()
    points_per(ppg, ppg)
    display_avg()
#Close loop
    
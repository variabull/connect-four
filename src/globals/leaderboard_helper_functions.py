# Leaderboard Helper Functions
# Contributors: Jacob Nettleship
# Date edited: 31/01/22
"""
File containing helper functions for leaderboard operations
"""


def load_leaderboard():
    """
    Read lines from leaderboard text file and store in a dictionary
    """

    leaderboard = {}
    with open('../leaderboard.txt', 'r') as f:
        for item in f.readlines():
            leaderboard[item.split(':')[0]] = item.split(':')[1]
    return leaderboard


def convert_to_array(leaderboard):
    return map(lambda a: f"{a}:{leaderboard[a]}", leaderboard)


def order_leaderboard(leaderboard):
    """
    Take leaderboard as dictionary and sort by score into two arrays
    """

    ordered = {
        'names': [],
        'scores': sorted(list(map(int, leaderboard.values())), reverse=True)
    }
    for score in ordered['scores']:
        for name in leaderboard:
            if int(leaderboard[name]) == score and not name in ordered['names']:
                ordered['names'].append(name)
                break
    return ordered


def save_score(username, score):
    """
    Save the users score
    """

    leaderboard = load_leaderboard()
    if username in leaderboard.keys():  # Checks whether user has played before
        # Updates score in dictionary
        leaderboard[username] = int(leaderboard[username]) + score
        # Writes dictionary to file
        with open('../leaderboard.txt', 'w') as f:
            f.writelines(convert_to_array(leaderboard))
    else:
        # Adds new user to file
        with open('../leaderboard.txt', 'a') as f:
            f.write(f"{username}:{score}\n")

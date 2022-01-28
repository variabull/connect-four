# Leaderboard Helper Functions
# Contributors: Jacob Nettleship
# Date edited: 28/01/22
"""
File containing helper functions for leaderboard operations
"""


def load_leaderboard():
    leaderboard = {}
    with open('../leaderboard.txt', 'r') as f:
        for item in f.readlines():
            leaderboard[item.split(':')[0]] = item.split(':')[1]
    return leaderboard


def convert_to_array(leaderboard):
    return map(lambda a: f"{a}:{leaderboard[a]}\n", leaderboard)


def order_leaderboard(leaderboard):
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
    leaderboard = load_leaderboard()
    if username in leaderboard.keys():
        leaderboard[username] = int(leaderboard[username]) + score
        with open('../leaderboard.txt', 'w') as f:
            f.writelines(convert_to_array(leaderboard))
    else:
        with open('../leaderboard.txt', 'a') as f:
            f.write(f"{username}:{score}\n")

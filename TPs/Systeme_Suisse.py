import json

file_path = 'players.json'
with open(file_path, 'r') as file:
    data = json.load(file)

def get_sorted_players():
    return sorted(data, key=lambda x: x['elo_points'], reverse=True)

def divide_players(players):
    mid = len(players) // 2
    return players[:mid], players[mid:]

def create_pairs(group1, group2):
    pairs = []
    for i in range(len(group1)):
        pairs.append((group1[i], group2[i]))
    return pairs

def main():
    #print(get_sorted_players())
    sorted_players = get_sorted_players()
    group1, group2 = divide_players(sorted_players)
    pairs = create_pairs(group1, group2)

    for pair in pairs:
        player1 = f"{pair[0]['first_name']} {pair[0]['last_name']}"
        player2 = f"{pair[1]['first_name']} {pair[1]['last_name']}"
        print(f"{player1} vs {player2}")

if __name__ == "__main__":
    main()
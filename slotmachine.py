import random

REEL = ('7', 'Bar', 'Cherry', 'Apple', 'Banana', 'Grapes', 'Grapes', 'Banana', 'Apple', 'Banana', 'Grapes', 'Banana', 'Apple')

bet_cost = 1 # Cost in credits of each pull

# Keeps track of the number of times the player hits a 3-in-a-row of each reel face
tracker = {
    "7": 0,
    "Bar": 0,
    "Cherry": 0,
    "Apple": 0,
    "Banana": 0,
    "Grapes": 0,
    "Lose": 0,
}

def pull():
    result_list = []
    for i in range(3):
        index = random.randint(0, len(REEL) - 1)
        result_list.append(REEL[index])
    return result_list

def tableCheck(result):
    global tracker
    global bet_cost

    if not isHit(result):
        tracker['Lose'] += 1
        return -1 * bet_cost
        
    value = result[0]
    if value == '7':
        tracker['7'] += 1
        return 120
    elif value == 'Bar':
        tracker['Bar'] += 1
        return 30
    elif value == 'Apple':
        tracker['Apple'] += 1
        return 8
    elif value == 'Cherry':
        tracker['Cherry'] += 1
        return 3
    elif value == 'Banana':
        tracker['Banana'] += 1
        tracker['Lose'] += 1
        return -1 * bet_cost
    elif value == 'Grapes':
        tracker['Grapes'] += 1
        tracker['Lose'] += 1
        return -1 * bet_cost

def isHit(result):
    if result[0] == result[1] and result[0] == result[2]:
        return True
    return False

def main():
    pull_count = 0 # Keeps track of the number of actual pulls
    starting_credits = int(input('Enter the amount of player coins to start with: '))
    player_credits = starting_credits
    
    jackpot_limit = int(input('Stop after n hitting the jackpot n times (Enter 0 for no limit): '))
    jackpot_counter = 0

    while player_credits > 0:
        pull_count += 1
        result = pull()
        player_credits = player_credits + tableCheck(result)
        if isHit(result) and result[0] == '7':
            jackpot_counter += 1
            if jackpot_limit > 0 and jackpot_counter == jackpot_limit:
                print(f'Jackpot limit of {jackpot_limit} reached.')
                break
        
    global tracker
    print(f'Pulled {pull_count} times.')
    print(f'Game ended with {player_credits} credits left.')
    print(tracker)

if __name__ == "__main__":
    main()
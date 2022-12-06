import random
import matplotlib.pyplot as plt

REEL = ('7', 'Bar', 'Cherry', 'Apple', 'Banana', 'Grapes', 'Grapes', 'Banana', 'Apple', 'Banana', 'Grapes', 'Banana', 'Apple')

bet_cost = 0.5 # Cost in credits of each pull

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

# Tracks the history of wealth/credits relative to the number of turns
wealth_history = []

def pull():
    result_list = []
    for i in range(5):
        index = random.randint(0, len(REEL) - 1)
        result_list.append(REEL[index])
    return result_list

def tableCheck(result):
    global tracker
    global bet_cost

    if not isMatch(result):
        tracker['Lose'] += 1
        return -1 * bet_cost
        
    value = result[0]
    if value == '7':
        tracker['7'] += 1
        return 50000
    elif value == 'Bar':
        tracker['Bar'] += 1
        return 300
    elif value == 'Apple':
        tracker['Apple'] += 1
        return 80
    elif value == 'Cherry':
        tracker['Cherry'] += 1
        return 30
    elif value == 'Banana':
        tracker['Banana'] += 1
        tracker['Lose'] += 1
        return -1 * bet_cost
    elif value == 'Grapes':
        tracker['Grapes'] += 1
        tracker['Lose'] += 1
        return -1 * bet_cost

def isMatch(result):
    if result[0] == result[1] and result[0] == result[2] and result[0] == result[3] and result[0] == result[4]:
        return True
    return False

def getPeak():
    global wealth_history
    peak = 0
    for i in wealth_history:
        if i > peak:
            peak = i
    
    return peak

def main():
    pull_count = 0 # Keeps track of the number of actual pulls
    starting_credits = int(input('Enter the amount of player coins to start with: '))
    player_credits = starting_credits
    wealth_history.append(starting_credits)
    
    jackpot_limit = 0
    try:
        jackpot_limit = int(input('Stop after n hitting the jackpot n times (Enter 0 for no limit): '))
    except:
        jackpot_limit = 0
    jackpot_counter = 0

    while player_credits > 0:
        pull_count += 1
        result = pull()
        player_credits = player_credits + tableCheck(result)
        wealth_history.append(player_credits)
        if isMatch(result) and result[0] == '7':
            jackpot_counter += 1
            if jackpot_limit > 0 and jackpot_counter == jackpot_limit:
                print(f'Jackpot limit of {jackpot_limit} reached.')
                break
        
    global tracker
    print(f'Pulled {pull_count} times.')
    print(f'Game ended with {player_credits} credits left.')
    if player_credits == starting_credits:
        print('Player broke even.')
    elif player_credits < starting_credits:
        print(f'Player at net loss of -{starting_credits - player_credits}')
    elif player_credits > starting_credits:
        print(f'Player at net profit of +{player_credits - starting_credits}')
    print(f'Peak of credits is {getPeak()}')
    print(tracker)
    
    figure, axis = plt.subplots(2, 1)

    axis[0].plot(wealth_history)
    axis[0].set_title('Credit History')

    bar_labels = list(tracker.keys())
    bar_values = list(tracker.values())
    axis[1].bar(bar_labels, bar_values)
    for i in range(len(bar_labels)):
        axis[1].text(i,bar_values[i],bar_values[i], ha='center')
    axis[1].set_title('Likelihood of a match/loss')
    
    plt.show()

if __name__ == "__main__":
    main()